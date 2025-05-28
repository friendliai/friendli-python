# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Any, Coroutine, List, Mapping, Optional

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncKnowledge:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def retrieve(
        self,
        *,
        k: int,
        knowledge_ids: List[str],
        query: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessKnowledgeRetrievalSuccess:
        """Retrieve contexts from chosen knowledge base

        Retrieve related documents from knowledge base by similarity.

        :param k: Maximum number of top-ranked knowledge-base entries to return in results.
        :param knowledge_ids: A List of knowledge-base IDs. For now, only one knowledge-base is supported.
        :param query: A text string used to find relevant information within the knowledge-base.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.serverless.knowledge.retrieve(
            k=k,
            knowledge_ids=knowledge_ids,
            query=query,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncKnowledge:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def retrieve(
        self,
        *,
        k: int,
        knowledge_ids: List[str],
        query: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ServerlessKnowledgeRetrievalSuccess:
        """Retrieve contexts from chosen knowledge base

        Retrieve related documents from knowledge base by similarity.

        :param k: Maximum number of top-ranked knowledge-base entries to return in results.
        :param knowledge_ids: A List of knowledge-base IDs. For now, only one knowledge-base is supported.
        :param query: A text string used to find relevant information within the knowledge-base.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.serverless.knowledge.retrieve(
            k=k,
            knowledge_ids=knowledge_ids,
            query=query,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
