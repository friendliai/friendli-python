# MessagesThinkingBlock


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `type`                                                    | *Literal["thinking"]*                                     | :heavy_check_mark:                                        | Content block type. Must be `thinking`.                   |
| `thinking`                                                | *str*                                                     | :heavy_check_mark:                                        | Reasoning content for this block.                         |
| `signature`                                               | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | Optional signature associated with the reasoning content. |