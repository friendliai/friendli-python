# MessagesStreamInputJSONDelta


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | *Literal["input_json_delta"]*                                          | :heavy_check_mark:                                                     | Delta type.                                                            |
| `partial_json`                                                         | *str*                                                                  | :heavy_check_mark:                                                     | Partial JSON fragment for tool arguments when `type=input_json_delta`. |