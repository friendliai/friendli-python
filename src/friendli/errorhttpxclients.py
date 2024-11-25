import httpx
from .httpclient import AsyncHttpClient, HttpClient
from typing import Any, NoReturn, Optional, Union, Type, TypeVar
from types import TracebackType

T = TypeVar("T", bound="ErrorThrowingSyncClient")
U = TypeVar("U", bound="ErrorThrowingAsyncClient")


class MethodUsedInWrongPlaceError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ErrorThrowingSyncClient(HttpClient):
    def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        self._raise_error()

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        self._raise_error()

    def __enter__(self: T) -> T:
        return self

    def __exit__(
        self,
        exc_type: Union[Type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None]
    ) -> None:
        pass

    def _raise_error(self) -> NoReturn:
        raise MethodUsedInWrongPlaceError("Sync operations are not supported in AsyncFriendli.")


class ErrorThrowingAsyncClient(AsyncHttpClient):
    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        self._raise_error()

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        self._raise_error()

    async def __aenter__(self: U) -> U:
        return self

    async def __aexit__(
        self,
        exc_type: Union[Type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None]
    ) -> None:
        pass


    def _raise_error(self) -> NoReturn:
        raise MethodUsedInWrongPlaceError("Async operations are not supported in SyncFriendli.")
