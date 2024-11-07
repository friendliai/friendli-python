# StreamedChatChoiceToolCalls


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `index`                                                                      | *int*                                                                        | :heavy_check_mark:                                                           | The index of tool call being generated.                                      |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The ID of the tool call.                                                     |
| `type`                                                                       | [models.StreamedChatChoiceType](../models/streamedchatchoicetype.md)         | :heavy_check_mark:                                                           | The type of the tool.                                                        |
| `function`                                                                   | [models.StreamedChatChoiceFunction](../models/streamedchatchoicefunction.md) | :heavy_check_mark:                                                           | N/A                                                                          |