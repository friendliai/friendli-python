# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Optional, Union

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore
    from friendli.core.utils import eventstreaming

    from ..config import Config


class SyncCompletions:
    """SyncCompletions."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncCompletions class."""
        self._core = core
        self._config = config

    def complete(
        self,
        *,
        dedicated_completions_body: Union[
            models.DedicatedCompletionsBody, models.DedicatedCompletionsBodyTypedDict
        ],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedCompletionsSuccess:
        r"""Completions.

        Generate text based on the given text prompt.

        :param dedicated_completions_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.completions.complete(
            dedicated_completions_body=dedicated_completions_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def stream(
        self,
        *,
        dedicated_completions_stream_body: Union[
            models.DedicatedCompletionsStreamBody,
            models.DedicatedCompletionsStreamBodyTypedDict,
        ],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> eventstreaming.EventStream[models.DedicatedCompletionsStreamSuccess]:
        r"""Stream completions.

        Generate text based on the given text prompt.

        :param dedicated_completions_stream_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.completions.stream(
            dedicated_completions_stream_body=dedicated_completions_stream_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncCompletions:
    """AsyncCompletions."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncCompletions class."""
        self._core = core
        self._config = config

    async def complete(
        self,
        *,
        dedicated_completions_body: Union[
            models.DedicatedCompletionsBody, models.DedicatedCompletionsBodyTypedDict
        ],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedCompletionsSuccess:
        r"""Completions.

        Generate text based on the given text prompt.

        :param dedicated_completions_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.completions.complete(
            dedicated_completions_body=dedicated_completions_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def stream(
        self,
        *,
        dedicated_completions_stream_body: Union[
            models.DedicatedCompletionsStreamBody,
            models.DedicatedCompletionsStreamBodyTypedDict,
        ],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> eventstreaming.EventStreamAsync[models.DedicatedCompletionsStreamSuccess]:
        r"""Stream completions.

        Generate text based on the given text prompt.

        :param dedicated_completions_stream_body:
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.completions.stream(
            dedicated_completions_stream_body=dedicated_completions_stream_body,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
