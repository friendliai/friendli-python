# Image
(*dedicated.image*)

## Overview

### Available Operations

* [generate](#generate) - Image generations

## generate

Given a description, the model generates image(s).

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.image.generate(prompt="<value>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `prompt`                                                                                                                          | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | A text description of the desired image(s).                                                                                       |
| `x_friendli_team`                                                                                                                 | *OptionalNullable[str]*                                                                                                           | :heavy_minus_sign:                                                                                                                | ID of team to run requests as (optional parameter).                                                                               |
| `num_inference_steps`                                                                                                             | *OptionalNullable[int]*                                                                                                           | :heavy_minus_sign:                                                                                                                | The number of inference steps to use during image generation. Supported range: [1, 10]. Defaults to 4.                            |
| `response_format`                                                                                                                 | [OptionalNullable[models.DedicatedImageGenerationBodyResponseFormat]](../../models/dedicatedimagegenerationbodyresponseformat.md) | :heavy_minus_sign:                                                                                                                | The format in which the generated image(s) will be returned. One of `url(default)`, `raw`, `png`, `jpeg`, and `jpg`.              |
| `seed`                                                                                                                            | *OptionalNullable[int]*                                                                                                           | :heavy_minus_sign:                                                                                                                | The seed to use for image generation.                                                                                             |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.DedicatedImageGenerateSuccess](../../models/dedicatedimagegeneratesuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |