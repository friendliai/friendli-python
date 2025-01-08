# StreamedChatData


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `choices`                                                          | List[[models.StreamedChatChoice](../models/streamedchatchoice.md)] | :heavy_check_mark:                                                 | N/A                                                                |
| `created`                                                          | *int*                                                              | :heavy_check_mark:                                                 | The Unix timestamp (in seconds) for when the token sampled.        |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | A unique ID of the chat completion.                                |
| `object`                                                           | *Literal["chat.completion.chunk"]*                                 | :heavy_check_mark:                                                 | The object type, which is always set to `chat.completion.chunk`.   |
| `usage`                                                            | [OptionalNullable[models.ChatUsage]](../models/chatusage.md)       | :heavy_minus_sign:                                                 | N/A                                                                |