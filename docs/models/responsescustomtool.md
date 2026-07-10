# ResponsesCustomTool


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | *Literal["custom"]*                                                    | :heavy_check_mark:                                                     | The type of the custom tool. Always `custom`.                          |
| `name`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | The name of the custom tool, used to identify it in tool calls.        |
| `description`                                                          | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | Optional description of the custom tool, used to provide more context. |