# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncFile:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def init_upload(
        self,
        *,
        digest: str,
        name: str,
        project_id: str,
        size: int,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FileInitUploadResponse:
        """Initiate file upload

        Initiate file upload.

        :param digest: Digest of the file.
        :param name: Name of the file.
        :param project_id: ID of the project the file belongs to.
        :param size: Size of the file in bytes.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.file.init_upload(
            digest=digest,
            name=name,
            project_id=project_id,
            size=size,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def complete_upload(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Complete file upload

        Complete file upload.

        :param file_id: File ID
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.file.complete_upload(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_info(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FileInfo:
        """Get file info

        Get file info.

        :param file_id: File ID
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.file.get_info(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_download_url(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FileGetDownloadURLResponse:
        """Get file download URL

        Get file download URL.

        :param file_id: File ID
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.file.get_download_url(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncFile:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def init_upload(
        self,
        *,
        digest: str,
        name: str,
        project_id: str,
        size: int,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FileInitUploadResponse:
        """Initiate file upload

        Initiate file upload.

        :param digest: Digest of the file.
        :param name: Name of the file.
        :param project_id: ID of the project the file belongs to.
        :param size: Size of the file in bytes.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.file.init_upload(
            digest=digest,
            name=name,
            project_id=project_id,
            size=size,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def complete_upload(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Complete file upload

        Complete file upload.

        :param file_id: File ID
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.file.complete_upload(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_info(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FileInfo:
        """Get file info

        Get file info.

        :param file_id: File ID
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.file.get_info(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_download_url(
        self,
        *,
        file_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FileGetDownloadURLResponse:
        """Get file download URL

        Get file download URL.

        :param file_id: File ID
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.file.get_download_url(
            file_id=file_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
