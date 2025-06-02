# File
(*file*)

## Overview

### Available Operations

* [init_upload](#init_upload) - Initiate file upload
* [complete_upload](#complete_upload) - Complete file upload
* [get_info](#get_info) - Get file info
* [get_download_url](#get_download_url) - Get file download URL

## init_upload

Initiate file upload.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.file.init_upload(
        digest="<value>", name="<value>", project_id="<id>", size=830650
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `digest`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Digest of the file.                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Name of the file.                                                   |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the project the file belongs to.                              |
| `size`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Size of the file in bytes.                                          |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileInitUploadResponse](../../models/fileinituploadresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## complete_upload

Complete file upload.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.file.complete_upload(file_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | File ID                                                             |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_info

Get file info.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.file.get_info(file_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | File ID                                                             |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileInfo](../../models/fileinfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_download_url

Get file download URL.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.file.get_download_url(file_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | File ID                                                             |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileGetDownloadURLResponse](../../models/filegetdownloadurlresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |