<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->