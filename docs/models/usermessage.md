# UserMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `content`                                                                            | [models.Content](../models/content.md)                                               | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `role`                                                                               | *Literal["user"]*                                                                    | :heavy_check_mark:                                                                   | The role of the message's author.                                                    |
| `name`                                                                               | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | The name for the participant to distinguish between participants with the same role. |