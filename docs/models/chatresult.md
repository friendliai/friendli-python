# ChatResult

Successfully generated a chat response.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A unique ID of the chat completion.                                |
| `object`                                                           | [Optional[models.Object]](../models/object.md)                     | :heavy_minus_sign:                                                 | The object type, which is always set to `chat.completion`.         |
| `choices`                                                          | List[[models.ChatChoice](../models/chatchoice.md)]                 | :heavy_minus_sign:                                                 | N/A                                                                |
| `usage`                                                            | [Optional[models.Usage]](../models/usage.md)                       | :heavy_minus_sign:                                                 | N/A                                                                |
| `created`                                                          | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | The Unix timestamp (in seconds) for when the generation completed. |