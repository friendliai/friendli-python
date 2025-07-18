# ModelCatalogResponseItem

Model listing in `/models` API.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `context_length`                                                  | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `created`                                                         | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `description`                                                     | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `functionality`                                                   | [models.Functionality](../models/functionality.md)                | :heavy_check_mark:                                                | Functionality of the model.                                       |
| `hugging_face_url`                                                | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `license`                                                         | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `max_completion_tokens`                                           | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `name`                                                            | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `policy`                                                          | *Nullable[str]*                                                   | :heavy_check_mark:                                                | N/A                                                               |
| `pricing`                                                         | [models.PricingModel](../models/pricingmodel.md)                  | :heavy_check_mark:                                                | Pricing model supporting both token-based and time-based pricing. |