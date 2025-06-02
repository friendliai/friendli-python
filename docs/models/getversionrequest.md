# GetVersionRequest


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `dataset_id`                                        | *str*                                               | :heavy_check_mark:                                  | ID of the dataset.                                  |
| `version_id`                                        | *str*                                               | :heavy_check_mark:                                  | ID of the version to get.                           |
| `x_friendli_team`                                   | *OptionalNullable[str]*                             | :heavy_minus_sign:                                  | ID of team to run requests as (optional parameter). |