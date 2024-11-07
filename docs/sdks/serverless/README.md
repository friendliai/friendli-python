# Serverless
(*serverless*)

## Overview

### Available Operations

* [tool_assisted_chat_completion](#tool_assisted_chat_completion) - Tool assisted chat completion

## tool_assisted_chat_completion

Given a list of messages forming a conversation, the model generates a response. Additionally, the model can utilize built-in tools for tool calls, enhancing its capability to provide more comprehensive and actionable responses.

### Example Usage

```python
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.tool_assisted_chat_completion(tool_assisted_completion_request_body={
    "model": "meta-llama-3.1-8b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Hello!",
        },
    ],
    "max_tokens": 200,
    "tools": [
        {
            "type": "math:calculator",
        },
        {
            "type": "web:url",
        },
    ],
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `x_friendli_team`                                                                                       | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | ID of team to run requests as (optional parameter).                                                     |
| `tool_assisted_completion_request_body`                                                                 | [Optional[models.ToolAssistedCompletionRequestBody]](../../models/toolassistedcompletionrequestbody.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |
| `server_url`                                                                                            | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | An optional server URL to use.                                                                          |

### Response

**[models.ToolAssistedChatCompletionResponse](../../models/toolassistedchatcompletionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |