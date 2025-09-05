# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Mapping, Optional

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

    from ..config import Config


class SyncToken:
    """SyncToken."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncToken class."""
        self._core = core
        self._config = config

    def tokenize(
        self,
        *,
        prompt: str,
        model: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerTokenizationSuccess:
        """Tokenization.

        By giving a text input, generate a tokenized output of token IDs.

        :param prompt: Input text prompt to tokenize.
        :param model: Routes the request to a specific adapter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.token.tokenize(
            prompt=prompt,
            model=model,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def detokenize(
        self,
        *,
        tokens: List[int],
        model: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerDetokenizationSuccess:
        """Detokenization.

        By giving a list of tokens, generate a detokenized output text string.

        :param tokens: A token sequence to detokenize.
        :param model: Routes the request to a specific adapter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.token.detokenize(
            tokens=tokens,
            model=model,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncToken:
    """AsyncToken."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncToken class."""
        self._core = core
        self._config = config

    async def tokenize(
        self,
        *,
        prompt: str,
        model: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerTokenizationSuccess:
        """Tokenization.

        By giving a text input, generate a tokenized output of token IDs.

        :param prompt: Input text prompt to tokenize.
        :param model: Routes the request to a specific adapter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.token.tokenize(
            prompt=prompt,
            model=model,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def detokenize(
        self,
        *,
        tokens: List[int],
        model: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerDetokenizationSuccess:
        """Detokenization.

        By giving a list of tokens, generate a detokenized output text string.

        :param tokens: A token sequence to detokenize.
        :param model: Routes the request to a specific adapter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.token.detokenize(
            tokens=tokens,
            model=model,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
