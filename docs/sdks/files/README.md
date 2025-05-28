# Files
(*platform.files*)

## Overview

### Available Operations

* [upload](#upload) - Files upload
* [list](#list) - Files list
* [retrieve](#retrieve) - File retrieve
* [delete](#delete) - Files delete
* [download](#download) - Files download

## upload

Uploads a file.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.platform.files.upload(
        file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
        purpose="batch",
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `file`                                                                | [models.File](../../models/file.md)                                   | :heavy_check_mark:                                                    | The File object (not file name) to be uploaded.                       |
| `purpose`                                                             | [models.Purpose](../../models/purpose.md)                             | :heavy_check_mark:                                                    | The intended purpose of the uploaded file. One of `batch` or `model`. |
| `x_friendli_team`                                                     | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | ID of team to run requests as (optional parameter).                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PlatformFilesUploadResult](../../models/platformfilesuploadresult.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list

List files.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.platform.files.list()

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `x_friendli_team`                                                                                        | *OptionalNullable[str]*                                                                                  | :heavy_minus_sign:                                                                                       | ID of team to run requests as (optional parameter).                                                      |
| `after`                                                                                                  | *OptionalNullable[str]*                                                                                  | :heavy_minus_sign:                                                                                       | File ID after which to fetch the next page of results. Optional.                                         |
| `limit`                                                                                                  | *OptionalNullable[int]*                                                                                  | :heavy_minus_sign:                                                                                       | Maximum number of files to return, between [1, 10,000]. Defaults to 10,000.                              |
| `order`                                                                                                  | [OptionalNullable[models.Order]](../../models/order.md)                                                  | :heavy_minus_sign:                                                                                       | Sort order by `created` timestamp. Use `asc` for ascending or `desc` for descending. Defaults to `desc`. |
| `purpose`                                                                                                | *OptionalNullable[str]*                                                                                  | :heavy_minus_sign:                                                                                       | Return files with the specified purpose. Optional.                                                       |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[models.PlatformFilesListResult](../../models/platformfileslistresult.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves a file info.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.platform.files.retrieve(file_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformFilesRetrieveResult](../../models/platformfilesretrieveresult.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a file.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.platform.files.delete(file_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformFilesDeleteResult](../../models/platformfilesdeleteresult.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## download

Downloads a file.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.platform.files.download(file_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |