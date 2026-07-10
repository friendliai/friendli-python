# ServerlessResponsesStreamBodyToolChoiceUnion

Controls which (if any) tool is called by the model. `none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools. An object can be used to force the model to call a specific function or custom tool.


## Supported Types

### `models.ServerlessResponsesStreamBodyToolChoiceEnum`

```python
value: models.ServerlessResponsesStreamBodyToolChoiceEnum = /* values here */
```

### `models.ResponsesToolChoiceFunction`

```python
value: models.ResponsesToolChoiceFunction = /* values here */
```

### `models.ResponsesToolChoiceCustom`

```python
value: models.ResponsesToolChoiceCustom = /* values here */
```

