<!-- Start SDK Example Usage [usage] -->
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
        messages=[
            {
                "content": "You are a helpful assistant.",
                "role": "system",
            },
            {
                "content": "Hello!",
                "role": "user",
            },
        ],
        model="meta-llama-3.1-8b-instruct",
        max_tokens=200,
        stream=False,
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
            messages=[
                {
                    "content": "You are a helpful assistant.",
                    "role": "system",
                },
                {
                    "content": "Hello!",
                    "role": "user",
                },
            ],
            model="meta-llama-3.1-8b-instruct",
            max_tokens=200,
            stream=False,
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
        messages=[
            {
                "content": "What is 3 + 6?",
                "role": "user",
            },
        ],
        model="meta-llama-3.1-8b-instruct",
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
            messages=[
                {
                    "content": "What is 3 + 6?",
                    "role": "user",
                },
            ],
            model="meta-llama-3.1-8b-instruct",
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