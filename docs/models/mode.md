# Mode

Primary API endpoint type for this model.

``chat`` routes requests to ``/v1/chat/completions``,
``completion`` to ``/v1/completions``, and
``embedding`` to ``/v1/embeddings``.

## Example Usage

```python
from friendli_core.models import Mode
value: Mode = "chat"
```


## Values

- `"chat"`
- `"completion"`
- `"embedding"`
