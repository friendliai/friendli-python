# ResponsesStreamFunctionCallArgumentsDone


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `type`                                             | *Literal["response.function_call_arguments.done"]* | :heavy_check_mark:                                 | The type of the event.                             |
| `item_id`                                          | *str*                                              | :heavy_check_mark:                                 | The ID of the output item.                         |
| `output_index`                                     | *int*                                              | :heavy_check_mark:                                 | The index of the output item.                      |
| `arguments`                                        | *str*                                              | :heavy_check_mark:                                 | The function-call arguments.                       |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | The name of the function that was called.          |
| `sequence_number`                                  | *int*                                              | :heavy_check_mark:                                 | The sequence number for this event.                |