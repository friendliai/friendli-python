# ResponsesInputMessage


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `role`                                                                               | [models.ResponsesInputMessageRole](../models/responsesinputmessagerole.md)           | :heavy_check_mark:                                                                   | The role of the message input. One of `user`, `assistant`, `system`, or `developer`. |
| `content`                                                                            | [models.ResponsesInputMessageContent](../models/responsesinputmessagecontent.md)     | :heavy_check_mark:                                                                   | Text or image input to the model. Can also contain previous assistant responses.     |
| `type`                                                                               | *OptionalNullable[Literal["message"]]*                                               | :heavy_minus_sign:                                                                   | The type of the message input. Always `message`.                                     |