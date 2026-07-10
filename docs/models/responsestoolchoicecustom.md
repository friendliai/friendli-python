# ResponsesToolChoiceCustom


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `type`                                                | *Literal["custom"]*                                   | :heavy_check_mark:                                    | For custom tool calling, the type is always `custom`. |
| `name`                                                | *str*                                                 | :heavy_check_mark:                                    | The name of the custom tool to call.                  |