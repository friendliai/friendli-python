# UserMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `role`                                                                               | *Literal["user"]*                                                                    | :heavy_check_mark:                                                                   | The role of the message's author.                                                    |
| `content`                                                                            | [models.Content](../models/content.md)                                               | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `name`                                                                               | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | The name for the participant to distinguish between participants with the same role. |