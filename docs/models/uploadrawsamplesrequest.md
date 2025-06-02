# UploadRawSamplesRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `dataset_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | ID of the dataset.                                               |
| `split_id`                                                       | *str*                                                            | :heavy_check_mark:                                               | ID of the split.                                                 |
| `x_friendli_team`                                                | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | ID of team to run requests as (optional parameter).              |
| `body_upload_raw_samples`                                        | [models.BodyUploadRawSamples](../models/bodyuploadrawsamples.md) | :heavy_check_mark:                                               | N/A                                                              |