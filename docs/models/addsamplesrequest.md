# AddSamplesRequest


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `dataset_id`                                        | *str*                                               | :heavy_check_mark:                                  | ID of the dataset.                                  |
| `split_id`                                          | *str*                                               | :heavy_check_mark:                                  | ID of the split.                                    |
| `x_friendli_team`                                   | *OptionalNullable[str]*                             | :heavy_minus_sign:                                  | ID of team to run requests as (optional parameter). |
| `request_body`                                      | List[*str*]                                         | :heavy_check_mark:                                  | N/A                                                 |