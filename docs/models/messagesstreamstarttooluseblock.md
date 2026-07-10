# MessagesStreamStartToolUseBlock


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `type`                                         | *Literal["tool_use"]*                          | :heavy_check_mark:                             | Content block type.                            |
| `id`                                           | *str*                                          | :heavy_check_mark:                             | Tool call ID when `type=tool_use`.             |
| `name`                                         | *str*                                          | :heavy_check_mark:                             | Tool name when `type=tool_use`.                |
| `input`                                        | Dict[str, *Any*]                               | :heavy_check_mark:                             | Parsed tool input object when `type=tool_use`. |