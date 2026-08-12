# Functionality

Whether the model supports specific features.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `tool_call`                                                 | *bool*                                                      | :heavy_check_mark:                                          | Whether the model supports tool calling.                    |
| `parallel_tool_call`                                        | *bool*                                                      | :heavy_check_mark:                                          | Whether the model supports parallel function calling.       |
| `structured_output`                                         | *bool*                                                      | :heavy_check_mark:                                          | Whether you can enforce a specific output format.           |
| `tool_choice`                                               | *bool*                                                      | :heavy_check_mark:                                          | Whether you can control how the model handles tool calling. |
| `system_messages`                                           | *bool*                                                      | :heavy_check_mark:                                          | Whether the model accepts system role messages.             |