# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import asyncio
import base64
import binascii
import io
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager, contextmanager
from typing import (
    IO,
    Any,
    AsyncIterator,
    Generic,
    Iterator,
    List,
    Mapping,
    Optional,
    TypeAlias,
    TypeVar,
    Union,
)

import httpx
from pydantic import AnyHttpUrl

from friendli_core import (
    AsyncFriendliCore,
    SyncFriendliCore,
    models,
    utils,
)
from friendli_core.types import UNSET, OptionalNullable

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

SAMPLE_DATA_T: TypeAlias = str
FULL_SAMPLE_ID_T: TypeAlias = str
"""A unique identifier for a sample in a dataset, \
formatted as `{DATASET_ID}:{VERSION_ID}:{SPLIT_ID}:{SAMPLE_ID}`"""
FULL_SAMPLE_ID_DATA_PAIR_T: TypeAlias = tuple[FULL_SAMPLE_ID_T, SAMPLE_DATA_T]


TCore = TypeVar("TCore", SyncFriendliCore, AsyncFriendliCore)


class BaseDataset(ABC, Generic[TCore]):
    def __init__(self, core: TCore, config: Config):
        self._core = core
        self._config = config

        self._project_id: str | None = None
        self._dataset: models.DatasetInfo | None = None
        self._default_split: models.SplitInfo | None = None
        self._splits: dict[str, models.SplitInfo] = {}
        """{name: SplitInfo}"""

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

    async def _process_message(
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
        output_modal_set: set[models.DedicatedDatasetModalityType] = set(["TEXT"])
        # NOTE: We only support text output modality for now.

        if isinstance(message.root, (SystemMessage, AssistantMessage, ToolMessage)):
            # NOTE: These types don't support multimodal content at the moment, so we skip them.
            input_modal_set.add("TEXT")
            return message, check_modality(
                dataset_modality=self._dataset.modality,
                message_modality=models.DedicatedDatasetModality(
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
                    message_modality=models.DedicatedDatasetModality(
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
                    message_modality=models.DedicatedDatasetModality(
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

    @abstractmethod
    async def _upload_to_s3(
        self,
        *,
        data: bytes,
        name: str,
    ) -> S3Dsn:
        """Upload content to S3 and return the S3 URI.

        Args:
            data: Content to upload
            name: Name of the file

        Returns:
            S3Dsn: S3 URI of uploaded content

        Raises:
            RuntimeError: If upload fails
        """
        ...


class SyncDataset(BaseDataset[SyncFriendliCore]):
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
            modality: Input modality of the dataset. Note that we only support text output modality for now.
            name: Name of the dataset
            project_id: Project ID
        """
        self._project_id = project_id

        try:
            # Create dataset
            self._dataset = self._core.dataset.create_dataset(
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
    ) -> Iterator[SyncDataset]:
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
                list_splits: models.ListSplitsResponse = self._core.dataset.list_splits(
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

    def get_split_by_name(
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
        if name not in self._splits:
            raise KeyError(f"Split '{name}' does not exist.")
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before adding samples."
            )
        if split not in self._splits:
            raise ValueError(f"Split '{split}' does not exist.")

        # Process samples
        processed_samples: list[Sample] = asyncio.run(
            self._process_samples(samples=samples)
        )

        # Add to the dataset
        res: models.AddSamplesResponse = self._core.dataset.add_samples(
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
            init_upload: models.FileInitUploadResponse = self._core.file.init_upload(
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
            download_url: models.FileGetDownloadURLResponse = (
                self._core.file.get_download_url(
                    file_id=init_upload.file_id,
                    **self._config.model_dump(),
                )
            )

            return S3Dsn(download_url.s3_uri)

        except Exception as e:
            raise RuntimeError(f"Failed to upload content to S3: {e}") from e

    #### Low-Level Methods ####

    def create_dataset(
        self,
        *,
        modality: Union[
            models.DedicatedDatasetModality, models.DedicatedDatasetModalityTypedDict
        ],
        name: str,
        project_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DatasetInfo:
        """Create a new dataset.

        Args:
            modality: Input modality of the dataset. Note that we only support text output modality for now.
            name: Name of the dataset.
            project_id: ID of the project the dataset belongs to.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            DatasetInfo: Information about the created dataset.
        """
        return self._core.dataset.create_dataset(
            modality=modality,
            name=name,
            project_id=project_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def list_datasets(
        self,
        *,
        project_id: str,
        cursor: OptionalNullable[Union[bytes, io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        direction: OptionalNullable[models.Direction] = UNSET,
        name_search: OptionalNullable[str] = UNSET,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListDatasetsResponse:
        """List datasets accessible to the user.

        Args:
            project_id: ID of the project to list datasets from.
            cursor: Cursor for pagination.
            limit: Maximum number of datasets to return.
            direction: Direction to sort results.
            name_search: Search term to filter datasets by name.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            ListDatasetsResponse: List of datasets and pagination information.
        """
        return self._core.dataset.list_datasets(
            project_id=project_id,
            cursor=cursor,
            limit=limit,
            direction=direction,
            name_search=name_search,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_dataset(
        self,
        *,
        dataset_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DatasetInfo:
        """Get information about a specific dataset.

        Args:
            dataset_id: ID of the dataset to retrieve.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            DatasetInfo: Information about the dataset.
        """
        return self._core.dataset.get_dataset(
            dataset_id=dataset_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def delete_dataset(
        self,
        *,
        dataset_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete a specific dataset.

        Args:
            dataset_id: ID of the dataset to delete.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            Any: Response from the server.
        """
        return self._core.dataset.delete_dataset(
            dataset_id=dataset_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def create_version(
        self,
        *,
        dataset_id: str,
        comment: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.VersionInfo:
        """Create a new version of a dataset.

        Args:
            dataset_id: ID of the dataset to create a version for.
            comment: Comment describing the version.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            VersionInfo: Information about the created version.
        """
        return self._core.dataset.create_version(
            dataset_id=dataset_id,
            comment=comment,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def list_versions(
        self,
        *,
        dataset_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListVersionsResponse:
        """List versions of a dataset.

        Args:
            dataset_id: ID of the dataset to list versions for.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            ListVersionsResponse: List of versions and pagination information.
        """
        return self._core.dataset.list_versions(
            dataset_id=dataset_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_version(
        self,
        *,
        dataset_id: str,
        version_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.VersionInfo:
        """Get information about a specific version of a dataset.

        Args:
            dataset_id: ID of the dataset.
            version_id: ID of the version to get.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            VersionInfo: Information about the version.
        """
        return self._core.dataset.get_version(
            dataset_id=dataset_id,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def delete_version(
        self,
        *,
        dataset_id: str,
        version_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete a version

        Delete a version from the dataset.

        :param dataset_id: ID of the dataset.
        :param version_id: ID of the version to delete.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dataset.delete_version(
            dataset_id=dataset_id,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def create_split(
        self,
        *,
        dataset_id: str,
        name: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SplitInfo:
        """Create a new split in a dataset.

        Args:
            dataset_id: ID of the dataset to create a split in.
            name: Name of the split.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            SplitInfo: Information about the created split.
        """
        return self._core.dataset.create_split(
            dataset_id=dataset_id,
            name=name,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def list_splits(
        self,
        *,
        dataset_id: str,
        cursor: OptionalNullable[Union[bytes, io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        direction: OptionalNullable[models.Direction] = UNSET,
        version_id: OptionalNullable[str] = UNSET,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListSplitsResponse:
        """List splits in a dataset.

        Args:
            dataset_id: ID of the dataset to list splits for.
            cursor: Cursor for pagination.
            limit: Maximum number of splits to return.
            direction: Direction to sort results.
            version_id: ID of the version to list splits for.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            ListSplitsResponse: List of splits and pagination information.
        """
        return self._core.dataset.list_splits(
            dataset_id=dataset_id,
            cursor=cursor,
            limit=limit,
            direction=direction,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_split(
        self,
        *,
        dataset_id: str,
        split_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SplitInfo:
        """Get information about a specific split in a dataset.

        Args:
            dataset_id: ID of the dataset.
            split_id: ID of the split to get.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            SplitInfo: Information about the split.
        """
        return self._core.dataset.get_split(
            dataset_id=dataset_id,
            split_id=split_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def delete_split(
        self,
        *,
        dataset_id: str,
        split_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete a specific split from a dataset.

        Args:
            dataset_id: ID of the dataset.
            split_id: ID of the split to delete.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            Any: Response from the server.
        """
        return self._core.dataset.delete_split(
            dataset_id=dataset_id,
            split_id=split_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def add_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        request_body: List[str],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AddSamplesResponse:
        """Add samples

        Add samples to the split.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param request_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dataset.add_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            request_body=request_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def list_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        cursor: OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        direction: OptionalNullable[models.ListSamplesQueryParamDirection] = UNSET,
        version_id: OptionalNullable[str] = UNSET,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListSamplesResponse:
        """List samples

        List samples from the split.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param cursor:
        :param limit:
        :param direction:
        :param version_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dataset.list_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            cursor=cursor,
            limit=limit,
            direction=direction,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def update_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        file: Union[models.FileModel, models.FileModelTypedDict],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AddSamplesResponse:
        """Update samples

        Update samples as raw file.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param file: File to update samples.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dataset.update_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            file=file,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def delete_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        request_body: Union[
            List[models.RequestBody], List[models.RequestBodyTypedDict]
        ],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DeleteSamplesResponse:
        """Delete samples

        Delete samples from the split.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param request_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dataset.delete_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            request_body=request_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncDataset(BaseDataset[AsyncFriendliCore]):
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
        """
        self._project_id = project_id
        try:
            # Create dataset
            self._dataset = await self._core.dataset.create_dataset(
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
    ) -> AsyncIterator[AsyncDataset]:
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
                list_splits: models.ListSplitsResponse = (
                    await self._core.dataset.list_splits(
                        dataset_id=self._dataset.id,
                        cursor=None,
                        limit=None,
                        direction=None,
                        version_id=None,
                        **self._config.model_dump(),
                    )
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before creating splits."
            )
        if name not in self._splits:
            raise KeyError(f"Split '{name}' does not exist.")
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
            raise RuntimeError(
                "No active dataset. You must first create or get a dataset "
                "using create_dataset() or get_dataset() before adding samples."
            )
        if split not in self._splits:
            raise ValueError(f"Split '{split}' does not exist.")

        # Process samples
        processed_samples: list[Sample] = await self._process_samples(samples=samples)

        # Add to the dataset
        res: models.AddSamplesResponse = await self._core.dataset.add_samples(
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
                await self._core.file.init_upload(
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
            await self._core.file.complete_upload(
                file_id=init_upload.file_id,
                **self._config.model_dump(),
            )

            # Get download URL
            download_url: models.FileGetDownloadURLResponse = (
                await self._core.file.get_download_url(
                    file_id=init_upload.file_id,
                    **self._config.model_dump(),
                )
            )

            return S3Dsn(download_url.s3_uri)

        except Exception as e:
            raise RuntimeError(f"Failed to upload content to S3: {e}") from e

    #### Low-Level Methods ####

    async def create_dataset(
        self,
        *,
        modality: Union[
            models.DedicatedDatasetModality, models.DedicatedDatasetModalityTypedDict
        ],
        name: str,
        project_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DatasetInfo:
        """Create a new dataset.

        Args:
            modality: Input modality of the dataset. Note that we only support text output modality for now.
            name: Name of the dataset.
            project_id: ID of the project the dataset belongs to.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            DatasetInfo: Information about the created dataset.
        """
        return await self._core.dataset.create_dataset(
            modality=modality,
            name=name,
            project_id=project_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def list_datasets(
        self,
        *,
        project_id: str,
        cursor: OptionalNullable[Union[bytes, io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        direction: OptionalNullable[models.Direction] = UNSET,
        name_search: OptionalNullable[str] = UNSET,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListDatasetsResponse:
        """List datasets accessible to the user.

        Args:
            project_id: ID of the project to list datasets from.
            cursor: Cursor for pagination.
            limit: Maximum number of datasets to return.
            direction: Direction to sort results.
            name_search: Search term to filter datasets by name.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            ListDatasetsResponse: List of datasets and pagination information.
        """
        return await self._core.dataset.list_datasets(
            project_id=project_id,
            cursor=cursor,
            limit=limit,
            direction=direction,
            name_search=name_search,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_dataset(
        self,
        *,
        dataset_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DatasetInfo:
        """Get information about a specific dataset.

        Args:
            dataset_id: ID of the dataset to retrieve.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            DatasetInfo: Information about the dataset.
        """
        return await self._core.dataset.get_dataset(
            dataset_id=dataset_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def delete_dataset(
        self,
        *,
        dataset_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete a specific dataset.

        Args:
            dataset_id: ID of the dataset to delete.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            Any: Response from the server.
        """
        return await self._core.dataset.delete_dataset(
            dataset_id=dataset_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def create_version(
        self,
        *,
        dataset_id: str,
        comment: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.VersionInfo:
        """Create a new version of a dataset.

        Args:
            dataset_id: ID of the dataset to create a version for.
            comment: Comment describing the version.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            VersionInfo: Information about the created version.
        """
        return await self._core.dataset.create_version(
            dataset_id=dataset_id,
            comment=comment,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def list_versions(
        self,
        *,
        dataset_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListVersionsResponse:
        """List versions of a dataset.

        Args:
            dataset_id: ID of the dataset to list versions for.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            ListVersionsResponse: List of versions and pagination information.
        """
        return await self._core.dataset.list_versions(
            dataset_id=dataset_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_version(
        self,
        *,
        dataset_id: str,
        version_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.VersionInfo:
        """Get information about a specific version of a dataset.

        Args:
            dataset_id: ID of the dataset.
            version_id: ID of the version to get.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            VersionInfo: Information about the version.
        """
        return await self._core.dataset.get_version(
            dataset_id=dataset_id,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def delete_version(
        self,
        *,
        dataset_id: str,
        version_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete a version

        Delete a version from the dataset.

        :param dataset_id: ID of the dataset.
        :param version_id: ID of the version to delete.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dataset.delete_version(
            dataset_id=dataset_id,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def create_split(
        self,
        *,
        dataset_id: str,
        name: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SplitInfo:
        """Create a new split in a dataset.

        Args:
            dataset_id: ID of the dataset to create a split in.
            name: Name of the split.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            SplitInfo: Information about the created split.
        """
        return await self._core.dataset.create_split(
            dataset_id=dataset_id,
            name=name,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def list_splits(
        self,
        *,
        dataset_id: str,
        cursor: OptionalNullable[Union[bytes, io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        direction: OptionalNullable[models.Direction] = UNSET,
        version_id: OptionalNullable[str] = UNSET,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListSplitsResponse:
        """List splits in a dataset.

        Args:
            dataset_id: ID of the dataset to list splits for.
            cursor: Cursor for pagination.
            limit: Maximum number of splits to return.
            direction: Direction to sort results.
            version_id: ID of the version to list splits for.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            ListSplitsResponse: List of splits and pagination information.
        """
        return await self._core.dataset.list_splits(
            dataset_id=dataset_id,
            cursor=cursor,
            limit=limit,
            direction=direction,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_split(
        self,
        *,
        dataset_id: str,
        split_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SplitInfo:
        """Get information about a specific split in a dataset.

        Args:
            dataset_id: ID of the dataset.
            split_id: ID of the split to get.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            SplitInfo: Information about the split.
        """
        return await self._core.dataset.get_split(
            dataset_id=dataset_id,
            split_id=split_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def delete_split(
        self,
        *,
        dataset_id: str,
        split_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete a specific split from a dataset.

        Args:
            dataset_id: ID of the dataset.
            split_id: ID of the split to delete.
            x_friendli_team: ID of team to run requests as (optional parameter).
            retries: Override the default retry configuration for this method.
            server_url: Override the default server URL for this method.
            timeout_ms: Override the default request timeout configuration for this method in milliseconds.
            http_headers: Additional headers to set or replace on requests.

        Returns:
            Any: Response from the server.
        """
        return await self._core.dataset.delete_split(
            dataset_id=dataset_id,
            split_id=split_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def add_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        request_body: List[str],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AddSamplesResponse:
        """Add samples

        Add samples to the split.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param request_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dataset.add_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            request_body=request_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def list_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        cursor: OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        direction: OptionalNullable[models.ListSamplesQueryParamDirection] = UNSET,
        version_id: OptionalNullable[str] = UNSET,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListSamplesResponse:
        """List samples

        List samples from the split.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param cursor:
        :param limit:
        :param direction:
        :param version_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dataset.list_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            cursor=cursor,
            limit=limit,
            direction=direction,
            version_id=version_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def update_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        file: Union[models.FileModel, models.FileModelTypedDict],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AddSamplesResponse:
        """Update samples

        Update samples as raw file.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param file: File to update samples.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dataset.update_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            file=file,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def delete_samples(
        self,
        *,
        dataset_id: str,
        split_id: str,
        request_body: Union[
            List[models.RequestBody], List[models.RequestBodyTypedDict]
        ],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DeleteSamplesResponse:
        """Delete samples

        Delete samples from the split.

        :param dataset_id: ID of the dataset.
        :param split_id: ID of the split.
        :param request_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dataset.delete_samples(
            dataset_id=dataset_id,
            split_id=split_id,
            request_body=request_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
