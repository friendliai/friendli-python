from .sdk import Friendli
from .httpclient import AsyncHttpClient, HttpClient
from .errorhttpxclients import ErrorThrowingSyncClient, ErrorThrowingAsyncClient
from .utils.logger import Logger
from .utils.retries import RetryConfig
from friendli.types import OptionalNullable, UNSET
import httpx
from typing import Callable, Dict, Optional, Type, Union
from types import TracebackType


class SyncFriendli(Friendli):
    def __init__(
        self,
        token: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        super().__init__(
            token=token,
            server_idx=server_idx,
            server_url=server_url,
            url_params=url_params,
            client=client or httpx.Client(),
            async_client=ErrorThrowingAsyncClient(),
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger,
        )

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: Union[Type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None]
    ) -> None:
        self.sdk_configuration.client.__exit__(exc_type, exc_val, exc_tb)


class AsyncFriendli(Friendli):
    def __init__(
        self,
        token: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        super().__init__(
            token=token,
            server_idx=server_idx,
            server_url=server_url,
            url_params=url_params,
            client=ErrorThrowingSyncClient(),
            async_client=async_client or httpx.AsyncClient(),
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Union[Type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None]
    ) -> None:
        await self.sdk_configuration.async_client.__aexit__(exc_type, exc_val, exc_tb)
