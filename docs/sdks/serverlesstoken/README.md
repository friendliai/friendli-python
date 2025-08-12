# ServerlessToken
(*serverless.token*)

## Overview

### Available Operations

* [tokenize](#tokenize) - Tokenization
* [detokenize](#detokenize) - Detokenization

## tokenize

By giving a text input, generate a tokenized output of token IDs.

### Example Usage

<!-- UsageSnippet language="python" operationID="serverlessTokenization" method="post" path="/serverless/v1/tokenize" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.token.tokenize(
        model="meta-llama-3.1-8b-instruct", prompt="What is generative AI?"
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                | Example                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                    | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models). | meta-llama-3.1-8b-instruct                                                                                                                 |
| `prompt`                                                                                                                                   | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | Input text prompt to tokenize.                                                                                                             | What is generative AI?                                                                                                                     |
| `x_friendli_team`                                                                                                                          | *OptionalNullable[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                         | ID of team to run requests as (optional parameter).                                                                                        |                                                                                                                                            |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |                                                                                                                                            |

### Response

**[models.ServerlessTokenizationSuccess](../../models/serverlesstokenizationsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## detokenize

By giving a list of tokens, generate a detokenized output text string.

### Example Usage

<!-- UsageSnippet language="python" operationID="serverlessDetokenization" method="post" path="/serverless/v1/detokenize" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.token.detokenize(
        model="meta-llama-3.1-8b-instruct",
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

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                | Example                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                    | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models). | meta-llama-3.1-8b-instruct                                                                                                                 |
| `tokens`                                                                                                                                   | List[*int*]                                                                                                                                | :heavy_check_mark:                                                                                                                         | A token sequence to detokenize.                                                                                                            | [<br/>128000,<br/>3923,<br/>374,<br/>1803,<br/>1413,<br/>15592,<br/>30<br/>]                                                               |
| `x_friendli_team`                                                                                                                          | *OptionalNullable[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                         | ID of team to run requests as (optional parameter).                                                                                        |                                                                                                                                            |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |                                                                                                                                            |

### Response

**[models.ServerlessDetokenizationSuccess](../../models/serverlessdetokenizationsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |