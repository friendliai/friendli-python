# Endpoint
(*dedicated.endpoint*)

## Overview

### Available Operations

* [wandb_artifact_create](#wandb_artifact_create) - Create endpoint from W&B artifact
* [create](#create) - Create a new endpoint
* [list](#list) - List all endpoints
* [get_spec](#get_spec) - Get endpoint specification
* [update](#update) - Update endpoint spec
* [delete](#delete) - Delete endpoint
* [get_version_history](#get_version_history) - Get endpoint version history
* [get_status](#get_status) - Get endpoint status
* [sleep](#sleep) - Sleep endpoint
* [wake](#wake) - Wake endpoint
* [terminate](#terminate) - Terminate endpoint
* [restart](#restart) - Restart endpoint

## wandb_artifact_create

Create an endpoint from Weights & Biases artifact. If the idempotency key is provided, the API will check if the endpoint already exists, and rollout the existing endpoint if it does. In such cases, the project id must be provided.

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedEndpointWandbArtifactCreate" method="post" path="/dedicated/endpoint/wandb-artifact-create" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.wandb_artifact_create(
        wandb_artifact_version_name="org/registry/name:v0"
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wandb_artifact_version_name`                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                         | The specific model artifact version from Weights & Biases. The referred artifact will be used to create a new endpoint in Friendli Dedicated Endpoints or rollout an existing one.                                                                                                                                         |
| `x_friendli_team`                                                                                                                                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | ID of team to run requests as (optional parameter).                                                                                                                                                                                                                                                                        |
| `accelerator`                                                                                                                                                                                                                                                                                                              | [OptionalNullable[models.AcceleratorRequirement]](../../models/acceleratorrequirement.md)                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Specifies the instance type for the endpoint.                                                                                                                                                                                                                                                                              |
| `name`                                                                                                                                                                                                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Specifies the name of your endpoint. If not provided, a name will be automatically generated for you.                                                                                                                                                                                                                      |
| `project_id`                                                                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Specifies where endpoint will be created in your Friendli Dedicated Endpoints. If not provided, a new project will be created within your default team.                                                                                                                                                                    |
| `idempotency_key`                                                                                                                                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Used by Friendli Dedicated Endpoints to track which webhook automation triggered an endpoint rollout. If the `idempotencyKey` is provided, the API will check if the endpoint already exists, and rollout the existing endpoint if it does. In such cases, the `projectId` must be provided. Any unique value can be used. |
| `autoscaling_policy`                                                                                                                                                                                                                                                                                                       | [OptionalNullable[models.AutoscalingPolicy]](../../models/autoscalingpolicy.md)                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Defines autoscaling settings for the endpoint.                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                        |

### Response

**[models.DedicatedEndpointWandbArtifactCreateResponse](../../models/dedicatedendpointwandbartifactcreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create

Create a new endpoint and return its status

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedCreateEndpoint" method="post" path="/dedicated/beta/endpoint" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.create(
        project_id="<id>",
        name="<value>",
        instance_option_id="<id>",
        advanced={
            "tokenizer_skip_special_tokens": False,
            "tokenizer_add_special_tokens": False,
        },
        hf_model_repo="<value>",
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `project_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the project that owns the endpoint.                                                   |
| `name`                                                                                          | *str*                                                                                           | :heavy_check_mark:                                                                              | The name of the endpoint.                                                                       |
| `instance_option_id`                                                                            | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the instance option.                                                                  |
| `advanced`                                                                                      | [models.EndpointAdvancedConfig](../../models/endpointadvancedconfig.md)                         | :heavy_check_mark:                                                                              | Endpoint advanced config.                                                                       |
| `hf_model_repo`                                                                                 | *str*                                                                                           | :heavy_check_mark:                                                                              | HF ID of the model.                                                                             |
| `x_friendli_team`                                                                               | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | ID of team to run requests as (optional parameter).                                             |
| `simplescale`                                                                                   | [OptionalNullable[models.EndpointSimplescaleConfig]](../../models/endpointsimplescaleconfig.md) | :heavy_minus_sign:                                                                              | The simple scaling configuration of the endpoint.                                               |
| `autoscaling_policy`                                                                            | [OptionalNullable[models.AutoscalingPolicy]](../../models/autoscalingpolicy.md)                 | :heavy_minus_sign:                                                                              | The auto scaling configuration of the endpoint.                                                 |
| `hf_model_repo_revision`                                                                        | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | HF commit hash of the model.                                                                    |
| `initial_version_comment`                                                                       | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The comment for the initial version.                                                            |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.DedicatedEndpointStatus](../../models/dedicatedendpointstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list

List all endpoint statuses

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedListEndpoints" method="get" path="/dedicated/beta/endpoint" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.list(project_id="", limit=20)

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `project_id`                                                           | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The ID of the project. If omitted, query all endpoints under the team. |
| `cursor`                                                               | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]*         | :heavy_minus_sign:                                                     | Cursor for pagination                                                  |
| `limit`                                                                | *OptionalNullable[int]*                                                | :heavy_minus_sign:                                                     | Limit of items per page                                                |
| `x_friendli_team`                                                      | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | ID of team to run requests as (optional parameter).                    |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.DedicatedEndpointListResponse](../../models/dedicatedendpointlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_spec

Get the specification of an endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedGetEndpoint" method="get" path="/dedicated/beta/endpoint/{endpoint_id}" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.get_spec(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointSpec](../../models/dedicatedendpointspec.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update the specification of a specific endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedUpdateEndpoint" method="put" path="/dedicated/beta/endpoint/{endpoint_id}" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.update(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `endpoint_id`                                                                                   | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the endpoint                                                                          |
| `x_friendli_team`                                                                               | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | ID of team to run requests as (optional parameter).                                             |
| `name`                                                                                          | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The name of the endpoint.                                                                       |
| `advanced`                                                                                      | [OptionalNullable[models.EndpointAdvancedConfig]](../../models/endpointadvancedconfig.md)       | :heavy_minus_sign:                                                                              | The advanced configuration of the endpoint.                                                     |
| `simplescale`                                                                                   | [OptionalNullable[models.EndpointSimplescaleConfig]](../../models/endpointsimplescaleconfig.md) | :heavy_minus_sign:                                                                              | The simple scaling configuration of the endpoint.                                               |
| `autoscaling_policy`                                                                            | [OptionalNullable[models.AutoscalingPolicy]](../../models/autoscalingpolicy.md)                 | :heavy_minus_sign:                                                                              | The auto scaling configuration of the endpoint.                                                 |
| `hf_model_repo`                                                                                 | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | HF ID of the model.                                                                             |
| `hf_model_repo_revision`                                                                        | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | HF commit hash of the model.                                                                    |
| `new_version_comment`                                                                           | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | Comment for the new version.                                                                    |
| `instance_option_id`                                                                            | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | The ID of the instance option.                                                                  |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.DedicatedEndpointSpec](../../models/dedicatedendpointspec.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete a specific endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedDeleteEndpoint" method="delete" path="/dedicated/beta/endpoint/{endpoint_id}" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.delete(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_version_history

Get version history of a specific endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedGetEndpointVersionHistory" method="get" path="/dedicated/beta/endpoint/{endpoint_id}/version" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.get_version_history(endpoint_id="<id>", limit=20)

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `cursor`                                                            | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]*      | :heavy_minus_sign:                                                  | Cursor for pagination                                               |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Limit of items per page                                             |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointVersionHistoryResponse](../../models/dedicatedendpointversionhistoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_status

Get the status of a specific endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedGetEndpointStatus" method="get" path="/dedicated/beta/endpoint/{endpoint_id}/status" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.get_status(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointStatus](../../models/dedicatedendpointstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## sleep

Put a specific endpoint to sleep

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedSleepEndpoint" method="put" path="/dedicated/beta/endpoint/{endpoint_id}/sleep" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.sleep(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointStatus](../../models/dedicatedendpointstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## wake

Wake up a specific endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedWakeEndpoint" method="put" path="/dedicated/beta/endpoint/{endpoint_id}/wake" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.wake(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointStatus](../../models/dedicatedendpointstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## terminate

Terminate a specific endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedTerminateEndpoint" method="put" path="/dedicated/beta/endpoint/{endpoint_id}/terminate" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.terminate(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointStatus](../../models/dedicatedendpointstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## restart

Restart a FAILED or TERMINATED endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="dedicatedRestartEndpoint" method="put" path="/dedicated/beta/endpoint/{endpoint_id}/restart" -->
```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.dedicated.endpoint.restart(endpoint_id="<id>")

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the endpoint                                              |
| `x_friendli_team`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ID of team to run requests as (optional parameter).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DedicatedEndpointStatus](../../models/dedicatedendpointstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |