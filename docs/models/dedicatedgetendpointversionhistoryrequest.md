# DedicatedGetEndpointVersionHistoryRequest


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `endpoint_id`                                       | *str*                                               | :heavy_check_mark:                                  | The ID of the endpoint.                             |
| `cursor`                                            | *Optional[Union[bytes, IO[bytes], io.IOBase]]*      | :heavy_minus_sign:                                  | Cursor for pagination.                              |
| `limit`                                             | *Optional[int]*                                     | :heavy_minus_sign:                                  | Limit of items per page.                            |
| `x_friendli_team`                                   | *Optional[str]*                                     | :heavy_minus_sign:                                  | ID of team to run requests as (optional parameter). |