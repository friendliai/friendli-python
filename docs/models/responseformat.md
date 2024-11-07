# ResponseFormat

The enforced format of the model's output.

Note that the content of the output message may be truncated if it exceeds the `max_tokens`.
You can check this by verifying that the `finish_reason` of the output message is `length`.

***Important***
You must explicitly instruct the model to produce the desired output format using a system prompt or user message (e.g., `You are an API generating a valid JSON as output.`).
Otherwise, the model may result in an unending stream of whitespace or other characters.



## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [models.Type](../models/type.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Type of the response format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `schema_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The schema of the output. For `{ "type": "json_object" }`, `schema` should be a serialized string of JSON schema. For `{ "type": "regex" }`, `schema` should be a regex pattern.<br/><br/>***Caveat***<br/>For the JSON object type, recursive definitions are not supported. Optional properties are also not supported; all properties of `{ "type": "object" }` are generated regardless of whether they are listed in the `required` field.<br/>For the regex type, lookaheads/lookbehinds (e.g., `\a`, `\z`, `^`, `$`, `(?=)`, `(?!)`, `(?<=...)`, `(?<!...)`) are not supported. Group specials (e.g., `\w`, `\W`, `\d`, `\D`, `\s`, `\S`) do not support non-ASCII characters. Unicode escape patterns (e.g., `\N`, `\p`, `\P`) are not supported. Additionally, conditional matching (`(?(`) and back-references can cause inefficiency.<br/> |