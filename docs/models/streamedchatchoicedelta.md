# StreamedChatChoiceDelta


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `content`                                                                  | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | The contents of the assistant message.                                     |
| `role`                                                                     | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | Role of the generated message author, in this case `assistant`.            |
| `tool_calls`                                                               | List[[models.StreamedToolCallResult](../models/streamedtoolcallresult.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |