# SystemMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `content`                                                                            | *str*                                                                                | :heavy_check_mark:                                                                   | The content of system message.                                                       |
| `role`                                                                               | *Literal["system"]*                                                                  | :heavy_check_mark:                                                                   | The role of the messages author.                                                     |
| `name`                                                                               | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | The name for the participant to distinguish between participants with the same role. |