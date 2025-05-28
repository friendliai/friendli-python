# FileInitUploadResponse

Initiate file upload response.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `file_id`                                                       | *str*                                                           | :heavy_check_mark:                                              | ID of the file.                                                 |
| `upload_url`                                                    | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | Upload URL of the file. `None` if the file is already uploaded. |