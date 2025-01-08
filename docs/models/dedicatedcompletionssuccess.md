# DedicatedCompletionsSuccess


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `choices`                                                        | List[[models.CompletionsChoice](../models/completionschoice.md)] | :heavy_check_mark:                                               | N/A                                                              |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | A unique ID of the completion.                                   |
| `usage`                                                          | [models.Usage](../models/usage.md)                               | :heavy_check_mark:                                               | N/A                                                              |
| `object`                                                         | *Literal["text_completion"]*                                     | :heavy_check_mark:                                               | The object type, which is always set to `text_completion`.       |