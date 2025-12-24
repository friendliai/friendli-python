# Dedicated.Embeddings

## Overview

### Available Operations

* [embeddings](#embeddings) - Embeddings

## embeddings

Creates an embedding vector representing the input text.

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedEmbeddings" method="post" path="/dedicated/v1/embeddings" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.embeddings.embeddings(
        model="(endpoint-id)",
        input_="The food was delicious and the waiter...",
        encoding_format="float",
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                                                                           | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         | Example                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                                                                                             | *str*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | ID of target endpoint. If you want to send request to specific adapter, use the format "YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE". Otherwise, you can just use "YOUR_ENDPOINT_ID" alone. | (endpoint-id)                                                                                                                                                                       |
| `input`                                                                                                                                                                             | [models.Input](../../models/input.md)                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays.                       | The food was delicious and the waiter...                                                                                                                                            |
| `x_friendli_team`                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                  | ID of team to run requests as (optional parameter).                                                                                                                                 |                                                                                                                                                                                     |
| `encoding_format`                                                                                                                                                                   | [OptionalNullable[models.EncodingFormat]](../../models/encodingformat.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                  | The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).                                                                    |                                                                                                                                                                                     |
| `retries`                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                 |                                                                                                                                                                                     |

### Response

**[models.DedicatedEmbeddingsSuccess](../../models/dedicatedembeddingssuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |