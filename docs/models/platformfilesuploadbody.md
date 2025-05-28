# PlatformFilesUploadBody


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `file`                                                                | [models.File](../models/file.md)                                      | :heavy_check_mark:                                                    | The File object (not file name) to be uploaded.                       |
| `purpose`                                                             | [models.Purpose](../models/purpose.md)                                | :heavy_check_mark:                                                    | The intended purpose of the uploaded file. One of `batch` or `model`. |