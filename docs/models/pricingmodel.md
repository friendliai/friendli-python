# PricingModel

Pricing model supporting both token-based and time-based pricing.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `input`                                                                          | *float*                                                                          | :heavy_check_mark:                                                               | Price per input token                                                            |
| `output`                                                                         | *float*                                                                          | :heavy_check_mark:                                                               | Price per output token                                                           |
| `response_time`                                                                  | *Optional[float]*                                                                | :heavy_minus_sign:                                                               | Price per response time in seconds                                               |
| `unit_type`                                                                      | [Optional[models.ServerlessPriceUnitType]](../models/serverlesspriceunittype.md) | :heavy_minus_sign:                                                               | Serverless price unit type.                                                      |