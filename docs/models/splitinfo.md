# SplitInfo

Split info.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `created_at`                                                     | *int*                                                            | :heavy_check_mark:                                               | Unix timestamp (in seconds) of when the split was created.       |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | ID of the split.                                                 |
| `length`                                                         | *int*                                                            | :heavy_check_mark:                                               | Number of samples.                                               |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | Name of the split.                                               |
| `size`                                                           | *int*                                                            | :heavy_check_mark:                                               | Size of the split in bytes.                                      |
| `updated_at`                                                     | *int*                                                            | :heavy_check_mark:                                               | Unix timestamp (in seconds) of when the split was last modified. |