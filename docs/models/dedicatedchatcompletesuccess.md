# DedicatedChatCompleteSuccess


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `choices`                                                          | List[[models.ChatChoice](../models/chatchoice.md)]                 | :heavy_check_mark:                                                 | N/A                                                                |
| `created`                                                          | *int*                                                              | :heavy_check_mark:                                                 | The Unix timestamp (in seconds) for when the generation completed. |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | A unique ID of the completion.                                     |
| `usage`                                                            | [models.ChatUsage](../models/chatusage.md)                         | :heavy_check_mark:                                                 | N/A                                                                |
| `object`                                                           | *Literal["chat.completion"]*                                       | :heavy_check_mark:                                                 | The object type, which is always set to `chat.completion`.         |