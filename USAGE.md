<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import friendli
from friendli import Friendli
import os

s = Friendli(
    bearer_auth=os.getenv("FRIENDLI_BEARER_AUTH", ""),
)

res = s.inference.chat_completion(chat_completion_request_body={
    "model": "meta-llama-3.1-8b-instruct",
    "messages": [
        {
            "role": friendli.Role.SYSTEM,
            "content": "You are a helpful assistant.",
        },
        {
            "role": friendli.UserMessageRole.USER,
            "content": "Hello!",
        },
    ],
    "max_tokens": 200,
})

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
import friendli
from friendli import Friendli
import os

async def main():
    s = Friendli(
        bearer_auth=os.getenv("FRIENDLI_BEARER_AUTH", ""),
    )
    res = await s.inference.chat_completion_async(chat_completion_request_body={
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [
            {
                "role": friendli.Role.SYSTEM,
                "content": "You are a helpful assistant.",
            },
            {
                "role": friendli.UserMessageRole.USER,
                "content": "Hello!",
            },
        ],
        "max_tokens": 200,
    })
    if res is not None:
        for event in res:
            # handle event
            print(event, flush=True)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->