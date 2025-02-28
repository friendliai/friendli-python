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
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.completions.complete(
        serverless_completions_body={
            "model": "meta-llama-3.1-8b-instruct",
            "prompt": "Say this is a test!",
            "stream": False,
        }
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `serverless_completions_body`                                                 | [models.ServerlessCompletionsBody](../../models/serverlesscompletionsbody.md) | :heavy_check_mark:                                                            | N/A                                                                           | {<br/>"model": "meta-llama-3.1-8b-instruct",<br/>"prompt": "Say this is a test!"<br/>} |
| `x_friendli_team`                                                             | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | ID of team to run requests as (optional parameter).                           |                                                                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.ServerlessCompletionsSuccess](../../models/serverlesscompletionssuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## stream

Generate text based on the given text prompt.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.completions.stream(
        serverless_completions_stream_body={
            "model": "meta-llama-3.1-8b-instruct",
            "prompt": "Say this is a test!",
            "stream": True,
        }
    )

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)
```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `serverless_completions_stream_body`                                                      | [models.ServerlessCompletionsStreamBody](../../models/serverlesscompletionsstreambody.md) | :heavy_check_mark:                                                                        | N/A                                                                                       | {<br/>"model": "meta-llama-3.1-8b-instruct",<br/>"prompt": "Say this is a test!"<br/>}    |
| `x_friendli_team`                                                                         | *OptionalNullable[str]*                                                                   | :heavy_minus_sign:                                                                        | ID of team to run requests as (optional parameter).                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[Union[eventstreaming.EventStream[models.ServerlessCompletionsStreamSuccess], eventstreaming.EventStreamAsync[models.ServerlessCompletionsStreamSuccess]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |