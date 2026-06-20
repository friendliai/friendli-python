# BaseClassificationData


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `index`                                              | *int*                                                | :heavy_check_mark:                                   | The index of the input in the list of inputs.        | 0                                                    |
| `label`                                              | *str*                                                | :heavy_check_mark:                                   | The predicted label for the input text.              | Positive                                             |
| `num_classes`                                        | *int*                                                | :heavy_check_mark:                                   | The number of possible labels the model can predict. | 2                                                    |
| `probs`                                              | List[*float*]                                        | :heavy_check_mark:                                   | A list of logits for each possible label.            | [<br/>0.1,<br/>0.9<br/>]                             |