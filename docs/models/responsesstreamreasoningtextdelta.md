# ResponsesStreamReasoningTextDelta


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `type`                                                  | *Literal["response.reasoning_text.delta"]*              | :heavy_check_mark:                                      | The type of the event.                                  |
| `item_id`                                               | *str*                                                   | :heavy_check_mark:                                      | The ID of the reasoning output item.                    |
| `output_index`                                          | *int*                                                   | :heavy_check_mark:                                      | The index of the output item.                           |
| `content_index`                                         | *int*                                                   | :heavy_check_mark:                                      | The index of the reasoning content part.                |
| `delta`                                                 | *str*                                                   | :heavy_check_mark:                                      | The text delta that was added to the reasoning content. |
| `sequence_number`                                       | *int*                                                   | :heavy_check_mark:                                      | The sequence number for this event.                     |