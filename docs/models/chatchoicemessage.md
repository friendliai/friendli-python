# ChatChoiceMessage


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `content`                                                       | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | The contents of the assistant message.                          |
| `role`                                                          | *str*                                                           | :heavy_check_mark:                                              | Role of the generated message author, in this case `assistant`. |
| `tool_calls`                                                    | List[[models.ToolCallResult](../models/toolcallresult.md)]      | :heavy_minus_sign:                                              | N/A                                                             |