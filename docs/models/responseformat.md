# ResponseFormat

The enforced format of the model's output.

Note that the content of the output message may be truncated if it exceeds the `max_tokens`.
You can check this by verifying that the `finish_reason` of the output message is `length`.

***Important***
You must explicitly instruct the model to produce the desired output format using a system prompt or user message (e.g., `You are an API generating a valid JSON as output.`).
Otherwise, the model may result in an unending stream of whitespace or other characters.

**When `response_format` is specified, `min_tokens` field is unsupported.**



## Supported Types

### `models.ResponseFormatJSONSchema`

```python
value: models.ResponseFormatJSONSchema = /* values here */
```

### `models.ResponseFormatJSONObject`

```python
value: models.ResponseFormatJSONObject = /* values here */
```

### `models.ResponseFormatRegex`

```python
value: models.ResponseFormatRegex = /* values here */
```

### `models.ResponseFormatText`

```python
value: models.ResponseFormatText = /* values here */
```

