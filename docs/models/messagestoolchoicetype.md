# MessagesToolChoiceType

Tool-calling mode. `auto` lets the model decide, `any` requires at least one tool call, `tool` forces a named tool, and `none` disables tool calls.

## Example Usage

```python
from friendli_core.models import MessagesToolChoiceType
value: MessagesToolChoiceType = "auto"
```


## Values

- `"auto"`
- `"any"`
- `"tool"`
- `"none"`
