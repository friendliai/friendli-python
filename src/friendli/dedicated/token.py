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
        model: str,
        prompt: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedTokenizationSuccess:
        r"""Tokenization.

        By giving a text input, generate a tokenized output of token IDs.

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format
            \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param prompt: Input text prompt to tokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.token.tokenize(
            model=model,
            prompt=prompt,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def detokenize(
        self,
        *,
        model: str,
        tokens: List[int],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedDetokenizationSuccess:
        r"""Detokenization.

        By giving a list of tokens, generate a detokenized output text string.

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format
            \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param tokens: A token sequence to detokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.token.detokenize(
            model=model,
            tokens=tokens,
            x_friendli_team=x_friendli_team,
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
        model: str,
        prompt: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedTokenizationSuccess:
        r"""Tokenization.

        By giving a text input, generate a tokenized output of token IDs.

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format
            \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param prompt: Input text prompt to tokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.token.tokenize(
            model=model,
            prompt=prompt,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def detokenize(
        self,
        *,
        model: str,
        tokens: List[int],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedDetokenizationSuccess:
        r"""Detokenization.

        By giving a list of tokens, generate a detokenized output text string.

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format
            \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param tokens: A token sequence to detokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.token.detokenize(
            model=model,
            tokens=tokens,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
