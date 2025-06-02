# ListDatasetsRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `cursor`                                                       | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]* | :heavy_minus_sign:                                             | N/A                                                            |
| `limit`                                                        | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | N/A                                                            |
| `direction`                                                    | [OptionalNullable[models.Direction]](../models/direction.md)   | :heavy_minus_sign:                                             | N/A                                                            |
| `project_id`                                                   | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `name_search`                                                  | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |
| `x_friendli_team`                                              | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | ID of team to run requests as (optional parameter).            |