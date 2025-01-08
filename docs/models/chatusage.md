# ChatUsage


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `completion_tokens`                                                                 | *int*                                                                               | :heavy_check_mark:                                                                  | Number of tokens in the generated chat completions.                                 | 7                                                                                   |
| `prompt_tokens`                                                                     | *int*                                                                               | :heavy_check_mark:                                                                  | Number of tokens in the prompt.                                                     | 5                                                                                   |
| `total_tokens`                                                                      | *int*                                                                               | :heavy_check_mark:                                                                  | Total number of tokens used in the request (`prompt_tokens` + `completion_tokens`). | 12                                                                                  |