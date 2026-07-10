# ServerlessResponsesRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `x_friendli_team`                                                      | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | ID of team to run requests as (optional parameter).                    |                                                                        |
| `serverless_responses_body`                                            | [models.ServerlessResponsesBody](../models/serverlessresponsesbody.md) | :heavy_check_mark:                                                     | N/A                                                                    | {<br/>"input": "Hello!",<br/>"model": "zai-org/GLM-5.2"<br/>}          |