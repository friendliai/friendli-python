# Friendli Python SDK

<p align="center">
  <img width="10%" alt="Friendli Logo" src="https://friendli.ai/icon.svg">
</p>

<h2><p align="center">Supercharge Generative AI Serving with Friendli 🚀</p></h2>

## Token Setup

When using Friendli Python SDK, you need to provide a Friendli Token for authentication and authorization purposes. A Friendli Token serves as an alternative method of authorization to signing in with an email and a password. You can generate a new Friendli Token through the [Friendli Suite](https://suite.friendli.ai), at your "User settings" page by following the steps below.

1. Go to the [Friendli Suite](https://suite.friendli.ai) and sign in with your account.
2. Click the profile icon at the top-right corner of the page.
3. Click "User settings" menu.
4. Go to the "Tokens" tab on the navigation bar.
5. Create a new Friendli Token by clicking the "Create token" button.
6. Copy the token and save it in a safe place. You will not be able to see this token again once the page is refreshed.

<!-- No Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Server-sent event streaming](#server-sent-event-streaming)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/friendliai/friendli-python-internal.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/friendliai/friendli-python-internal.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Chat completion

Given a list of messages forming a conversation, the model generates a response.

```python
# Synchronous Example
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200)

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from friendli import Friendli
import os

async def main():
    s = Friendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    )
    res = await s.inference.chat_completion_async(model="meta-llama-3.1-8b-instruct", messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Hello!",
        },
    ], max_tokens=200)
    if res is not None:
        for event in res:
            # handle event
            print(event, flush=True)

asyncio.run(main())
```

### Tool assisted chat completion

Given a list of messages forming a conversation, the model generates a response. Additionally, the model can utilize built-in tools for tool calls, enhancing its capability to provide more comprehensive and actionable responses.

```python
# Synchronous Example
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.tool_assisted_chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200, tools=[
    {
        "type": "math:calculator",
    },
    {
        "type": "web:url",
    },
])

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from friendli import Friendli
import os

async def main():
    s = Friendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    )
    res = await s.serverless.tool_assisted_chat_completion_async(model="meta-llama-3.1-8b-instruct", messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Hello!",
        },
    ], max_tokens=200, tools=[
        {
            "type": "math:calculator",
        },
        {
            "type": "math:calculator",
        },
    ])
    if res is not None:
        for event in res:
            # handle event
            print(event, flush=True)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [inference](docs/sdks/inference/README.md)

* [chat_completion](docs/sdks/inference/README.md#chat_completion) - Chat completion
* [completion](docs/sdks/inference/README.md#completion) - Completion
* [tokenization](docs/sdks/inference/README.md#tokenization) - Tokenization
* [detokenization](docs/sdks/inference/README.md#detokenization) - Detokenization

### [serverless](docs/sdks/serverless/README.md)

* [tool_assisted_chat_completion](docs/sdks/serverless/README.md#tool_assisted_chat_completion) - Tool assisted chat completion

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.

```python
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200)

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://wiki.python.org/moin/Generators
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from friendli import Friendli
from friendli.utils import BackoffStrategy, RetryConfig
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from friendli import Friendli
from friendli.utils import BackoffStrategy, RetryConfig
import os

s = Friendli(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200)

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `chat_completion_async` method may raise the following exceptions:

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

### Example

```python
from friendli import Friendli, models
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = None
try:
    res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Hello!",
        },
    ], max_tokens=200)

    if res is not None:
        for event in res:
            # handle event
            print(event, flush=True)

except models.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `serverless` | `https://inference.friendli.ai` | None |
| `dedicated` | `https://inference.friendli.ai/dedicated` | None |

#### Example

```python
from friendli import Friendli
import os

s = Friendli(
    server="dedicated",
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200)

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from friendli import Friendli
import os

s = Friendli(
    server_url="https://inference.friendli.ai",
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200)

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.tool_assisted_chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200, tools=[
    {
        "type": "math:calculator",
    },
    {
        "type": "web:url",
    },
], server_url="https://inference.friendli.ai")

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from friendli import Friendli
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Friendli(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from friendli import Friendli
from friendli.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

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
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

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
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Friendli(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                 | Type                 | Scheme               | Environment Variable |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `token`              | http                 | HTTP Bearer          | `FRIENDLI_TOKEN`     |

To authenticate with the API the `token` parameter must be set when initializing the SDK client instance. For example:
```python
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.inference.chat_completion(model="meta-llama-3.1-8b-instruct", messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
], max_tokens=200)

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from friendli import Friendli
import logging

logging.basicConfig(level=logging.DEBUG)
s = Friendli(debug_logger=logging.getLogger("friendli"))
```

You can also enable a default debug logger by setting an environment variable `FRIENDLI_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
