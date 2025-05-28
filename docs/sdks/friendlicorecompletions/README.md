# FriendliCoreCompletions
(*dedicated.completions*)

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
    res = friendli.dedicated.completions.complete(
        dedicated_completions_body={
            "model": "(endpoint-id)",
            "prompt": "Say this is a test!",
            "stream": False,
        }
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `dedicated_completions_body`                                                | [models.DedicatedCompletionsBody](../../models/dedicatedcompletionsbody.md) | :heavy_check_mark:                                                          | N/A                                                                         | {<br/>"model": "(endpoint-id)",<br/>"prompt": "Say this is a test!"<br/>}   |
| `x_friendli_team`                                                           | *OptionalNullable[str]*                                                     | :heavy_minus_sign:                                                          | ID of team to run requests as (optional parameter).                         |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

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
    res = friendli.dedicated.completions.stream(
        dedicated_completions_stream_body={
            "model": "(endpoint-id)",
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

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `dedicated_completions_stream_body`                                                     | [models.DedicatedCompletionsStreamBody](../../models/dedicatedcompletionsstreambody.md) | :heavy_check_mark:                                                                      | N/A                                                                                     | {<br/>"model": "(endpoint-id)",<br/>"prompt": "Say this is a test!"<br/>}               |
| `x_friendli_team`                                                                       | *OptionalNullable[str]*                                                                 | :heavy_minus_sign:                                                                      | ID of team to run requests as (optional parameter).                                     |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[Union[eventstreaming.EventStream[models.ServerlessCompletionsStreamSuccess], eventstreaming.EventStreamAsync[models.ServerlessCompletionsStreamSuccess]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |