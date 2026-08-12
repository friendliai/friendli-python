# Serverless.Model

## Overview

### Available Operations

* [models](#models) - List Models

## models

Lists the currently available models, and provides basic information about each one such as pricing and functionality.

### Example Usage

<!-- UsageSnippet language="python" operationID="serverlessModels" method="get" path="/serverless/v1/models" example="Example" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.model.models()

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServerlessModelListSuccess](../../models/serverlessmodellistsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |