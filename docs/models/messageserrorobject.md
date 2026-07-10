# MessagesErrorObject


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | Error category. For HTTP 422 in Messages API, this is `invalid_request_error`. |
| `message`                                                                      | *str*                                                                          | :heavy_check_mark:                                                             | Human-readable error message.                                                  |