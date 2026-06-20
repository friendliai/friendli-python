# MessagesResponseThinkingBlock


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `type`                                           | *Literal["thinking"]*                            | :heavy_check_mark:                               | Content block type.                              |
| `thinking`                                       | *str*                                            | :heavy_check_mark:                               | Reasoning content returned by the model.         |
| `signature`                                      | *str*                                            | :heavy_check_mark:                               | Signature associated with the reasoning content. |