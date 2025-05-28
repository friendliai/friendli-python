# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Any, Coroutine, List, Mapping, Optional

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncToken:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def tokenization(
        self,
        *,
        model: str,
        prompt: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessTokenizationSuccess:
        """Tokenization

        By giving a text input, generate a tokenized output of token IDs.

        :param model: Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models).
        :param prompt: Input text prompt to tokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.serverless.token.tokenization(
            model=model,
            prompt=prompt,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def detokenization(
        self,
        *,
        model: str,
        tokens: List[int],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessDetokenizationSuccess:
        """Detokenization

        By giving a list of tokens, generate a detokenized output text string.

        :param model: Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models).
        :param tokens: A token sequence to detokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.serverless.token.detokenization(
            model=model,
            tokens=tokens,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncToken:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def tokenization(
        self,
        *,
        model: str,
        prompt: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessTokenizationSuccess:
        """Tokenization

        By giving a text input, generate a tokenized output of token IDs.

        :param model: Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models).
        :param prompt: Input text prompt to tokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.serverless.token.tokenization(
            model=model,
            prompt=prompt,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def detokenization(
        self,
        *,
        model: str,
        tokens: List[int],
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessDetokenizationSuccess:
        """Detokenization

        By giving a list of tokens, generate a detokenized output text string.

        :param model: Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models).
        :param tokens: A token sequence to detokenize.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.serverless.token.detokenization(
            model=model,
            tokens=tokens,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
