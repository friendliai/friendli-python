# PlatformFilesDeleteResult


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `deleted`                                              | *bool*                                                 | :heavy_check_mark:                                     | Deletion status. `true` if deleted, otherwise `false`. |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | ID of the file of interest.                            |
| `object`                                               | *Literal["file"]*                                      | :heavy_check_mark:                                     | The object type, which is always `file`.               |