# ContainerDetokenizationBody


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `model`                                      | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | Routes the request to a specific adapter.    | (adapter-route)                              |
| `tokens`                                     | List[*int*]                                  | :heavy_check_mark:                           | A token sequence to detokenize.              | [<br/>128000,<br/>3923,<br/>374,<br/>1803,<br/>1413,<br/>15592,<br/>30<br/>] |