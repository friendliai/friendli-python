# FriendliToken
(*dedicated.token*)

## Overview

### Available Operations

* [tokenization](#tokenization) - Tokenization
* [detokenization](#detokenization) - Detokenization

## tokenization

By giving a text input, generate a tokenized output of token IDs.

### Example Usage

```python
from friendli import SyncFriendli
import os

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:

    res = friendli.dedicated.token.tokenization(
        model="(endpoint-id):(adapter-route)", prompt="What is generative AI?"
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                           | *str*                                                                                                             | :heavy_check_mark:                                                                                                | ID of target endpoint. If you want to send request to specific adapter, using "ENDPOINT_ID:ADAPTER_ROUTE" format. | (endpoint-id):(adapter-route)                                                                                     |
| `prompt`                                                                                                          | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Input text prompt to tokenize.                                                                                    | What is generative AI?                                                                                            |
| `x_friendli_team`                                                                                                 | *OptionalNullable[str]*                                                                                           | :heavy_minus_sign:                                                                                                | ID of team to run requests as (optional parameter).                                                               |                                                                                                                   |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.DedicatedTokenizationSuccess](../../models/dedicatedtokenizationsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## detokenization

By giving a list of tokens, generate a detokenized output text string.

### Example Usage

```python
from friendli import SyncFriendli
import os

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:

    res = friendli.dedicated.token.detokenization(
        model="(endpoint-id):(adapter-route)",
        tokens=[
            128000,
            3923,
            374,
            1803,
            1413,
            15592,
            30,
        ],
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                           | *str*                                                                                                             | :heavy_check_mark:                                                                                                | ID of target endpoint. If you want to send request to specific adapter, using "ENDPOINT_ID:ADAPTER_ROUTE" format. | (endpoint-id):(adapter-route)                                                                                     |
| `tokens`                                                                                                          | List[*int*]                                                                                                       | :heavy_check_mark:                                                                                                | A token sequence to detokenize.                                                                                   | [<br/>128000,<br/>3923,<br/>374,<br/>1803,<br/>1413,<br/>15592,<br/>30<br/>]                                      |
| `x_friendli_team`                                                                                                 | *OptionalNullable[str]*                                                                                           | :heavy_minus_sign:                                                                                                | ID of team to run requests as (optional parameter).                                                               |                                                                                                                   |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.DedicatedDetokenizationSuccess](../../models/dedicateddetokenizationsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |