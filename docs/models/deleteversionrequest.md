# DeleteVersionRequest


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `dataset_id`                                        | *int*                                               | :heavy_check_mark:                                  | ID of the dataset.                                  |
| `split_id`                                          | *int*                                               | :heavy_check_mark:                                  | ID of the split.                                    |
| `version_id`                                        | *int*                                               | :heavy_check_mark:                                  | ID of the version to delete.                        |
| `x_friendli_team`                                   | *OptionalNullable[str]*                             | :heavy_minus_sign:                                  | ID of team to run requests as (optional parameter). |