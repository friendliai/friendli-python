# CompletionChoice


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `index`                                                   | *int*                                                     | :heavy_check_mark:                                        | The index of the choice in the list of generated choices. | 0                                                         |
| `seed`                                                    | *int*                                                     | :heavy_check_mark:                                        | Random seed used for the generation.                      | 42                                                        |
| `text`                                                    | *str*                                                     | :heavy_check_mark:                                        | Generated text output.                                    | This is indeed a test                                     |
| `tokens`                                                  | List[*int*]                                               | :heavy_check_mark:                                        | Generated output tokens.                                  | [<br/>128000,<br/>2028,<br/>374,<br/>13118,<br/>264,<br/>1296<br/>] |