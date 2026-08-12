# ReasoningEffort

Sets how much reasoning the model does before answering.

This affects reasoning models only, and the available options depend on
the model.

## Example Usage

```python
from friendli_core.models import ReasoningEffort
value: ReasoningEffort = "minimal"
```


## Values

- `"minimal"`
- `"low"`
- `"medium"`
- `"high"`
- `"xhigh"`
- `"max"`
- `"ultracode"`
