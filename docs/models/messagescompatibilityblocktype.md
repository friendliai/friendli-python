# MessagesCompatibilityBlockType

Compatibility block type. These blocks are accepted for parsing compatibility and ignored for generation.

## Example Usage

```python
from friendli_core.models import MessagesCompatibilityBlockType
value: MessagesCompatibilityBlockType = "document"
```


## Values

- `"document"`
- `"search_result"`
- `"redacted_thinking"`
- `"server_tool_use"`
- `"web_search_tool_result"`
- `"web_fetch_tool_result"`
- `"code_execution_tool_result"`
- `"bash_code_execution_tool_result"`
- `"text_editor_code_execution_tool_result"`
- `"tool_search_tool_result"`
- `"container_upload"`
