<!-- Start SDK Example Usage [usage] -->
### Chat completions

Generate a model response from a list of messages comprising a conversation. Compatible with the OpenAI Chat Completions API, with support for streaming, tool calls, and structured outputs.

```python
# Synchronous Example
from friendli_core import FriendliCore
import os


with FriendliCore(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as fc_client:

    res = fc_client.serverless.chat.complete(model="zai-org/GLM-5.3", messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Hello!",
        },
    ])

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from friendli_core import FriendliCore
import os

async def main():

    async with FriendliCore(
        token=os.getenv("FRIENDLI_TOKEN", ""),
    ) as fc_client:

        res = await fc_client.serverless.chat.complete_async(model="zai-org/GLM-5.3", messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ])

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->