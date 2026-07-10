# DedicatedResponsesRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `x_friendli_team`                                                    | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | ID of team to run requests as (optional parameter).                  |                                                                      |
| `dedicated_responses_body`                                           | [models.DedicatedResponsesBody](../models/dedicatedresponsesbody.md) | :heavy_check_mark:                                                   | N/A                                                                  | {<br/>"input": "Hello!",<br/>"model": "(endpoint-id)"<br/>}          |