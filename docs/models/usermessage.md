# UserMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `content`                                                                            | *str*                                                                                | :heavy_check_mark:                                                                   | The content of user message.                                                         |
| `role`                                                                               | *Literal["user"]*                                                                    | :heavy_check_mark:                                                                   | The role of the messages author.                                                     |
| `name`                                                                               | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | The name for the participant to distinguish between participants with the same role. |