# Content


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `token`                                                                           | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The token.                                                                        |
| `logprob`                                                                         | *Optional[float]*                                                                 | :heavy_minus_sign:                                                                | The log probability of this token.                                                |
| `top_logprobs`                                                                    | List[[models.TopLogprobs](../models/toplogprobs.md)]                              | :heavy_minus_sign:                                                                | List of the most likely tokens and their log probability, at this token position. |