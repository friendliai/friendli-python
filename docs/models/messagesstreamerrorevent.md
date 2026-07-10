# MessagesStreamErrorEvent


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `type`                                                                     | *Literal["error"]*                                                         | :heavy_check_mark:                                                         | The type of the event.                                                     |
| `error`                                                                    | [models.MessagesStreamErrorDetail](../models/messagesstreamerrordetail.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `request_id`                                                               | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | Request identifier for debugging and support.                              |