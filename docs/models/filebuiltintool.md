# FileBuiltInTool


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `files`                                                                   | List[*str*]                                                               | :heavy_check_mark:                                                        | A List of file IDs. For now, only one file is supported.                  |
| `type`                                                                    | *Literal["file:text"]*                                                    | :heavy_check_mark:                                                        | The type of the file parser tool. Only .txt and .pdf files are supported. |