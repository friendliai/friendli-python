<!-- Start SDK Example Usage [usage] -->
### Chat completions

Given a list of messages forming a conversation, the model generates a response.

```python
# Synchronous Example
from friendli import SyncFriendli
import os

s = SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.chat.complete(
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
    s = AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    )
    res = await s.serverless.chat.complete_async(
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
    print(res)

asyncio.run(main())
```

### Tool assisted chat completions

Given a list of messages forming a conversation, the model generates a response. Additionally, the model can utilize built-in tools for tool calls, enhancing its capability to provide more comprehensive and actionable responses.

```python
# Synchronous Example
from friendli import SyncFriendli
import os

s = SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.tool_assisted_chat.complete(
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
    s = AsyncFriendli(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    )
    res = await s.serverless.tool_assisted_chat.complete_async(
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
    print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->