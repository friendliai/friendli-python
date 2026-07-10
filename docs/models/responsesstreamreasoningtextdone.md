# ResponsesStreamReasoningTextDone


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `type`                                            | *Literal["response.reasoning_text.done"]*         | :heavy_check_mark:                                | The type of the event.                            |
| `item_id`                                         | *str*                                             | :heavy_check_mark:                                | The ID of the reasoning output item.              |
| `output_index`                                    | *int*                                             | :heavy_check_mark:                                | The index of the output item.                     |
| `content_index`                                   | *int*                                             | :heavy_check_mark:                                | The index of the reasoning content part.          |
| `text`                                            | *str*                                             | :heavy_check_mark:                                | The full text of the completed reasoning content. |
| `sequence_number`                                 | *int*                                             | :heavy_check_mark:                                | The sequence number for this event.               |