# CreateDatasetRequest

Create dataset request.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `name`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | Name of the dataset.                                                     |
| `project_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | ID of the project.                                                       |
| `modality`                                                               | [models.DedicatedDatasetModality](../models/dedicateddatasetmodality.md) | :heavy_check_mark:                                                       | Dataset modality.                                                        |