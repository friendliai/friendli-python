# CompletionsResult

Successfully generated completions.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `choices`                                                                        | List[[models.CompletionsChoice](../models/completionschoice.md)]                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `usage`                                                                          | [models.Usage](../models/usage.md)                                               | :heavy_check_mark:                                                               | N/A                                                                              |
| `id`                                                                             | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique ID of the completion.                                                   |
| `object`                                                                         | [Optional[models.CompletionsResultObject]](../models/completionsresultobject.md) | :heavy_minus_sign:                                                               | The object type, which is always set to `text_completion`.                       |