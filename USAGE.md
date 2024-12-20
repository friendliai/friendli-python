<!-- Start SDK Example Usage [usage] -->
### Chat completions

Given a list of messages forming a conversation, the model generates a response.

```python
# Synchronous Example
from friendli import SyncFriendli
import os

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

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from friendli import AsyncFriendli
import os


async def main():
    async with AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as friendli:

        res = await friendli.serverless.chat.complete_async(
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
from friendli import SyncFriendli
import os

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

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from friendli import AsyncFriendli
import os


async def main():
    async with AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as friendli:

        res = await friendli.serverless.tool_assisted_chat.complete_async(
            model="meta-llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "What is 3 + 6?",
                },
            ],
            max_tokens=200,
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