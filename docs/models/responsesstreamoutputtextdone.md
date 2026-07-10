# ResponsesStreamOutputTextDone


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `type`                                                | *Literal["response.output_text.done"]*                | :heavy_check_mark:                                    | The type of the event.                                |
| `item_id`                                             | *str*                                                 | :heavy_check_mark:                                    | The ID of the output item.                            |
| `output_index`                                        | *int*                                                 | :heavy_check_mark:                                    | The index of the output item.                         |
| `content_index`                                       | *int*                                                 | :heavy_check_mark:                                    | The index of the content part within the output item. |
| `text`                                                | *str*                                                 | :heavy_check_mark:                                    | The text content that was added.                      |
| `sequence_number`                                     | *int*                                                 | :heavy_check_mark:                                    | The sequence number for this event.                   |