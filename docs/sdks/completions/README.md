# Completions
(*serverless.completions*)

## Overview

### Available Operations

* [complete](#complete) - Completions
* [stream](#stream) - Stream completions

## complete

Generate text based on the given text prompt.

### Example Usage

```python
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.completions.complete(serverless_completions_complete_body={
    "prompt": "Say this is a test!",
    "model": "meta-llama-3.1-8b-instruct",
    "max_tokens": 200,
    "top_k": 1,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `serverless_completions_complete_body`                                                        | [models.ServerlessCompletionsCompleteBody](../../models/serverlesscompletionscompletebody.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `x_friendli_team`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | ID of team to run requests as (optional parameter).                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CompletionsResult](../../models/completionsresult.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## stream

Generate text based on the given text prompt.

### Example Usage

```python
from friendli import Friendli
import os

s = Friendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
)

res = s.serverless.completions.stream(serverless_completions_stream_body={
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

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `serverless_completions_stream_body`                                                      | [models.ServerlessCompletionsStreamBody](../../models/serverlesscompletionsstreambody.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `x_friendli_team`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | ID of team to run requests as (optional parameter).                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[Union[Generator[models.StreamedCompletionsResult, None, None], AsyncGenerator[models.StreamedCompletionsResult, None]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |