# FileInfo

File information.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the file.                                                      |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name of the file.                                                    |
| `size`                                                               | *int*                                                                | :heavy_check_mark:                                                   | Size of the file in bytes.                                           |
| `digest`                                                             | *str*                                                                | :heavy_check_mark:                                                   | SHA256 hash of the file.                                             |
| `project_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | ID of the project the file belongs to.                               |
| `creator_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | ID of the creator of the file.                                       |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Unix timestamp (in seconds) of when the file was created.            |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Unix timestamp (in seconds) of when the file will expire.            |
| `status`                                                             | [models.AccountFileStatus](../models/accountfilestatus.md)           | :heavy_check_mark:                                                   | AccountFile status.                                                  |