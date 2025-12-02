# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Optional, Union

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

    from ..config import Config


class SyncEmbeddings:
    """SyncEmbeddings."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncEmbeddings class."""
        self._core = core
        self._config = config

    def embeddings(
        self,
        *,
        model: str,
        input_: Union[models.Input, models.InputTypedDict],
        x_friendli_team: OptionalNullable[str] = UNSET,
        encoding_format: OptionalNullable[models.EncodingFormat] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEmbeddingsSuccess:
        """Embeddings

        Creates an embedding vector representing the input text.

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param input_: Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param encoding_format: The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.embeddings.embeddings(
            model=model,
            input_=input_,
            x_friendli_team=x_friendli_team,
            encoding_format=encoding_format,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncEmbeddings:
    """AsyncEmbeddings."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncEmbeddings class."""
        self._core = core
        self._config = config

    async def embeddings(
        self,
        *,
        model: str,
        input_: Union[models.Input, models.InputTypedDict],
        x_friendli_team: OptionalNullable[str] = UNSET,
        encoding_format: OptionalNullable[models.EncodingFormat] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEmbeddingsSuccess:
        """Embeddings

        Creates an embedding vector representing the input text.

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param input_: Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param encoding_format: The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.embeddings.embeddings(
            model=model,
            input_=input_,
            x_friendli_team=x_friendli_team,
            encoding_format=encoding_format,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
