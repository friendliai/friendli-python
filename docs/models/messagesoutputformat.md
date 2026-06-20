# MessagesOutputFormat


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | *OptionalNullable[Literal["json_schema"]]*                                     | :heavy_minus_sign:                                                             | Output format type. Set to `json_schema` to constrain output to a JSON schema. |
| `schema_`                                                                      | Dict[str, *Any*]                                                               | :heavy_minus_sign:                                                             | JSON Schema object applied when `type` is `json_schema`.                       |