# MessagesErrorObject


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | Error category. For HTTP 422 in Messages API, this is `invalid_request_error`. |
| `message`                                                                      | *str*                                                                          | :heavy_check_mark:                                                             | Human-readable error message.                                                  |
| `__pydantic_extra__`                                                           | Dict[str, *Any*]                                                               | :heavy_minus_sign:                                                             | N/A                                                                            |