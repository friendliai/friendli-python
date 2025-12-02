# FileInitUploadRequest

Initiate file upload request.


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `name`                                 | *str*                                  | :heavy_check_mark:                     | Name of the file.                      |
| `size`                                 | *int*                                  | :heavy_check_mark:                     | Size of the file in bytes.             |
| `digest`                               | *str*                                  | :heavy_check_mark:                     | Digest of the file.                    |
| `project_id`                           | *str*                                  | :heavy_check_mark:                     | ID of the project the file belongs to. |