# ToolCalls


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | The ID of tool call.                                                     |
| `type`                                                                   | [models.AssistantMessageType](../models/assistantmessagetype.md)         | :heavy_check_mark:                                                       | The type of tool call.                                                   |
| `function`                                                               | [models.AssistantMessageFunction](../models/assistantmessagefunction.md) | :heavy_check_mark:                                                       | The function specification                                               |