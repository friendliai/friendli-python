# ReasoningBudgetTokens

Specifies a limit on the number of tokens used for reasoning.

The limit is an integer count of reasoning (thinking) tokens.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | *Literal["budget_tokens"]*                                                     | :heavy_check_mark:                                                             | N/A                                                                            |
| `min`                                                                          | *Nullable[int]*                                                                | :heavy_check_mark:                                                             | Minimum reasoning tokens. `-1` means the model reasons without a budget limit. |
| `max`                                                                          | *Nullable[int]*                                                                | :heavy_check_mark:                                                             | Maximum reasoning token budget.                                                |