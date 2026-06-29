# Copyright (c) 2025-present, FriendliAI Corp. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Dict, Optional, Union

from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli.core.types import UNSET, OptionalNullable

from .config import Config

if TYPE_CHECKING:
    from friendli.core.httpclient import AsyncHttpClient, HttpClient
    from friendli.core.utils.logger import Logger
    from friendli.core.utils.retries import RetryConfig

    from .dataset import AsyncDataset, SyncDataset

# The dataset namespace is overridden with the hand-written subclass that adds the
# high-level, S3-backed sample-upload helpers on top of the generated CRUD methods.
_SYNC_DATASET = ("friendli.dataset.dataset", "SyncDataset")
_ASYNC_DATASET = ("friendli.dataset.dataset", "AsyncDataset")


class SyncFriendli(SyncFriendliCore):
    """Friendli Python SDK (synchronous).

    Subclasses the generated, sync/async-split core so that every namespace
    (`serverless`, `container`, `dedicated`, `file`, `cost`, `dataset`, ...) and
    every operation is inherited automatically. Only the `dataset` namespace and the
    `Config` (team header) are layered on top.
    """

    dataset: "SyncDataset"

    def __init__(
        self,
        token: Union[None, str, Callable[[], Optional[str]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
        config_cls: type[Config] = Config,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize the Friendli class."""
        super().__init__(
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
        self._sub_sdk_map = {**self._sub_sdk_map, "dataset": _SYNC_DATASET}

    @property
    def core(self) -> "SyncFriendli":
        """Return the underlying core SDK (this instance)."""
        return self

    @property
    def config(self) -> "Config":
        """Get the config instance."""
        return self._config


class AsyncFriendli(AsyncFriendliCore):
    """Friendli Python SDK (asynchronous).

    See `SyncFriendli`; this is its asynchronous counterpart.
    """

    dataset: "AsyncDataset"

    def __init__(
        self,
        token: Union[None, str, Callable[[], Optional[str]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
        config_cls: type[Config] = Config,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize the Friendli class."""
        super().__init__(
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
        self._sub_sdk_map = {**self._sub_sdk_map, "dataset": _ASYNC_DATASET}

    @property
    def core(self) -> "AsyncFriendli":
        """Return the underlying core SDK (this instance)."""
        return self

    @property
    def config(self) -> "Config":
        """Get the config instance."""
        return self._config
