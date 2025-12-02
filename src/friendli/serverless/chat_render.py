# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Mapping, Optional, Union

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

    from ..config import Config


class SyncChatRender:
    """SyncChatRender."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncChatRender class."""
        self._core = core
        self._config = config

    def render(
        self,
        *,
        model: str,
        messages: Union[List[models.Message], List[models.MessageTypedDict]],
        x_friendli_team: OptionalNullable[str] = UNSET,
        chat_template_kwargs: OptionalNullable[Dict[str, Any]] = UNSET,
        tools: OptionalNullable[
            Union[List[models.Tool], List[models.ToolTypedDict]]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessChatRenderSuccess:
        """Chat render

        Given a list of messages forming a conversation, the API renders them into the final prompt text that will be sent to the model.

        :param model: Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#billing-methods).
        :param messages: A list of messages comprising the conversation so far.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param chat_template_kwargs: Additional keyword arguments supplied to the template renderer. These parameters will be available for use within the chat template.
        :param tools: A list of tools the model may call. Use this to provide a list of functions the model may generate JSON inputs for.  **When `tools` is specified, `min_tokens` and `response_format` fields are unsupported.**
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.serverless.chat_render.render(
            model=model,
            messages=messages,
            x_friendli_team=x_friendli_team,
            chat_template_kwargs=chat_template_kwargs,
            tools=tools,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncChatRender:
    """AsyncChatRender."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncChatRender class."""
        self._core = core
        self._config = config

    async def render(
        self,
        *,
        model: str,
        messages: Union[List[models.Message], List[models.MessageTypedDict]],
        x_friendli_team: OptionalNullable[str] = UNSET,
        chat_template_kwargs: OptionalNullable[Dict[str, Any]] = UNSET,
        tools: OptionalNullable[
            Union[List[models.Tool], List[models.ToolTypedDict]]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessChatRenderSuccess:
        """Chat render

        Given a list of messages forming a conversation, the API renders them into the final prompt text that will be sent to the model.

        :param model: Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#billing-methods).
        :param messages: A list of messages comprising the conversation so far.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param chat_template_kwargs: Additional keyword arguments supplied to the template renderer. These parameters will be available for use within the chat template.
        :param tools: A list of tools the model may call. Use this to provide a list of functions the model may generate JSON inputs for.  **When `tools` is specified, `min_tokens` and `response_format` fields are unsupported.**
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.serverless.chat_render.render(
            model=model,
            messages=messages,
            x_friendli_team=x_friendli_team,
            chat_template_kwargs=chat_template_kwargs,
            tools=tools,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
