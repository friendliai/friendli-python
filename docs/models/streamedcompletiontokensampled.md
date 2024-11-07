# StreamedCompletionTokenSampled


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `event`                                                   | [models.Event](../models/event.md)                        | :heavy_check_mark:                                        | Type of server-sent event.                                |
| `index`                                                   | *int*                                                     | :heavy_check_mark:                                        | The index of the choice in the list of generated choices. |
| `text`                                                    | *str*                                                     | :heavy_check_mark:                                        | Generated text output.                                    |
| `token`                                                   | *int*                                                     | :heavy_check_mark:                                        | Generated output token.                                   |