# Cost

## Overview

### Available Operations

* [get_costs](#get_costs) - Get cost details for the team.

## get_costs

Get cost details for the team.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCosts" method="get" path="/v1/team/cost" -->
```python
import os

from friendli import SyncFriendli
from friendli.utils import parse_datetime

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.cost.get_costs(
        start_time=parse_datetime("2025-11-15T17:37:03.985Z"),
        end_time=parse_datetime("2024-07-27T03:54:55.930Z"),
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                               | :heavy_check_mark:                                                                                                                 | RFC 3339 timestamp in UTC. The time portion must be zeroed out (e.g., 2026-01-01T00:00:00Z). Must be no earlier than one year ago. |
| `end_time`                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                               | :heavy_check_mark:                                                                                                                 | RFC 3339 timestamp in UTC. The time portion must be zeroed out (e.g., 2026-01-02T00:00:00Z).                                       |
| `bucket_width`                                                                                                                     | [OptionalNullable[models.CostBucketWidth]](../../models/costbucketwidth.md)                                                        | :heavy_minus_sign:                                                                                                                 | Width of each time bucket in response. Currently only `1d` is supported, default to `1d`.                                          |
| `limit`                                                                                                                            | *OptionalNullable[int]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | A limit on the number of buckets to be returned. Limit can range between 1 and 35, and the default is 7.                           |
| `page`                                                                                                                             | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.                                 |
| `group_by`                                                                                                                         | [OptionalNullable[models.CostGroupBy]](../../models/costgroupby.md)                                                                | :heavy_minus_sign:                                                                                                                 | Group the costs by the specified fields. Currently only `line_item` is supported.                                                  |
| `x_friendli_team`                                                                                                                  | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | ID of team to run requests as (optional parameter).                                                                                |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[models.CostResponse](../../models/costresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |