# ResponsesStreamContentPartAdded


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `type`                                                           | *Literal["response.content_part.added"]*                         | :heavy_check_mark:                                               | The type of the event.                                           |
| `item_id`                                                        | *str*                                                            | :heavy_check_mark:                                               | The ID of the output item the content part was added to.         |
| `output_index`                                                   | *int*                                                            | :heavy_check_mark:                                               | The index of the output item.                                    |
| `content_index`                                                  | *int*                                                            | :heavy_check_mark:                                               | The index of the content part within the output item.            |
| `part`                                                           | [models.ResponsesContentPart](../models/responsescontentpart.md) | :heavy_check_mark:                                               | N/A                                                              |
| `sequence_number`                                                | *int*                                                            | :heavy_check_mark:                                               | The sequence number for this event.                              |