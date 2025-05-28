# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Any, Coroutine, Mapping, Optional, Union

import httpx

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncFiles:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def upload(
        self,
        *,
        file: Union[models.File, models.FileTypedDict],
        purpose: models.Purpose,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesUploadResult:
        """Files upload

        Uploads a file.

        :param file: The File object (not file name) to be uploaded.
        :param purpose: The intended purpose of the uploaded file. One of `batch` or `model`.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.platform.files.upload(
            file=file,
            purpose=purpose,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def list(
        self,
        *,
        x_friendli_team: OptionalNullable[str] = UNSET,
        after: OptionalNullable[str] = UNSET,
        limit: OptionalNullable[int] = 10000,
        order: OptionalNullable[models.Order] = "desc",
        purpose: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesListResult:
        """Files list

        List files.

        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param after: File ID after which to fetch the next page of results. Optional.
        :param limit: Maximum number of files to return, between [1, 10,000]. Defaults to 10,000.
        :param order: Sort order by `created` timestamp. Use `asc` for ascending or `desc` for descending. Defaults to `desc`.
        :param purpose: Return files with the specified purpose. Optional.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.platform.files.list(
            x_friendli_team=x_friendli_team,
            after=after,
            limit=limit,
            order=order,
            purpose=purpose,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def retrieve(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesRetrieveResult:
        """File retrieve

        Retrieves a file info.

        :param file_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.platform.files.retrieve(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def delete(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesDeleteResult:
        """Files delete

        Deletes a file.

        :param file_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.platform.files.delete(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def download(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Response:
        """Files download

        Downloads a file.

        :param file_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.platform.files.download(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncFiles:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def upload(
        self,
        *,
        file: Union[models.File, models.FileTypedDict],
        purpose: models.Purpose,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesUploadResult:
        """Files upload

        Uploads a file.

        :param file: The File object (not file name) to be uploaded.
        :param purpose: The intended purpose of the uploaded file. One of `batch` or `model`.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.platform.files.upload(
            file=file,
            purpose=purpose,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def list(
        self,
        *,
        x_friendli_team: OptionalNullable[str] = UNSET,
        after: OptionalNullable[str] = UNSET,
        limit: OptionalNullable[int] = 10000,
        order: OptionalNullable[models.Order] = "desc",
        purpose: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesListResult:
        """Files list

        List files.

        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param after: File ID after which to fetch the next page of results. Optional.
        :param limit: Maximum number of files to return, between [1, 10,000]. Defaults to 10,000.
        :param order: Sort order by `created` timestamp. Use `asc` for ascending or `desc` for descending. Defaults to `desc`.
        :param purpose: Return files with the specified purpose. Optional.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.platform.files.list(
            x_friendli_team=x_friendli_team,
            after=after,
            limit=limit,
            order=order,
            purpose=purpose,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def retrieve(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesRetrieveResult:
        """File retrieve

        Retrieves a file info.

        :param file_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.platform.files.retrieve(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def delete(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlatformFilesDeleteResult:
        """Files delete

        Deletes a file.

        :param file_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.platform.files.delete(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def download(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Response:
        """Files download

        Downloads a file.

        :param file_id:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.platform.files.download(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
