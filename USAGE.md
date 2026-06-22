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
        model="zai-org/GLM-5.2",
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
            model="zai-org/GLM-5.2",
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
        )

        # Handle response
        print(res)


asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->