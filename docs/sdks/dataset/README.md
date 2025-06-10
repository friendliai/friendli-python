# Dataset
(*dataset*)

## Overview

### Available Operations

* [create_dataset](#create_dataset) - Create a new dataset
* [list_datasets](#list_datasets) - List datasets
* [get_dataset](#get_dataset) - Get dataset info
* [delete_dataset](#delete_dataset) - Delete dataset
* [create_version](#create_version) - Create a version
* [list_versions](#list_versions) - List versions
* [get_version](#get_version) - Get version info
* [delete_version](#delete_version) - Delete a version
* [create_split](#create_split) - Create a split
* [list_splits](#list_splits) - List splits
* [get_split](#get_split) - Get split info
* [delete_split](#delete_split) - Delete split
* [add_samples](#add_samples) - Add samples
* [list_samples](#list_samples) - List samples
* [update_samples](#update_samples) - Update samples
* [delete_samples](#delete_samples) - Delete samples

## create_dataset

Create a new dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.create_dataset(
        modality={}, name="<value>", project_id="<id>"
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `modality`                                                                  | [models.DedicatedDatasetModality](../../models/dedicateddatasetmodality.md) | :heavy_check_mark:                                                          | Dataset modality.                                                           |
| `name`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | Name of the dataset.                                                        |
| `project_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | ID of the project.                                                          |
| `x_friendli_team`                                                           | *OptionalNullable[str]*                                                     | :heavy_minus_sign:                                                          | ID of team to run requests as (optional parameter).                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.DatasetInfo](../../models/datasetinfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_datasets

List datasets accessible to the user.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.list_datasets(project_id="<id>", limit=20)

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `cursor`                                                            | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]*      | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `direction`                                                         | [OptionalNullable[models.Direction]](../../models/direction.md)     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name_search`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDatasetsResponse](../../models/listdatasetsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_dataset

Get information about a specific dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.get_dataset(dataset_id="539201")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset to retrieve.                                      |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetInfo](../../models/datasetinfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_dataset

Delete a specific dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.delete_dataset(dataset_id="195431")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset to delete.                                        |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_version

Create a version for the current state of the split.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.create_version(
        dataset_id="224113",
        comment="New range of formal shirts are designed keeping you in mind. With fits and styling that will make you stand apart",
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `comment`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VersionInfo](../../models/versioninfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_versions

List versions for a dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.list_versions(dataset_id="653403")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListVersionsResponse](../../models/listversionsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_version

Get a dataset version.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.get_version(dataset_id="665101", version_id="813303")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `version_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the version to get.                                           |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VersionInfo](../../models/versioninfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_version

Delete a version from the dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.delete_version(dataset_id="310482", version_id="434150")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `version_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the version to delete.                                        |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_split

Create a new split in the dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.create_split(dataset_id="334066", name="<value>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SplitInfo](../../models/splitinfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_splits

List splits in the dataset.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.list_splits(dataset_id="494482", limit=20)

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `dataset_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the dataset.                                                                  |
| `cursor`                                                                            | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]*                      | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `limit`                                                                             | *OptionalNullable[int]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `direction`                                                                         | [OptionalNullable[models.QueryParamDirection]](../../models/queryparamdirection.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `version_id`                                                                        | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `x_friendli_team`                                                                   | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | ID of team to run requests as (optional parameter).                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ListSplitsResponse](../../models/listsplitsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_split

Get information about a specific split.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.get_split(dataset_id="84405", split_id="516409")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `split_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the split.                                                    |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SplitInfo](../../models/splitinfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_split

Delete a specific split.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.delete_split(dataset_id="724178", split_id="4400")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `split_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the split.                                                    |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## add_samples

Add samples to the split.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.add_samples(
        dataset_id="304268",
        split_id="345943",
        request_body=[
            "0xA76F67a260",
            "0x0274A1ADf1",
            "0x626BF2e0Df",
        ],
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `split_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the split.                                                    |
| `request_body`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddSamplesResponse](../../models/addsamplesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_samples

List samples from the split.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.list_samples(
        dataset_id="282743", split_id="505420", limit=20
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | ID of the dataset.                                                                                        |
| `split_id`                                                                                                | *str*                                                                                                     | :heavy_check_mark:                                                                                        | ID of the split.                                                                                          |
| `cursor`                                                                                                  | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]*                                            | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `limit`                                                                                                   | *OptionalNullable[int]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `direction`                                                                                               | [OptionalNullable[models.ListSamplesQueryParamDirection]](../../models/listsamplesqueryparamdirection.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `version_id`                                                                                              | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `x_friendli_team`                                                                                         | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | ID of team to run requests as (optional parameter).                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.ListSamplesResponse](../../models/listsamplesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_samples

Update samples as raw file.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.update_samples(
        dataset_id="<id>",
        split_id="<id>",
        file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `split_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the split.                                                    |
| `file`                                                              | [models.FileModel](../../models/filemodel.md)                       | :heavy_check_mark:                                                  | File to update samples.                                             |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddSamplesResponse](../../models/addsamplesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_samples

Delete samples from the split.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dataset.delete_samples(
        dataset_id="658326",
        split_id="581117",
        request_body=[
            "<value 1>",
            "<value 2>",
        ],
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the dataset.                                                  |
| `split_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the split.                                                    |
| `request_body`                                                      | List[[models.RequestBody](../../models/requestbody.md)]             | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteSamplesResponse](../../models/deletesamplesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |