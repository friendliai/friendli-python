# Friendli Python SDK

<p align="center">
  <img width="10%" alt="Friendli Logo" src="https://friendli.ai/icon.svg">
</p>

<h2><p align="center">Supercharge Generative AI Serving with Friendli 🚀</p></h2>

## Token Setup

When using Friendli Python SDK, you need to provide a Friendli Token for authentication and authorization purposes. A Friendli Token serves as an alternative method of authorization to signing in with an email and a password. You can generate a new Friendli Token through the [Friendli Suite](https://friendli.ai/suite), at your "Personal settings" page by following the steps below.

1. Go to the [Friendli Suite](https://friendli.ai/suite) and sign in with your account.
2. Click the profile icon at the top-right corner of the page.
3. Click "Personal settings" menu.
4. Go to the "Tokens" tab on the navigation bar.
5. Create a new Friendli Token by clicking the "Create token" button.
6. Copy the token and save it in a safe place. You will not be able to see this token again once the page is refreshed.

<!-- No Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Friendli Python SDK](#friendli-python-sdk)
  * [Token Setup](#token-setup)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Server-sent event streaming](#server-sent-event-streaming)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [IDE Support](#ide-support)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add friendli
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install friendli
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add friendli
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from friendli python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "friendli",
# ]
# ///


from friendli import SyncFriendli

sdk = SyncFriendli(
    # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Chat completions

Given a list of messages forming a conversation, the model generates a response.

```python
# Synchronous Example

import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.chat.complete(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        max_tokens=200,
    )

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os

from friendli import AsyncFriendli


async def main():
    async with AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as friendli:
        res = await friendli.serverless.chat.complete(
            model="meta-llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Hello!",
                },
            ],
            max_tokens=200,
        )

        # Handle response
        print(res)


asyncio.run(main())
```

### Tool assisted chat completions

Given a list of messages forming a conversation, the model generates a response. Additionally, the model can utilize built-in tools for tool calls, enhancing its capability to provide more comprehensive and actionable responses.

```python
# Synchronous Example

import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.tool_assisted_chat.complete(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {
                "role": "user",
                "content": "What is 3 + 6?",
            },
        ],
        max_tokens=200,
        stream=False,
        tools=[
            {
                "type": "math:calculator",
            },
        ],
    )

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os

from friendli import AsyncFriendli


async def main():
    async with AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as friendli:
        res = await friendli.serverless.tool_assisted_chat.complete(
            model="meta-llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "What is 3 + 6?",
                },
            ],
            max_tokens=200,
            stream=False,
            tools=[
                {
                    "type": "math:calculator",
                },
            ],
        )

        # Handle response
        print(res)


asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name    | Type | Scheme      | Environment Variable |
| ------- | ---- | ----------- | -------------------- |
| `token` | http | HTTP Bearer | `FRIENDLI_TOKEN`     |

To authenticate with the API the `token` parameter must be set when initializing the SDK client instance. For example:
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.container.chat.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        model="(adapter-route)",
        max_tokens=200,
    )

    # Handle response
    print(res)
```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Container.Audio](docs/sdks/containeraudio/README.md)

* [transcribe](docs/sdks/containeraudio/README.md#transcribe) - Audio transcriptions

### [Container.Chat](docs/sdks/containerchat/README.md)

* [complete](docs/sdks/containerchat/README.md#complete) - Chat completions
* [stream](docs/sdks/containerchat/README.md#stream) - Stream chat completions

### [Container.Completions](docs/sdks/containercompletions/README.md)

* [complete](docs/sdks/containercompletions/README.md#complete) - Completions
* [stream](docs/sdks/containercompletions/README.md#stream) - Stream completions

### [Container.Image](docs/sdks/containerimage/README.md)

* [generate](docs/sdks/containerimage/README.md#generate) - Image generations
* [edit](docs/sdks/containerimage/README.md#edit) - Image edits

### [Container.Token](docs/sdks/containertoken/README.md)

* [tokenize](docs/sdks/containertoken/README.md#tokenize) - Tokenization
* [detokenize](docs/sdks/containertoken/README.md#detokenize) - Detokenization

### [Dataset](docs/sdks/dataset/README.md)

* [create_dataset](docs/sdks/dataset/README.md#create_dataset) - Create a new dataset
* [list_datasets](docs/sdks/dataset/README.md#list_datasets) - List datasets
* [get_dataset](docs/sdks/dataset/README.md#get_dataset) - Get dataset info
* [delete_dataset](docs/sdks/dataset/README.md#delete_dataset) - Delete dataset
* [create_version](docs/sdks/dataset/README.md#create_version) - Create a version
* [list_versions](docs/sdks/dataset/README.md#list_versions) - List versions
* [get_version](docs/sdks/dataset/README.md#get_version) - Get version info
* [delete_version](docs/sdks/dataset/README.md#delete_version) - Delete a version
* [create_split](docs/sdks/dataset/README.md#create_split) - Create a split
* [list_splits](docs/sdks/dataset/README.md#list_splits) - List splits
* [get_split](docs/sdks/dataset/README.md#get_split) - Get split info
* [delete_split](docs/sdks/dataset/README.md#delete_split) - Delete split
* [add_samples](docs/sdks/dataset/README.md#add_samples) - Add samples
* [list_samples](docs/sdks/dataset/README.md#list_samples) - List samples
* [update_samples](docs/sdks/dataset/README.md#update_samples) - Update samples
* [delete_samples](docs/sdks/dataset/README.md#delete_samples) - Delete samples

### [Dedicated.Audio](docs/sdks/dedicatedaudio/README.md)

* [transcribe](docs/sdks/dedicatedaudio/README.md#transcribe) - Audio transcriptions

### [Dedicated.Chat](docs/sdks/dedicatedchat/README.md)

* [complete](docs/sdks/dedicatedchat/README.md#complete) - Chat completions
* [stream](docs/sdks/dedicatedchat/README.md#stream) - Stream chat completions

### [Dedicated.ChatRender](docs/sdks/dedicatedchatrender/README.md)

* [render](docs/sdks/dedicatedchatrender/README.md#render) - Chat render

### [Dedicated.Completions](docs/sdks/dedicatedcompletions/README.md)

* [complete](docs/sdks/dedicatedcompletions/README.md#complete) - Completions
* [stream](docs/sdks/dedicatedcompletions/README.md#stream) - Stream completions

### [Dedicated.Embeddings](docs/sdks/embeddings/README.md)

* [embeddings](docs/sdks/embeddings/README.md#embeddings) - Embeddings

### [Dedicated.Endpoint](docs/sdks/endpoint/README.md)

* [wandb_artifact_create](docs/sdks/endpoint/README.md#wandb_artifact_create) - Create endpoint from W&B artifact
* [create](docs/sdks/endpoint/README.md#create) - Create a new endpoint
* [list](docs/sdks/endpoint/README.md#list) - List all endpoints
* [get_spec](docs/sdks/endpoint/README.md#get_spec) - Get endpoint specification
* [update](docs/sdks/endpoint/README.md#update) - Update endpoint spec
* [delete](docs/sdks/endpoint/README.md#delete) - Delete endpoint
* [get_version_history](docs/sdks/endpoint/README.md#get_version_history) - Get endpoint version history
* [get_status](docs/sdks/endpoint/README.md#get_status) - Get endpoint status
* [sleep](docs/sdks/endpoint/README.md#sleep) - Sleep endpoint
* [wake](docs/sdks/endpoint/README.md#wake) - Wake endpoint
* [terminate](docs/sdks/endpoint/README.md#terminate) - Terminate endpoint
* [restart](docs/sdks/endpoint/README.md#restart) - Restart endpoint

### [Dedicated.Image](docs/sdks/dedicatedimage/README.md)

* [generate](docs/sdks/dedicatedimage/README.md#generate) - Image generations
* [edit](docs/sdks/dedicatedimage/README.md#edit) - Image edits

### [Dedicated.Token](docs/sdks/dedicatedtoken/README.md)

* [tokenize](docs/sdks/dedicatedtoken/README.md#tokenize) - Tokenization
* [detokenize](docs/sdks/dedicatedtoken/README.md#detokenize) - Detokenization

### [File](docs/sdks/filesdk/README.md)

* [init_upload](docs/sdks/filesdk/README.md#init_upload) - Initiate file upload
* [complete_upload](docs/sdks/filesdk/README.md#complete_upload) - Complete file upload
* [get_info](docs/sdks/filesdk/README.md#get_info) - Get file info
* [get_download_url](docs/sdks/filesdk/README.md#get_download_url) - Get file download URL

### [Serverless.Chat](docs/sdks/serverlesschat/README.md)

* [complete](docs/sdks/serverlesschat/README.md#complete) - Chat completions
* [stream](docs/sdks/serverlesschat/README.md#stream) - Stream chat completions

### [Serverless.ChatRender](docs/sdks/serverlesschatrender/README.md)

* [render](docs/sdks/serverlesschatrender/README.md#render) - Chat render

### [Serverless.Completions](docs/sdks/serverlesscompletions/README.md)

* [complete](docs/sdks/serverlesscompletions/README.md#complete) - Completions
* [stream](docs/sdks/serverlesscompletions/README.md#stream) - Stream completions

### [Serverless.Knowledge](docs/sdks/knowledge/README.md)

* [retrieve](docs/sdks/knowledge/README.md#retrieve) - Retrieve contexts from chosen knowledge base

### [Serverless.Model](docs/sdks/model/README.md)

* [list](docs/sdks/model/README.md#list) - Retrieve serverless models

### [Serverless.Token](docs/sdks/serverlesstoken/README.md)

* [tokenize](docs/sdks/serverlesstoken/README.md#tokenize) - Tokenization
* [detokenize](docs/sdks/serverlesstoken/README.md#detokenize) - Detokenization

### [Serverless.ToolAssistedChat](docs/sdks/toolassistedchat/README.md)

* [complete](docs/sdks/toolassistedchat/README.md#complete) - Tool assisted chat completions
* [stream](docs/sdks/toolassistedchat/README.md#stream) - Stream tool assisted chat completions

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.chat.stream(
        model="(endpoint-id)",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        max_tokens=200,
    )

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)
```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.audio.transcribe(
        model="(endpoint-id)",
        file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    )

    # Handle response
    print(res)
```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os

from friendli import SyncFriendli
from friendli.utils import BackoffStrategy, RetryConfig

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.container.chat.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        model="(adapter-route)",
        max_tokens=200,
        retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    )

    # Handle response
    print(res)
```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os

from friendli import SyncFriendli
from friendli.utils import BackoffStrategy, RetryConfig

with SyncFriendli(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.container.chat.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        model="(adapter-route)",
        max_tokens=200,
    )

    # Handle response
    print(res)
```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`FriendliCoreError`](./src/friendli/models/friendlicoreerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import os

import friendli
from friendli import SyncFriendli, models

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = None
    try:
        res = friendli.dedicated.endpoint.delete(endpoint_id="<id>")

        # Handle response
        print(res)

    except models.FriendliCoreError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.HTTPValidationError):
            print(e.data.detail)  # Optional[List[friendli.ValidationError]]
```

### Error Classes
**Primary error:**
* [`FriendliCoreError`](./src/friendli/models/friendlicoreerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`FriendliCoreError`](./src/friendli/models/friendlicoreerror.py)**:
* [`HTTPValidationError`](./src/friendli/models/httpvalidationerror.py): Validation Error. Status code `422`. Applicable to 21 of 63 methods.*
* [`ResponseValidationError`](./src/friendli/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    server_url="https://api.friendli.ai",
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.container.chat.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        model="(adapter-route)",
        max_tokens=200,
    )

    # Handle response
    print(res)
```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.container.chat.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        model="(adapter-route)",
        max_tokens=200,
        server_url="http://localhost:8000",
    )

    # Handle response
    print(res)
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import httpx

from friendli import SyncFriendli

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SyncFriendli(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from typing import Any, Optional, Union

import httpx

from friendli import AsyncFriendli
from friendli.httpclient import AsyncHttpClient


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


s = AsyncFriendli(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

## Resource Management

The `SyncFriendli` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from friendli import SyncFriendli, AsyncFriendli
import os
def main():
    with SyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as friendli:
        # Rest of application here...


# Or when using async:
async def amain():
    async with AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as friendli:
        # Rest of application here...
```
<!-- No Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
import logging

from friendli import SyncFriendli

logging.basicConfig(level=logging.DEBUG)
s = SyncFriendli(debug_logger=logging.getLogger("friendli"))
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
