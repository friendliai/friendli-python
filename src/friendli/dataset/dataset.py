# Copyright (c) 2025-present, FriendliAI Corp. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import asyncio
import base64
import binascii
import io
from contextlib import asynccontextmanager, contextmanager
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Iterator,
    Optional,
    TypeAlias,
)

import httpx
from pydantic import AnyHttpUrl

from friendli.core import models
from friendli.core.dataset import AsyncDataset as _CoreAsyncDataset
from friendli.core.dataset import SyncDataset as _CoreSyncDataset

from ..config import DEFAULT_SPLIT_NAME, Config
from ..models import (
    BASE64_IMAGE_PREFIXES,
    AssistantMessage,
    AudioContent,
    ImageContent,
    ImageData,
    ImageUrl,
    ImageUrlData,
    Message,
    S3Dsn,
    Sample,
    SystemMessage,
    TextContent,
    ToolMessage,
    UserMessage,
    VideoContent,
)
from ..utils import (
    check_modality,
    digest,
    download_from_url,
)

if TYPE_CHECKING:
    from .. import AsyncFriendli, SyncFriendli

SAMPLE_DATA_T: TypeAlias = str
FULL_SAMPLE_ID_T: TypeAlias = str
"""A unique identifier for a sample in a dataset, \
formatted as `{DATASET_ID}:{VERSION_ID}:{SPLIT_ID}:{SAMPLE_ID}`"""
FULL_SAMPLE_ID_DATA_PAIR_T: TypeAlias = tuple[FULL_SAMPLE_ID_T, SAMPLE_DATA_T]


class _DatasetMixin:
    """Client-side dataset state and sample-processing helpers.

    Mixed into the generated core dataset SDK so that the high-level helpers below
    (S3-backed sample uploads, multimodal processing) sit alongside the inherited,
    auto-generated CRUD operations. The active dataset/split context is tracked per
    instance and consumed by the high-level methods.
    """

    parent_ref: object

    def _init_dataset_state(self) -> None:
        self._project_id: Optional[str] = None
        self._dataset: Optional[models.DatasetInfo] = None
        self._default_split: Optional[models.SplitInfo] = None
        self._splits: dict[str, models.SplitInfo] = {}
        """{name: SplitInfo}"""

    @property
    def _config(self) -> Config:
        """The Config carried by the owning ``SyncFriendli`` / ``AsyncFriendli``."""
        return self._root.config

    @property
    def _root(self) -> "SyncFriendli | AsyncFriendli":
        """The owning top-level SDK instance (set as ``parent_ref`` on creation)."""
        return self.parent_ref  # type: ignore[return-value]

    #### Helper Methods ####
    async def _process_samples(self, samples: list[Sample]) -> list[Sample]:
        """Process samples.

        Args:
            samples: List of samples to process

        Returns:
            list[Sample]: Processed samples
        """
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(self._process_sample(sample)) for sample in samples]
        return [task.result() for task in tasks]

    async def _process_sample(self, sample: Sample) -> Sample:
        """Process a sample.

        Args:
            sample: Sample to process

        Returns:
            Sample: Processed sample
        """
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(self._process_message(message=msg))
                for msg in sample.messages
            ]
        return Sample(messages=[task.result()[0] for task in tasks])

    async def _process_message(  # noqa: PLR0912, PLR0915, C901
        self,
        *,
        message: Message,
    ) -> tuple[Message, models.DedicatedDatasetModality]:
        """Process a message.

        Args:
            message: Message to process

        Returns:
            Message: Processed message
            DedicatedDatasetModality: Modality of the messages

        Raises:
            TypeError: If message type is not supported
            ValueError: If message modality is not compatible with dataset modality
        """
        input_modal_set: set[models.DedicatedDatasetModalityType] = set()
        output_modal_set: set[models.DedicatedDatasetModalityType] = {"TEXT"}
        # NOTE: We only support text output modality for now.

        if isinstance(message.root, (SystemMessage, AssistantMessage, ToolMessage)):
            # NOTE: These types don't support multimodal content at the moment,
            #       so we skip them.
            input_modal_set.add("TEXT")
            return message, check_modality(
                dataset_modality=self._dataset.modality,
                message_modality=models.DedicatedDatasetModality(
                    input_modals=list(input_modal_set),
                    output_modals=list(output_modal_set),
                ),
            )

        if isinstance(message.root, UserMessage):
            if isinstance(message.root.content, str):
                # NOTE: `UserMessageContentString` type, which is a string, so we
                #       skip it.
                input_modal_set.add("TEXT")
                return message, check_modality(
                    dataset_modality=self._dataset.modality,
                    message_modality=models.DedicatedDatasetModality(
                        input_modals=list(input_modal_set),
                        output_modals=list(output_modal_set),
                    ),
                )

            if isinstance(message.root.content, list):
                # NOTE: `UserMessageContentArray` type
                for content in message.root.content:
                    if isinstance(content.root, TextContent):
                        # NOTE: `TextContent` is a string, so we skip it.
                        input_modal_set.add("TEXT")
                        continue

                    if isinstance(content.root, AudioContent):
                        input_modal_set.add("AUDIO")
                        original_audio = content.root.audio_url.url
                        content.root.audio_url.url = str(
                            await self._upload_to_s3(
                                data=download_from_url(url=original_audio),
                                name=original_audio,
                            )
                        )
                        continue

                    if isinstance(content.root, ImageContent):
                        input_modal_set.add("IMAGE")
                        if isinstance(content.root.root, ImageUrlData):
                            if isinstance(content.root.root.image_url, str):
                                original_image = content.root.root.image_url
                                content.root.root.image_url = str(
                                    await self._upload_to_s3(
                                        data=download_from_url(url=original_image),
                                        name=original_image,
                                    )
                                )

                            elif isinstance(content.root.root.image_url, ImageUrl):
                                original_image = content.root.root.image_url.url
                                content.root.root.image_url = str(
                                    await self._upload_to_s3(
                                        data=download_from_url(url=original_image),
                                        name=original_image,
                                    )
                                )

                            else:
                                msg = "`image_url` must be a string or ImageUrl."
                                raise ValueError(msg)  # noqa: TRY004
                            content.root.root = content.root.root.to_image_data()
                            continue

                        if isinstance(content.root.root, ImageData):
                            original_image = content.root.root.image
                            if any(
                                original_image.startswith(prefix)
                                for prefix in BASE64_IMAGE_PREFIXES
                            ):
                                # If base64 image, we upload it to S3 and replace the
                                # original image with the S3 URL
                                try:
                                    base64_string = original_image.split(
                                        sep=",", maxsplit=1
                                    )[1]
                                    decoded_data = base64.b64decode(
                                        base64_string, validate=True
                                    )
                                except binascii.Error:
                                    msg = "`image` must be a valid base64 string."
                                    raise ValueError(msg) from None
                                else:
                                    # Replace the original image with the S3 URL
                                    content.root.root.image = str(
                                        await self._upload_to_s3(
                                            data=decoded_data,
                                            name=digest(data=decoded_data),
                                            # NOTE: Use the digest as the name for
                                            # base64 image for now
                                        )
                                    )
                                    continue
                            try:
                                S3Dsn(original_image)
                            except ValueError:
                                try:
                                    AnyHttpUrl(original_image)
                                except ValueError:
                                    msg = "`image` must be a valid HTTP URL or S3 URL."
                                    raise ValueError(msg) from None
                                else:
                                    # If HTTP URL, we download it and upload it to S3
                                    # and replace the original URL with the S3 URL
                                    content.root.root.image = str(
                                        await self._upload_to_s3(
                                            data=download_from_url(url=original_image),
                                            name=original_image,
                                        )
                                    )
                                    continue
                            else:
                                # if S3 URL, no need to re-upload, so we skip it
                                # TODO: We may need to check if user-provided S3 URL belongs to our S3 bucket
                                continue

                    elif isinstance(content.root, VideoContent):
                        input_modal_set.add("VIDEO")
                        original_video = content.root.video_url.url
                        content.root.video_url.url = str(
                            await self._upload_to_s3(
                                data=download_from_url(url=original_video),
                                name=original_video,
                            )
                        )
                        continue

                    else:
                        msg = (
                            f"Invalid user message content type: {type(content.root)}."
                        )
                        raise TypeError(msg)

                return message, check_modality(
                    dataset_modality=self._dataset.modality,
                    message_modality=models.DedicatedDatasetModality(
                        input_modals=list(input_modal_set),
                        output_modals=list(output_modal_set),
                    ),
                )

            msg = f"Invalid user message content type: {type(message.root.content)}."
            raise TypeError(msg)

        msg = f"Invalid message type: {type(message.root)}."
        raise TypeError(msg)

    async def _upload_to_s3(self, *, data: bytes, name: str) -> S3Dsn:
        """Upload content to S3 and return the S3 URI.

        Implemented by the sync/async subclasses.
        """
        raise NotImplementedError


class SyncDataset(_DatasetMixin, _CoreSyncDataset):
    """Dataset SDK with high-level, S3-backed sample upload helpers (synchronous)."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the SyncDataset class."""
        super().__init__(*args, **kwargs)  # type: ignore[arg-type]
        self._init_dataset_state()

    @property
    def _root(self) -> "SyncFriendli":
        return self.parent_ref  # type: ignore[return-value]

    #### High-Level Methods ####
    @contextmanager
    def create(
        self,
        *,
        modality: list[models.DedicatedDatasetModalityType],
        name: str,
        project_id: str,
        default_split_name: str = DEFAULT_SPLIT_NAME,
    ) -> Iterator[SyncDataset]:
        """Create a new dataset.

        Args:
            modality: Input modality of the dataset. Note that we only support text
                output modality for now.
            name: Name of the dataset
            project_id: Project ID
            default_split_name: Name of the default split to create
        """
        self._project_id = project_id

        try:
            # Create dataset
            self._dataset = self.create_dataset(
                modality=models.DedicatedDatasetModality(
                    input_modals=modality,
                    output_modals=[
                        "TEXT"
                    ],  # NOTE: We only support text output modality for now
                ),
                name=name,
                project_id=project_id,
                **self._config.model_dump(),
            )

            # Create default split
            self._default_split = self.create_split(
                dataset_id=self._dataset.id,
                name=default_split_name,
                **self._config.model_dump(),
            )
            self._splits[default_split_name] = self._default_split

            yield self

        finally:
            # TODO: Cleanup if needed
            pass

    @contextmanager
    def get(
        self,
        *,
        dataset_id: str,
        project_id: str,
    ) -> Iterator[SyncDataset]:
        """Get a dataset.

        Args:
            dataset_id: ID of the dataset
            project_id: Project ID
        """
        self._project_id = project_id

        try:
            # Get dataset
            self._dataset = self.get_dataset(
                dataset_id=dataset_id,
                **self._config.model_dump(),
            )

            # Get splits
            prev_cursor = None
            while True:
                list_splits: models.ListSplitsResponse = self.list_splits(
                    dataset_id=self._dataset.id,
                    cursor=None,
                    limit=None,
                    direction=None,
                    version_id=None,
                    **self._config.model_dump(),
                )
                self._splits.update({split.name: split for split in list_splits.data})
                if (
                    list_splits.next_cursor is None
                    or list_splits.next_cursor == prev_cursor
                ):
                    break
                else:
                    prev_cursor = list_splits.next_cursor

            self._default_split = self._splits.get(DEFAULT_SPLIT_NAME, None)

            yield self

        finally:
            # TODO: Cleanup if needed
            pass

    def add_split(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> models.SplitInfo:
        """Create a new split in the dataset.

        Args:
            name: Name of the split to create

        Returns:
            SplitInfo: Information about the created split

        Raises:
            RuntimeError: If no dataset is active
            ValueError: If split with given name already exists
        """
        if self._dataset is None:
            msg = (
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
            raise RuntimeError(msg)
        if name in self._splits:
            msg = f"Split '{name}' already exists."
            raise ValueError(msg)
        split_info = self.create_split(
            dataset_id=self._dataset.id,
            name=name,
            **self._config.model_dump(),
        )
        self._splits[name] = split_info
        return split_info

    def get_split_by_name(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> models.SplitInfo:
        """Get the information for a split, returns the default split if not specified.

        Args:
            name: Name of the split to get. If `None`, returns the default split.

        Returns:
            SplitInfo: Information about the split

        Raises:
            RuntimeError: If no dataset is active
            KeyError: If split with given name does not exist
        """
        if self._dataset is None:
            msg = (
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
            raise RuntimeError(msg)
        if name not in self._splits:
            msg = f"Split '{name}' does not exist."
            raise KeyError(msg)
        return self._splits[name]

    def upload_samples(
        self,
        *,
        samples: list[Sample],
        split: str = DEFAULT_SPLIT_NAME,
    ) -> list[FULL_SAMPLE_ID_DATA_PAIR_T]:
        """Add multiple samples to the dataset.

        Args:
            samples: List of samples, where each sample is a list of messages
            split: Split name to add the samples to. If not specified, uses default split.

        Returns:
            List of tuples, where each tuple contains a full sample ID and the sample data.

        Raises:
            RuntimeError: If no dataset is active
            ValueError: If split with given name does not exist
        """
        if self._dataset is None:
            msg = (
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before adding samples."
            )
            raise RuntimeError(msg)
        if split not in self._splits:
            msg = f"Split '{split}' does not exist."
            raise ValueError(msg)

        # Process samples
        processed_samples: list[Sample] = asyncio.run(
            self._process_samples(samples=samples)
        )

        # Add to the dataset
        res: models.AddSamplesResponse = self.add_samples(
            dataset_id=self._dataset.id,
            split_id=self._get_or_create_split_id(name=split),
            request_body=[s.model_dump_json() for s in processed_samples],
            **self._config.model_dump(),
        )
        return res.samples

    #### Helper Methods ####

    def _get_or_create_split_id(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> str:
        """Given a split name, get its ID. If it doesn't exist, create it.

        Args:
            name: Name of the split to get.

        Returns:
            str: ID of the split
        """
        return (
            self._splits[name].id
            if name in self._splits
            else self.create_split(dataset_id=self._dataset.id, name=name).id
        )

    async def _upload_to_s3(
        self,
        *,
        data: bytes,
        name: str,
    ) -> S3Dsn:
        # TODO: Batch upload
        try:
            # Initialize upload
            init_upload: models.FileInitUploadResponse = self._root.file.init_upload(
                digest=digest(data=data),
                name=name,
                project_id=self._project_id,
                size=len(data),
                **self._config.model_dump(),
            )

            # upload_url is None if the file is already uploaded to S3
            if init_upload.upload_url is not None:
                # Upload to S3
                httpx.post(
                    url=init_upload.upload_url,
                    data=init_upload.aws,
                    files={"file": io.BytesIO(data)},
                    timeout=60,  # TODO: Determine timeout
                ).raise_for_status()

            # Complete upload
            self._root.file.complete_upload(
                file_id=init_upload.file_id,
                **self._config.model_dump(),
            )

            # Get download URL
            download_url: models.FileGetDownloadURLResponse = (
                self._root.file.get_download_url(
                    file_id=init_upload.file_id,
                    **self._config.model_dump(),
                )
            )

            return S3Dsn(download_url.s3_uri)

        except Exception as e:
            msg = f"Failed to upload content to S3: {e}"
            raise RuntimeError(msg) from e


class AsyncDataset(_DatasetMixin, _CoreAsyncDataset):
    """Dataset SDK with high-level, S3-backed sample upload helpers (asynchronous)."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the AsyncDataset class."""
        super().__init__(*args, **kwargs)  # type: ignore[arg-type]
        self._init_dataset_state()

    @property
    def _root(self) -> "AsyncFriendli":
        return self.parent_ref  # type: ignore[return-value]

    #### High-Level Methods ####

    @asynccontextmanager
    async def create(
        self,
        *,
        modality: list[models.DedicatedDatasetModalityType],
        name: str,
        project_id: str,
        default_split_name: str = DEFAULT_SPLIT_NAME,
    ) -> AsyncIterator[AsyncDataset]:
        """Create a new dataset.

        Args:
            modality: Input modality of the dataset. Note that we only support text output modality for now.
            name: Name of the dataset
            project_id: Project ID
            default_split_name: Name of the default split to create
        """
        self._project_id = project_id
        try:
            # Create dataset
            self._dataset = await self.create_dataset(
                modality=models.DedicatedDatasetModality(
                    input_modals=modality,
                    output_modals=[
                        "TEXT"
                    ],  # NOTE: We only support text output modality for now
                ),
                name=name,
                project_id=project_id,
                **self._config.model_dump(),
            )

            # Create default split
            self._default_split = await self.create_split(
                dataset_id=self._dataset.id,
                name=default_split_name,
                **self._config.model_dump(),
            )
            self._splits[default_split_name] = self._default_split

            yield self

        finally:
            # TODO: Cleanup if needed
            pass

    @asynccontextmanager
    async def get(
        self,
        *,
        dataset_id: str,
        project_id: str,
    ) -> AsyncIterator[AsyncDataset]:
        """Get a dataset.

        Args:
            dataset_id: ID of the dataset
            project_id: Project ID
        """
        self._project_id = project_id
        try:
            # Get dataset
            self._dataset = await self.get_dataset(
                dataset_id=dataset_id,
                **self._config.model_dump(),
            )

            # Get splits
            prev_cursor = None
            while True:
                list_splits: models.ListSplitsResponse = await self.list_splits(
                    dataset_id=self._dataset.id,
                    cursor=None,
                    limit=None,
                    direction=None,
                    version_id=None,
                    **self._config.model_dump(),
                )
                self._splits.update({split.name: split for split in list_splits.data})
                if (
                    list_splits.next_cursor is None
                    or list_splits.next_cursor == prev_cursor
                ):
                    break
                else:
                    prev_cursor = list_splits.next_cursor

            self._default_split = self._splits.get(DEFAULT_SPLIT_NAME, None)

            yield self

        finally:
            # TODO: Cleanup if needed
            pass

    async def add_split(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> models.SplitInfo:
        """Create a new split in the dataset.

        Args:
            name: Name of the split to create

        Returns:
            SplitInfo: Information about the created split

        Raises:
            RuntimeError: If no dataset is active
            ValueError: If split with given name already exists
        """
        if self._dataset is None:
            msg = (
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
            raise RuntimeError(msg)
        if name in self._splits:
            msg = f"Split '{name}' already exists."
            raise ValueError(msg)
        split_info = await self.create_split(
            dataset_id=self._dataset.id,
            name=name,
            **self._config.model_dump(),
        )
        self._splits[name] = split_info
        return split_info

    async def get_split_by_name(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> models.SplitInfo:
        """Get the information for a split, returns for the default split if not specified.

        Args:
            name: Name of the split to get. If `None`, returns the default split.

        Returns:
            SplitInfo: Information about the split

        Raises:
            RuntimeError: If no dataset is active
            KeyError: If split with given name does not exist
        """
        if self._dataset is None:
            msg = (
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
            raise RuntimeError(msg)
        if name not in self._splits:
            msg = f"Split '{name}' does not exist."
            raise KeyError(msg)
        return self._splits[name]

    async def upload_samples(
        self,
        *,
        samples: list[Sample],
        split: str = DEFAULT_SPLIT_NAME,
    ) -> list[FULL_SAMPLE_ID_DATA_PAIR_T]:
        """Add multiple samples to the dataset.

        Args:
            samples: List of samples, where each sample is a list of messages
            split: Split name to add the samples to. If not specified, uses default split.

        Returns:
            List of tuples, where each tuple contains a full sample ID and the sample data.

        Raises:
            RuntimeError: If no dataset is active
            ValueError: If split with given name does not exist
        """
        if self._dataset is None:
            msg = (
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before adding samples."
            )
            raise RuntimeError(msg)
        if split not in self._splits:
            msg = f"Split '{split}' does not exist."
            raise ValueError(msg)

        # Process samples
        processed_samples: list[Sample] = await self._process_samples(samples=samples)

        # Add to the dataset
        res: models.AddSamplesResponse = await self.add_samples(
            dataset_id=self._dataset.id,
            split_id=await self._get_or_create_split_id(name=split),
            request_body=[s.model_dump_json() for s in processed_samples],
            **self._config.model_dump(),
        )
        return res.samples

    #### Helper Methods ####

    async def _get_or_create_split_id(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> str:
        """Given a split name, get its ID. If it doesn't exist, create it.

        Args:
            name: Name of the split to get.

        Returns:
            str: ID of the split
        """
        return (
            self._splits[name].id
            if name in self._splits
            else (await self.create_split(dataset_id=self._dataset.id, name=name)).id
        )

    async def _upload_to_s3(
        self,
        *,
        data: bytes,
        name: str,
    ) -> S3Dsn:
        # TODO: Batch upload
        try:
            # Initialize upload
            init_upload: models.FileInitUploadResponse = (
                await self._root.file.init_upload(
                    digest=digest(data=data),
                    name=name,
                    project_id=self._project_id,
                    size=len(data),
                    **self._config.model_dump(),
                )
            )

            # upload_url is None if the file is already uploaded to S3
            if init_upload.upload_url is not None:
                # Upload to S3
                async with httpx.AsyncClient() as client:
                    await client.post(
                        url=init_upload.upload_url,
                        data=init_upload.aws,
                        files={"file": io.BytesIO(data)},
                        timeout=60,  # TODO: Determine timeout
                    )

            # Complete upload
            await self._root.file.complete_upload(
                file_id=init_upload.file_id,
                **self._config.model_dump(),
            )

            # Get download URL
            download_url: models.FileGetDownloadURLResponse = (
                await self._root.file.get_download_url(
                    file_id=init_upload.file_id,
                    **self._config.model_dump(),
                )
            )

            return S3Dsn(download_url.s3_uri)

        except Exception as e:
            msg = f"Failed to upload content to S3: {e}"
            raise RuntimeError(msg) from e
