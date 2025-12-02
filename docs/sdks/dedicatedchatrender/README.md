# DedicatedChatRender
(*dedicated.chat_render*)

## Overview

### Available Operations

* [render](#render) - Chat render

## render

Given a list of messages forming a conversation, the API renders them into the final prompt text that will be sent to the model.

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedChatRender" method="post" path="/dedicated/v1/chat/render" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.chat_render.render(
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
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    | Example                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | ID of target endpoint. If you want to send request to specific adapter, use the format "YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE". Otherwise, you can just use "YOUR_ENDPOINT_ID" alone.                            | (endpoint-id)                                                                                                                                                                                                  |
| `messages`                                                                                                                                                                                                     | List[[models.Message](../../models/message.md)]                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                             | A list of messages comprising the conversation so far.                                                                                                                                                         | [<br/>{<br/>"content": "You are a helpful assistant.",<br/>"role": "system"<br/>},<br/>{<br/>"content": "Hello!",<br/>"role": "user"<br/>}<br/>]                                                               |
| `x_friendli_team`                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                             | ID of team to run requests as (optional parameter).                                                                                                                                                            |                                                                                                                                                                                                                |
| `chat_template_kwargs`                                                                                                                                                                                         | Dict[str, *Any*]                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Additional keyword arguments supplied to the template renderer. These parameters will be available for use within the chat template.                                                                           |                                                                                                                                                                                                                |
| `tools`                                                                                                                                                                                                        | List[[models.Tool](../../models/tool.md)]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                             | A list of tools the model may call.<br/>Use this to provide a list of functions the model may generate JSON inputs for.<br/><br/>**When `tools` is specified, `min_tokens` and `response_format` fields are unsupported.** |                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                            |                                                                                                                                                                                                                |

### Response

**[models.DedicatedChatRenderSuccess](../../models/dedicatedchatrendersuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |