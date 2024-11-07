# Inference
(*inference*)

## Overview

### Available Operations

* [chat_completion](#chat_completion) - Chat completion
* [completion](#completion) - Completion
* [tokenization](#tokenization) - Tokenization
* [detokenization](#detokenization) - Detokenization

## chat_completion

Given a list of messages forming a conversation, the model generates a response.

### Example Usage

```python
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

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `x_friendli_team`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | ID of team to run requests as (optional parameter).                                     |
| `chat_completion_request_body`                                                          | [Optional[models.ChatCompletionRequestBody]](../../models/chatcompletionrequestbody.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ChatCompletionResponse1](../../models/chatcompletionresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## completion

Generate text based on the given text prompt.

### Example Usage

```python
from friendli import Friendli
import os

s = Friendli(
    bearer_auth=os.getenv("FRIENDLI_BEARER_AUTH", ""),
)

res = s.inference.completion(completion_request_body={
    "prompt": "Say this is a test!",
    "model": "meta-llama-3.1-8b-instruct",
    "max_tokens": 200,
    "top_k": 1,
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `x_friendli_team`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | ID of team to run requests as (optional parameter).                             |
| `completion_request_body`                                                       | [Optional[models.CompletionRequestBody]](../../models/completionrequestbody.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CompletionResponse1](../../models/completionresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## tokenization

By giving a text input, generate a tokenized output of token IDs.

### Example Usage

```python
from friendli import Friendli
import os

s = Friendli(
    bearer_auth=os.getenv("FRIENDLI_BEARER_AUTH", ""),
)

res = s.inference.tokenization(tokenization_request_body={
    "model": "meta-llama-3.1-8b-instruct",
    "prompt": "What is generative AI?",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `x_friendli_team`                                                                   | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | ID of team to run requests as (optional parameter).                                 |
| `tokenization_request_body`                                                         | [Optional[models.TokenizationRequestBody]](../../models/tokenizationrequestbody.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.TokenizationResponse](../../models/tokenizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## detokenization

By giving a list of tokens, generate a detokenized output text string.

### Example Usage

```python
from friendli import Friendli
import os

s = Friendli(
    bearer_auth=os.getenv("FRIENDLI_BEARER_AUTH", ""),
)

res = s.inference.detokenization(detokenization_request_body={
    "model": "meta-llama-3.1-8b-instruct",
    "tokens": [
        128000,
        3923,
        374,
        1803,
        1413,
        15592,
        30,
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `x_friendli_team`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | ID of team to run requests as (optional parameter).                                     |
| `detokenization_request_body`                                                           | [Optional[models.DetokenizationRequestBody]](../../models/detokenizationrequestbody.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.DetokenizationResponse](../../models/detokenizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |