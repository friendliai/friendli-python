# DedicatedCompletionsCompleteRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `x_friendli_team`                                                        | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | ID of team to run requests as (optional parameter).                      |                                                                          |
| `dedicated_completions_body`                                             | [models.DedicatedCompletionsBody](../models/dedicatedcompletionsbody.md) | :heavy_check_mark:                                                       | N/A                                                                      | {<br/>"model": "(endpoint-id)",<br/>"prompt": "Say this is a test!"<br/>} |