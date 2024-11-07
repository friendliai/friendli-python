# ChatCompletionResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `choices`                                                              | List[[models.ChatCompletionChoice](../models/chatcompletionchoice.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `usage`                                                                | [models.Usage](../models/usage.md)                                     | :heavy_check_mark:                                                     | N/A                                                                    |
| `created`                                                              | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | The Unix timestamp (in seconds) for when the generation completed.     |