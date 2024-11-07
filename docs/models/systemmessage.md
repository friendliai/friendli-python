# SystemMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `role`                                                                               | [models.Role](../models/role.md)                                                     | :heavy_check_mark:                                                                   | The role of the messages author.                                                     |
| `content`                                                                            | *str*                                                                                | :heavy_check_mark:                                                                   | The content of system message.                                                       |
| `name`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The name for the participant to distinguish between participants with the same role. |