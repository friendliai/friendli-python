# FileInitUploadResponse

Initiate file upload response.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `file_id`                                                       | *str*                                                           | :heavy_check_mark:                                              | ID of the file.                                                 |
| `aws`                                                           | Dict[str, *Any*]                                                | :heavy_minus_sign:                                              | AWS fields to be uploaded with file.                            |
| `upload_url`                                                    | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | Upload URL of the file. `None` if the file is already uploaded. |