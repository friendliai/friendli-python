# Dedicated.Classification

## Overview

### Available Operations

* [classify](#classify) - Text classification

## classify

Given a text input, the model classifies it into categories.

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedTextClassification" method="post" path="/dedicated/classify" example="Example" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.classification.classify(
        model="(endpoint-id)", input_="I love programming."
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                                                                    | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | ID of target endpoint. If you want to send request to specific adapter, use the format "YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE". Otherwise, you can just use "YOUR_ENDPOINT_ID" alone.        | (endpoint-id)                                                                                                                                                                              |
| `x_friendli_team`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                         | ID of team to run requests as (optional parameter).                                                                                                                                        |                                                                                                                                                                                            |
| `input`                                                                                                                                                                                    | [OptionalNullable[models.DedicatedTextClassificationBodyInput]](../../models/dedicatedtextclassificationbodyinput.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                         | Input text to classify, encoded as a string or array of strings. To classify multiple inputs in a single request, pass an array of strings.<br/><br/>Either `input` or `tokens` field is required. | I love programming.                                                                                                                                                                        |
| `tokens`                                                                                                                                                                                   | List[*int*]                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                         | The tokenized prompt (i.e., input tokens).<br/><br/>Either `input` or `tokens` field is required.                                                                                          |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[models.ContainerTextClassificationSuccess](../../models/containertextclassificationsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |