# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import base64
import binascii
import io
from contextlib import asynccontextmanager, contextmanager
from typing import TypeAlias

import httpx
from pydantic import AnyHttpUrl

from friendli_core import (
    AddSamplesResponse,
    AsyncFriendliCore,
    DatasetInfo,
    DedicatedDatasetModality,
    DedicatedDatasetModalityType,
    FileGetDownloadURLResponse,
    FileInitUploadResponse,
    ListSplitsResponse,
    SplitInfo,
    SyncFriendliCore,
)

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

SAMPLE_DATA_T: TypeAlias = bytes
FULL_SAMPLE_ID_T: TypeAlias = str
"""A unique identifier for a sample in a dataset, \
formatted as `{DATASET_ID}:{VERSION_ID}:{SPLIT_ID}:{SAMPLE_ID}`"""
FULL_SAMPLE_ID_DATA_PAIR_T: TypeAlias = tuple[FULL_SAMPLE_ID_T, SAMPLE_DATA_T]


class SyncDataset:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

        self._dataset: DatasetInfo | None = None
        self._project_id: str | None = None
        self._default_split: SplitInfo | None = None
        self._splits: dict[str, SplitInfo] = {}
        """{name: SplitInfo}"""

    @contextmanager
    def create(
        self,
        *,
        modality: list[DedicatedDatasetModalityType],
        name: str,
        project_id: str,
        default_split_name: str = DEFAULT_SPLIT_NAME,
    ):
        """Create a new dataset.

        Args:
            modality: Input modality of the dataset. Note that we only support text output modality for now.
            name: Name of the dataset
            project_id: Project ID
        """
        self._project_id = project_id

        try:
            # Create dataset
            self._dataset = self._core.dataset.create_dataset(
                modality=DedicatedDatasetModality(
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
            self._default_split = self._core.dataset.create_split(
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
    ):
        """Get a dataset.

        Args:
            name: Name of the dataset
            project_id: Project ID
        """

        self._project_id = project_id

        try:
            # Get dataset
            self._dataset = self._core.dataset.get_dataset(
                dataset_id=dataset_id,
                **self._config.model_dump(),
            )

            # Get splits
            prev_cursor = None
            while True:
                list_splits: ListSplitsResponse = self._core.dataset.list_splits(
                    dataset_id=self._dataset.id,
                    cursor=None,
                    limit=None,
                    direction=None,
                    version_id=None,
                    **self._config.model_dump(),
                )
                self._splits.update({split.name: split for split in list_splits.data})
                if list_splits.next_cursor is None:
                    break
                else:
                    # FIXME: This is a temporary fix to avoid infinite loop,
                    # we should fix the backend  to return the correct next_cursor
                    if list_splits.next_cursor == prev_cursor:
                        break
                    else:
                        prev_cursor = list_splits.next_cursor

            self._default_split = self._splits.get(DEFAULT_SPLIT_NAME, None)

            yield self

        finally:
            # TODO: Cleanup if needed
            pass

    def create_split(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> SplitInfo:
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
        if name in self._splits:
            raise ValueError(f"Split '{name}' already exists.")
        split_info = self._core.dataset.create_split(
            dataset_id=self._dataset.id,
            name=name,
            **self._config.model_dump(),
        )
        self._splits[name] = split_info
        return split_info

    def get_split(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> SplitInfo:
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
        if name not in self._splits:
            raise KeyError(f"Split '{name}' does not exist.")
        return self._splits[name]

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
            else self.create_split(name=name).id
        )

    def _process_message(
        self,
        *,
        message: Message,
    ) -> tuple[Message, DedicatedDatasetModality]:
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
        input_modal_set: set[DedicatedDatasetModalityType] = set()
        output_modal_set: set[DedicatedDatasetModalityType] = set(["TEXT"])
        # NOTE: We only support text output modality for now.

        if isinstance(message.root, (SystemMessage, AssistantMessage, ToolMessage)):
            # NOTE: These types don't support multimodal content at the moment, so we skip them.
            input_modal_set.add("TEXT")
            return message, check_modality(
                dataset_modality=self._dataset.modality,
                message_modality=DedicatedDatasetModality(
                    input_modals=list(input_modal_set),
                    output_modals=list(output_modal_set),
                ),
            )

        elif isinstance(message.root, UserMessage):
            if isinstance(message.root.content, str):
                # NOTE: `UserMessageContentString` type, which is a string, so we skip it.
                input_modal_set.add("TEXT")
                return message, check_modality(
                    dataset_modality=self._dataset.modality,
                    message_modality=DedicatedDatasetModality(
                        input_modals=list(input_modal_set),
                        output_modals=list(output_modal_set),
                    ),
                )

            elif isinstance(message.root.content, list):
                # NOTE: `UserMessageContentArray` type
                for content in message.root.content:
                    if isinstance(content.root, TextContent):
                        # NOTE: `TextContent` is a string, so we skip it.
                        input_modal_set.add("TEXT")
                        continue

                    elif isinstance(content.root, AudioContent):
                        input_modal_set.add("AUDIO")
                        original_audio = content.root.audio_url.url
                        content.root.audio_url.url = str(
                            self._upload_to_s3(
                                data=download_from_url(url=original_audio),
                                name=original_audio,
                            )
                        )
                        continue

                    elif isinstance(content.root, ImageContent):
                        input_modal_set.add("IMAGE")
                        if isinstance(content.root.root, ImageUrlData):
                            if isinstance(content.root.root.image_url, str):
                                original_image = content.root.root.image_url
                                content.root.root.image_url = str(
                                    self._upload_to_s3(
                                        data=download_from_url(url=original_image),
                                        name=original_image,
                                    )
                                )

                            elif isinstance(content.root.root.image_url, ImageUrl):
                                original_image = content.root.root.image_url.url
                                content.root.root.image_url = str(
                                    self._upload_to_s3(
                                        data=download_from_url(url=original_image),
                                        name=original_image,
                                    )
                                )

                            else:
                                raise ValueError(
                                    "`image_url` must be a string or ImageUrl."
                                )
                            content.root.root = content.root.root.to_ImageData()
                            continue

                        elif isinstance(content.root.root, ImageData):
                            original_image = content.root.root.image
                            if any(
                                original_image.startswith(prefix)
                                for prefix in BASE64_IMAGE_PREFIXES
                            ):
                                # If base64 image, we upload it to S3 and replace the original image with the S3 URL
                                try:
                                    base64_string = original_image.split(
                                        sep=",", maxsplit=1
                                    )[1]
                                    decoded_data = base64.b64decode(
                                        base64_string, validate=True
                                    )
                                except binascii.Error:
                                    raise ValueError(
                                        "`image` must be a valid base64 string."
                                    )
                                else:
                                    # Replace the original image with the S3 URL
                                    content.root.root.image = str(
                                        self._upload_to_s3(
                                            data=decoded_data,
                                            name=digest(
                                                data=decoded_data
                                            ),  # NOTE: Use the digest as the name for base64 image for now
                                        )
                                    )
                                    continue
                            try:
                                S3Dsn(original_image)
                            except ValueError:
                                try:
                                    AnyHttpUrl(original_image)
                                except ValueError:
                                    raise ValueError(
                                        "`image` must be a valid HTTP URL or S3 URL."
                                    )
                                else:
                                    # If HTTP URL, we download it and upload it to S3 and replace the original URL with the S3 URL
                                    content.root.root.image = str(
                                        self._upload_to_s3(
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
                            self._upload_to_s3(
                                data=download_from_url(url=original_video),
                                name=original_video,
                            )
                        )
                        continue

                    else:
                        raise TypeError(
                            f"Invalid user message content type: {type(content.root)}."
                        )

                return message, check_modality(
                    dataset_modality=self._dataset.modality,
                    message_modality=DedicatedDatasetModality(
                        input_modals=list(input_modal_set),
                        output_modals=list(output_modal_set),
                    ),
                )

            else:
                raise TypeError(
                    f"Invalid user message content type: {type(message.root.content)}."
                )
        else:
            raise TypeError(f"Invalid message type: {type(message.root)}.")

    def _upload_to_s3(
        self,
        *,
        data: bytes,
        name: str,
    ) -> S3Dsn:
        """Upload content to S3 and return the S3 URL.

        Args:
            content: Content to upload
            name: Name of the file

        Returns:
            S3Dsn: S3 URL of uploaded content

        Raises:
            RuntimeError: If upload fails
        """
        # TODO: Batch upload
        try:
            # Initialize upload
            init_upload: FileInitUploadResponse = self._core.file.init_upload(
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
            self._core.file.complete_upload(
                file_id=init_upload.file_id,
                **self._config.model_dump(),
            )

            # Get download URL
            download_url: FileGetDownloadURLResponse = self._core.file.get_download_url(
                file_id=init_upload.file_id,
                **self._config.model_dump(),
            )

            return S3Dsn(download_url.s3_uri)

        except Exception as e:
            raise RuntimeError(f"Failed to upload content to S3: {e}") from e

    def add_samples(
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before adding samples."
            )
        if split not in self._splits:
            raise ValueError(f"Split '{split}' does not exist.")

        processed_samples: list[Sample] = []

        # Process all messages
        for sample in samples:
            processed_messages = []
            for message in sample.messages:
                processed_message, _ = self._process_message(message=message)
                processed_messages.append(processed_message)
            processed_samples.append(Sample(messages=processed_messages))

        # Add samples to the dataset
        res: AddSamplesResponse = self._core.dataset.add_samples(
            dataset_id=self._dataset.id,
            split_id=self._get_or_create_split_id(name=split),
            request_body=[s.to_bytes() for s in processed_samples],
            **self._config.model_dump(),
        )
        return res.samples


class AsyncDataset:
    def __init__(
        self,
        *,
        core: AsyncFriendliCore,
        config: Config,
    ):
        self._core = core
        self._config = config

        self._dataset: DatasetInfo | None = None
        self._project_id: str | None = None
        self._default_split: SplitInfo | None = None
        self._splits: dict[str, SplitInfo] = {}
        """{name: SplitInfo}"""

    @asynccontextmanager
    async def create(
        self,
        *,
        modality: list[DedicatedDatasetModalityType],
        name: str,
        project_id: str,
        default_split_name: str = DEFAULT_SPLIT_NAME,
    ):
        """Create a new dataset.

        Args:
            modality: Input modality of the dataset. Note that we only support text output modality for now.
            name: Name of the dataset
            project_id: Project ID
        """
        self._project_id = project_id
        try:
            # Create dataset
            self._dataset = await self._core.dataset.create_dataset(
                modality=DedicatedDatasetModality(
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
            self._default_split = await self._core.dataset.create_split(
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
    ):
        """Get a dataset.

        Args:
            name: Name of the dataset
            project_id: Project ID
        """
        self._project_id = project_id
        try:
            # Get dataset
            self._dataset = await self._core.dataset.get_dataset(
                dataset_id=dataset_id,
                **self._config.model_dump(),
            )

            # Get splits
            prev_cursor = None
            while True:
                list_splits: ListSplitsResponse = await self._core.dataset.list_splits(
                    dataset_id=self._dataset.id,
                    cursor=None,
                    limit=None,
                    direction=None,
                    version_id=None,
                    **self._config.model_dump(),
                )
                self._splits.update({split.name: split for split in list_splits.data})
                if list_splits.next_cursor is None:
                    break
                else:
                    # FIXME: This is a temporary fix to avoid infinite loop,
                    # we should fix the backend  to return the correct next_cursor
                    if list_splits.next_cursor == prev_cursor:
                        break
                    else:
                        prev_cursor = list_splits.next_cursor

            self._default_split = self._splits.get(DEFAULT_SPLIT_NAME, None)

            yield self

        finally:
            # TODO: Cleanup if needed
            pass

    async def create_split(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> SplitInfo:
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
        if name in self._splits:
            raise ValueError(f"Split '{name}' already exists.")
        split_info = await self._core.dataset.create_split(
            dataset_id=self._dataset.id,
            name=name,
            **self._config.model_dump(),
        )
        self._splits[name] = split_info
        return split_info

    async def get_split(
        self,
        *,
        name: str = DEFAULT_SPLIT_NAME,
    ) -> SplitInfo:
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
        if name not in self._splits:
            raise KeyError(f"Split '{name}' does not exist.")
        return self._splits[name]

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
            else (await self.create_split(name=name)).id
        )

    async def _process_message(
        self,
        *,
        message: Message,
    ) -> tuple[Message, DedicatedDatasetModality]:
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
        input_modal_set: set[DedicatedDatasetModalityType] = set()
        output_modal_set: set[DedicatedDatasetModalityType] = set(["TEXT"])
        # NOTE: We only support text output modality for now.

        if isinstance(message.root, (SystemMessage, AssistantMessage, ToolMessage)):
            # NOTE: These types don't support multimodal content at the moment, so we skip them.
            input_modal_set.add("TEXT")
            return message, check_modality(
                dataset_modality=self._dataset.modality,
                message_modality=DedicatedDatasetModality(
                    input_modals=list(input_modal_set),
                    output_modals=list(output_modal_set),
                ),
            )

        elif isinstance(message.root, UserMessage):
            if isinstance(message.root.content, str):
                # NOTE: `UserMessageContentString` type, which is a string, so we skip it.
                input_modal_set.add("TEXT")
                return message, check_modality(
                    dataset_modality=self._dataset.modality,
                    message_modality=DedicatedDatasetModality(
                        input_modals=list(input_modal_set),
                        output_modals=list(output_modal_set),
                    ),
                )

            elif isinstance(message.root.content, list):
                # NOTE: `UserMessageContentArray` type
                for content in message.root.content:
                    if isinstance(content.root, TextContent):
                        # NOTE: `TextContent` is a string, so we skip it.
                        input_modal_set.add("TEXT")
                        continue

                    elif isinstance(content.root, AudioContent):
                        input_modal_set.add("AUDIO")
                        original_audio = content.root.audio_url.url
                        content.root.audio_url.url = str(
                            await self._upload_to_s3(
                                data=download_from_url(url=original_audio),
                                name=original_audio,
                            )
                        )
                        continue

                    elif isinstance(content.root, ImageContent):
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
                                raise ValueError(
                                    "`image_url` must be a string or ImageUrl."
                                )
                            content.root.root = content.root.root.to_ImageData()
                            continue

                        elif isinstance(content.root.root, ImageData):
                            original_image = content.root.root.image
                            if any(
                                original_image.startswith(prefix)
                                for prefix in BASE64_IMAGE_PREFIXES
                            ):
                                # If base64 image, we upload it to S3 and replace the original image with the S3 URL
                                try:
                                    base64_string = original_image.split(
                                        sep=",", maxsplit=1
                                    )[1]
                                    decoded_data = base64.b64decode(
                                        base64_string, validate=True
                                    )
                                except binascii.Error:
                                    raise ValueError(
                                        "`image` must be a valid base64 string."
                                    )
                                else:
                                    # Replace the original image with the S3 URL
                                    content.root.root.image = str(
                                        await self._upload_to_s3(
                                            data=decoded_data,
                                            name=digest(
                                                data=decoded_data
                                            ),  # NOTE: Use the digest as the name for base64 image for now
                                        )
                                    )
                                    continue
                            try:
                                S3Dsn(original_image)
                            except ValueError:
                                try:
                                    AnyHttpUrl(original_image)
                                except ValueError:
                                    raise ValueError(
                                        "`image` must be a valid HTTP URL or S3 URL."
                                    )
                                else:
                                    # If HTTP URL, we download it and upload it to S3 and replace the original URL with the S3 URL
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
                        raise TypeError(
                            f"Invalid user message content type: {type(content.root)}."
                        )

                return message, check_modality(
                    dataset_modality=self._dataset.modality,
                    message_modality=DedicatedDatasetModality(
                        input_modals=list(input_modal_set),
                        output_modals=list(output_modal_set),
                    ),
                )

            else:
                raise TypeError(
                    f"Invalid user message content type: {type(message.root.content)}."
                )
        else:
            raise TypeError(f"Invalid message type: {type(message.root)}.")

    async def _upload_to_s3(
        self,
        *,
        data: bytes,
        name: str,
    ) -> S3Dsn:
        """Upload content to S3 and return the S3 URL.

        Args:
            content: Content to upload
            name: Name of the file

        Returns:
            S3Dsn: S3 URL of uploaded content

        Raises:
            RuntimeError: If upload fails
        """
        # TODO: Batch upload
        try:
            # Initialize upload
            init_upload: FileInitUploadResponse = await self._core.file.init_upload(
                digest=digest(data=data),
                name=name,
                project_id=self._project_id,
                size=len(data),
                **self._config.model_dump(),
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
            await self._core.file.complete_upload(
                file_id=init_upload.file_id,
                **self._config.model_dump(),
            )

            # Get download URL
            download_url: FileGetDownloadURLResponse = (
                await self._core.file.get_download_url(
                    file_id=init_upload.file_id,
                    **self._config.model_dump(),
                )
            )

            return S3Dsn(download_url.s3_uri)

        except Exception as e:
            raise RuntimeError(f"Failed to upload content to S3: {e}") from e

    async def add_samples(
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before adding samples."
            )
        if split not in self._splits:
            raise ValueError(f"Split '{split}' does not exist.")

        processed_samples: list[Sample] = []

        # Process all messages
        for sample in samples:
            processed_messages = []
            for message in sample.messages:
                processed_message, _ = await self._process_message(message=message)
                processed_messages.append(processed_message)
            processed_samples.append(Sample(messages=processed_messages))

        # Add samples to the dataset
        res: AddSamplesResponse = await self._core.dataset.add_samples(
            dataset_id=self._dataset.id,
            split_id=await self._get_or_create_split_id(name=split),
            request_body=[s.to_bytes() for s in processed_samples],
            **self._config.model_dump(),
        )
        return res.samples
