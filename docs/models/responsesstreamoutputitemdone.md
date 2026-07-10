# ResponsesStreamOutputItemDone


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `type`                                                         | *Literal["response.output_item.done"]*                         | :heavy_check_mark:                                             | The type of the event.                                         |
| `output_index`                                                 | *int*                                                          | :heavy_check_mark:                                             | The index of the output item that was marked done.             |
| `item`                                                         | [models.ResponsesOutputItem](../models/responsesoutputitem.md) | :heavy_check_mark:                                             | N/A                                                            |
| `sequence_number`                                              | *int*                                                          | :heavy_check_mark:                                             | The sequence number for this event.                            |