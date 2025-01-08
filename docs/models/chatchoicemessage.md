# ChatChoiceMessage


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `role`                                                          | *str*                                                           | :heavy_check_mark:                                              | Role of the generated message author, in this case `assistant`. |
| `content`                                                       | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | The contents of the assistant message.                          |
| `tool_calls`                                                    | List[[models.ToolCallResult](../models/toolcallresult.md)]      | :heavy_minus_sign:                                              | N/A                                                             |