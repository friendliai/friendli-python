# MessagesStreamStartThinkingBlock


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `type`                                   | *Literal["thinking"]*                    | :heavy_check_mark:                       | Content block type.                      |
| `thinking`                               | *str*                                    | :heavy_check_mark:                       | Reasoning content when `type=thinking`.  |
| `signature`                              | *OptionalNullable[str]*                  | :heavy_minus_sign:                       | Optional signature when `type=thinking`. |