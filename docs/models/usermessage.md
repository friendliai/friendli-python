# UserMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `role`                                                                               | [models.UserMessageRole](../models/usermessagerole.md)                               | :heavy_check_mark:                                                                   | The role of the messages author.                                                     |
| `content`                                                                            | *str*                                                                                | :heavy_check_mark:                                                                   | The content of user message.                                                         |
| `name`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The name for the participant to distinguish between participants with the same role. |