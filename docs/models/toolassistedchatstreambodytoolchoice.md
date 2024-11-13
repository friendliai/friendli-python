# ToolAssistedChatStreamBodyToolChoice

Determines the tool calling behavior of the model.
When set to `none`, the model will bypass tool execution and generate a response directly.
In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
You can also specify a particular tool by `{"type": "function", "function": {"name": "my_function"}}`.



## Supported Types

### `str`

```python
value: str = /* values here */
```

### `models.ToolAssistedChatStreamBodyToolChoiceObject`

```python
value: models.ToolAssistedChatStreamBodyToolChoiceObject = /* values here */
```

