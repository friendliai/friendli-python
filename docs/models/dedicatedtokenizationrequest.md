# DedicatedTokenizationRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `x_friendli_team`                                                          | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | ID of team to run requests as (optional parameter).                        |                                                                            |
| `dedicated_tokenization_body`                                              | [models.DedicatedTokenizationBody](../models/dedicatedtokenizationbody.md) | :heavy_check_mark:                                                         | N/A                                                                        | {<br/>"model": "(endpoint-id)",<br/>"prompt": "What is generative AI?"<br/>} |