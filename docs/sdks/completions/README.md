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
from friendli import SyncFriendli
import os

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:

    res = friendli.serverless.completions.complete(
        serverless_completions_complete_body={
            "prompt": "Say this is a test!",
            "model": "meta-llama-3.1-8b-instruct",
            "max_tokens": 200,
            "top_k": 1,
        }
    )

    # Handle response
    print(res)
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
from friendli import SyncFriendli
import os

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:

    res = friendli.serverless.completions.stream(
        serverless_completions_stream_body={
            "prompt": "Say this is a test!",
            "model": "meta-llama-3.1-8b-instruct",
            "max_tokens": 200,
            "top_k": 1,
        }
    )

    with res as event_stream:
        for event in event_stream:
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

**[Union[eventstreaming.EventStream[models.StreamedCompletionsResult], eventstreaming.EventStreamAsync[models.StreamedCompletionsResult]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |