# FileInfo

File information.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Unix timestamp (in seconds) of when the file was created.            |
| `creator_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | ID of the creator of the file.                                       |
| `digest`                                                             | *str*                                                                | :heavy_check_mark:                                                   | SHA256 hash of the file.                                             |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Unix timestamp (in seconds) of when the file will expire.            |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the file.                                                      |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name of the file.                                                    |
| `project_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | ID of the project the file belongs to.                               |
| `size`                                                               | *int*                                                                | :heavy_check_mark:                                                   | Size of the file in bytes.                                           |
| `status`                                                             | [models.AccountFileStatus](../models/accountfilestatus.md)           | :heavy_check_mark:                                                   | AccountFile status.                                                  |