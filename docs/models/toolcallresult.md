# ToolCallResult


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `type`                                               | *Literal["function"]*                                | :heavy_check_mark:                                   | The type of the tool.                                |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | The ID of the tool call.                             |
| `function`                                           | [models.FunctionResult](../models/functionresult.md) | :heavy_check_mark:                                   | N/A                                                  |