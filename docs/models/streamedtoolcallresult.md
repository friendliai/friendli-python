# StreamedToolCallResult


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `function`                                                           | [models.StreamedFunctionResult](../models/streamedfunctionresult.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `index`                                                              | *int*                                                                | :heavy_check_mark:                                                   | The index of tool call being generated.                              |
| `type`                                                               | *Literal["function"]*                                                | :heavy_check_mark:                                                   | The type of the tool.                                                |
| `id`                                                                 | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | The ID of the tool call.                                             |