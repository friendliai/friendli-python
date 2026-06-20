# Container.Classification

## Overview

### Available Operations

* [classify](#classify) - Text classification

## classify

Given a text input, the model classifies it into categories.

### Example Usage

<!-- UsageSnippet language="python" operationID="containerTextClassification" method="post" path="/classify" example="Example" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.container.classification.classify(
        model="(adapter-route)", input_="I love programming."
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                         | Routes the request to a specific adapter.                                                                                                                                                  | (adapter-route)                                                                                                                                                                            |
| `input`                                                                                                                                                                                    | [OptionalNullable[models.ContainerTextClassificationBodyInput]](../../models/containertextclassificationbodyinput.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                         | Input text to classify, encoded as a string or array of strings. To classify multiple inputs in a single request, pass an array of strings.<br/><br/>Either `input` or `tokens` field is required. | I love programming.                                                                                                                                                                        |
| `tokens`                                                                                                                                                                                   | List[*int*]                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                         | The tokenized prompt (i.e., input tokens).<br/><br/>Either `input` or `tokens` field is required.                                                                                          |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |
| `server_url`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | An optional server URL to use.                                                                                                                                                             | http://localhost:8080                                                                                                                                                                      |

### Response

**[models.ContainerTextClassificationSuccess](../../models/containertextclassificationsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |