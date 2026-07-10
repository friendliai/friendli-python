# MessagesStreamSignatureDelta


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `type`                                          | *Literal["signature_delta"]*                    | :heavy_check_mark:                              | Delta type.                                     |
| `signature`                                     | *str*                                           | :heavy_check_mark:                              | Signature fragment when `type=signature_delta`. |