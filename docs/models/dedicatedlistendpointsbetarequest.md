# DedicatedListEndpointsBetaRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `project_id`                                                           | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The ID of the project. If omitted, query all endpoints under the team. |
| `cursor`                                                               | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]*         | :heavy_minus_sign:                                                     | Cursor for pagination                                                  |
| `limit`                                                                | *OptionalNullable[int]*                                                | :heavy_minus_sign:                                                     | Limit of items per page                                                |
| `x_friendli_team`                                                      | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | ID of team to run requests as (optional parameter).                    |