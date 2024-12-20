# ChatResult

Successfully generated a chat response.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `choices`                                                          | List[[models.ChatChoice](../models/chatchoice.md)]                 | :heavy_check_mark:                                                 | N/A                                                                |
| `usage`                                                            | [models.Usage](../models/usage.md)                                 | :heavy_check_mark:                                                 | N/A                                                                |
| `created`                                                          | *int*                                                              | :heavy_check_mark:                                                 | The Unix timestamp (in seconds) for when the generation completed. |
| `id`                                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A unique ID of the chat completion.                                |
| `object`                                                           | [Optional[models.Object]](../models/object.md)                     | :heavy_minus_sign:                                                 | The object type, which is always set to `chat.completion`.         |