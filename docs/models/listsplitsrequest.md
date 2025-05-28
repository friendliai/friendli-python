# ListSplitsRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `dataset_id`                                                   | *int*                                                          | :heavy_check_mark:                                             | ID of the dataset.                                             |
| `cursor`                                                       | *OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]]* | :heavy_minus_sign:                                             | N/A                                                            |
| `limit`                                                        | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | N/A                                                            |
| `x_friendli_team`                                              | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | ID of team to run requests as (optional parameter).            |