# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Optional

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

    from ..config import Config


class SyncModel:
    """Model."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncModel class."""
        self._core = core
        self._config = config

    def list(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessModelListSuccess:
        r"""Retrieve serverless models.

        Retrieve list of serverless models.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this
            method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.serverless.model.list(
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncModel:
    """Model."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncModel class."""
        self._core = core
        self._config = config

    async def list(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessModelListSuccess:
        r"""Retrieve serverless models.

        Retrieve list of serverless models.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this
            method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.serverless.model.list(
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
