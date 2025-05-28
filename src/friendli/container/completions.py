# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Any, Coroutine, Mapping, Optional, Union

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable
from friendli_core.utils import eventstreaming

from ..config import Config


class SyncCompletions:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def complete(
        self,
        *,
        request: Union[
            models.ContainerCompletionsBody, models.ContainerCompletionsBodyTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerCompletionsSuccess:
        """Completions

        Generate text based on the given text prompt.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.completions.complete(
            request=request,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def stream(
        self,
        *,
        request: Union[
            models.ContainerCompletionsStreamBody,
            models.ContainerCompletionsStreamBodyTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> eventstreaming.EventStream[models.ContainerCompletionsStreamSuccess]:
        """Stream completions

        Generate text based on the given text prompt.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.completions.stream(
            request=request,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncCompletions:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def complete(
        self,
        *,
        request: Union[
            models.ContainerCompletionsBody, models.ContainerCompletionsBodyTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerCompletionsSuccess:
        """Completions

        Generate text based on the given text prompt.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.completions.complete(
            request=request,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def stream(
        self,
        *,
        request: Union[
            models.ContainerCompletionsStreamBody,
            models.ContainerCompletionsStreamBodyTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> eventstreaming.EventStreamAsync[models.ContainerCompletionsStreamSuccess]:
        """Stream completions

        Generate text based on the given text prompt.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.completions.stream(
            request=request,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
