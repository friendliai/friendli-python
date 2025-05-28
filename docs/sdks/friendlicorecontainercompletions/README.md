# FriendliCoreContainerCompletions
(*container.completions*)

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
    res = friendli.container.completions.complete(
        request={
            "prompt": "Say this is a test!",
            "stream": False,
        }
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.ContainerCompletionsBody](../../models/containercompletionsbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |
| `server_url`                                                                | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | An optional server URL to use.                                              |

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
    res = friendli.container.completions.stream(
        request={
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

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.ContainerCompletionsStreamBody](../../models/containercompletionsstreambody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |
| `server_url`                                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | An optional server URL to use.                                                          |

### Response

**[Union[eventstreaming.EventStream[models.ServerlessCompletionsStreamSuccess], eventstreaming.EventStreamAsync[models.ServerlessCompletionsStreamSuccess]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |