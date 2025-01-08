# ToolMessage


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `content`                                                             | *str*                                                                 | :heavy_check_mark:                                                    | The content of tool message that contains the result of tool calling. |
| `tool_call_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The ID of tool call corresponding to this message.                    |
| `role`                                                                | *Literal["tool"]*                                                     | :heavy_check_mark:                                                    | The role of the messages author.                                      |
| `name`                                                                | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | An optional name of the tool call corresponding to this message.      |