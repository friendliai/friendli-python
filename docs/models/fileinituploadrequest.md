# FileInitUploadRequest

Initiate file upload request.


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `digest`                               | *str*                                  | :heavy_check_mark:                     | Digest of the file.                    |
| `name`                                 | *str*                                  | :heavy_check_mark:                     | Name of the file.                      |
| `project_id`                           | *str*                                  | :heavy_check_mark:                     | ID of the project the file belongs to. |
| `size`                                 | *int*                                  | :heavy_check_mark:                     | Size of the file in bytes.             |