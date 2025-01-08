# StreamedToolCallResult


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `function`                                           | [models.FunctionResult](../models/functionresult.md) | :heavy_check_mark:                                   | N/A                                                  |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | The ID of the tool call.                             |
| `index`                                              | *int*                                                | :heavy_check_mark:                                   | The index of tool call being generated.              |
| `type`                                               | *Literal["function"]*                                | :heavy_check_mark:                                   | The type of the tool.                                |