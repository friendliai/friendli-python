# DedicatedListEndpointsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `project_id`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The ID of the project. If omitted, query all endpoints under the team. |
| `cursor`                                                               | *Optional[Union[bytes, IO[bytes], io.IOBase]]*                         | :heavy_minus_sign:                                                     | Cursor for pagination.                                                 |
| `limit`                                                                | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Limit of items per page.                                               |
| `x_friendli_team`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | ID of team to run requests as (optional parameter).                    |