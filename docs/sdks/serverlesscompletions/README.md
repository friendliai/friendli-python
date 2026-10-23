# Serverless.Completions

## Overview

### Available Operations

* [complete](#complete) - Completions

## complete

Generate a text completion from a prompt or token sequence. Supports streaming and configurable generation parameters.

### Example Usage

<!-- UsageSnippet language="python" operationID="serverlessCompletionsComplete" method="post" path="/serverless/v1/completions" example="Example" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.completions.complete(
        serverless_completions_body={
            "model": "meta-llama-3.1-8b-instruct",
            "stream": True,
            "prompt": "Say this is a test!",
        }
    )

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)
```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `serverless_completions_body`                                                 | [models.ServerlessCompletionsBody](../../models/serverlesscompletionsbody.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `x_friendli_team`                                                             | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | ID of team to run requests as (optional parameter).                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ServerlessCompletionsCompleteResponse](../../models/serverlesscompletionscompleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |