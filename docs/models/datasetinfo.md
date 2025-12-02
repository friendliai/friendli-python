# DatasetInfo

Dataset info.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | ID of the dataset.                                                       |
| `name`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | Name of the dataset.                                                     |
| `created_at`                                                             | *int*                                                                    | :heavy_check_mark:                                                       | Unix timestamp (in seconds) of when the dataset was created.             |
| `updated_at`                                                             | *int*                                                                    | :heavy_check_mark:                                                       | Unix timestamp (in seconds) of when the dataset was last modified.       |
| `modality`                                                               | [models.DedicatedDatasetModality](../models/dedicateddatasetmodality.md) | :heavy_check_mark:                                                       | Dataset modality.                                                        |