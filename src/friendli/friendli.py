# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Callable, Dict, Optional, Union

from friendli_core.httpclient import AsyncHttpClient, HttpClient
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable
from friendli_core.utils.logger import Logger
from friendli_core.utils.retries import RetryConfig

from .config import Config
from .container import AsyncContainer, SyncContainer
from .dataset import AsyncDataset, SyncDataset
from .dedicated import AsyncDedicated, SyncDedicated
from .file import AsyncFile, SyncFile
from .serverless import AsyncServerless, SyncServerless


class SyncFriendli:
    def __init__(
        self,
        token: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
        core_cls: type[SyncFriendliCore] = SyncFriendliCore,
        config_cls: type[Config] = Config,
        *args,
        **kwargs,
    ):
        self._core = core_cls(
            token=token,
            server_idx=server_idx,
            server_url=server_url,
            url_params=url_params,
            client=client,
            async_client=async_client,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger,
        )
        self._config = config_cls(*args, **kwargs)

        self.container = SyncContainer(core=self._core, config=self._config)
        self.dataset = SyncDataset(core=self._core, config=self._config)
        self.dedicated = SyncDedicated(core=self._core, config=self._config)
        self.file = SyncFile(core=self._core, config=self._config)
        self.serverless = SyncServerless(core=self._core, config=self._config)

    @property
    def core(self) -> SyncFriendliCore:
        return self._core

    @property
    def config(self) -> Config:
        return self._config

    def __enter__(self):
        self._core.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._core.__exit__(exc_type, exc_val, exc_tb)


class AsyncFriendli:
    def __init__(
        self,
        token: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
        core_cls: type[AsyncFriendliCore] = AsyncFriendliCore,
        config_cls: type[Config] = Config,
        *args,
        **kwargs,
    ):
        self._core = core_cls(
            token=token,
            server_idx=server_idx,
            server_url=server_url,
            url_params=url_params,
            client=client,
            async_client=async_client,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger,
        )
        self._config = config_cls(*args, **kwargs)

        self.container = AsyncContainer(core=self._core, config=self._config)
        self.dataset = AsyncDataset(core=self._core, config=self._config)
        self.dedicated = AsyncDedicated(core=self._core, config=self._config)
        self.file = AsyncFile(core=self._core, config=self._config)
        self.serverless = AsyncServerless(core=self._core, config=self._config)

    @property
    def core(self) -> AsyncFriendliCore:
        return self._core

    @property
    def config(self) -> Config:
        return self._config

    async def __aenter__(self):
        await self._core.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._core.__aexit__(exc_type, exc_val, exc_tb)
