# Data


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `choices`                                                          | List[[models.StreamedChatChoice](../models/streamedchatchoice.md)] | :heavy_check_mark:                                                 | N/A                                                                |
| `created`                                                          | *int*                                                              | :heavy_check_mark:                                                 | The Unix timestamp (in seconds) for when the token sampled.        |
| `usage`                                                            | [Optional[models.Usage]](../models/usage.md)                       | :heavy_minus_sign:                                                 | N/A                                                                |