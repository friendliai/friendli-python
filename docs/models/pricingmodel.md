# PricingModel

Pricing for a model, charged per individual token in USD.


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `input`                                           | *str*                                             | :heavy_check_mark:                                | Price per 1 input token in USD.                   |
| `output`                                          | *str*                                             | :heavy_check_mark:                                | Price per 1 output token in USD.                  |
| `prompt`                                          | *str*                                             | :heavy_check_mark:                                | Alias of input. Price per 1 input token in USD.   |
| `completion`                                      | *str*                                             | :heavy_check_mark:                                | Alias of output. Price per 1 output token in USD. |
| `input_cache_read`                                | *Nullable[str]*                                   | :heavy_check_mark:                                | Price per 1 cached input token read in USD.       |
| `cache_write`                                     | *Nullable[str]*                                   | :heavy_check_mark:                                | Price per 1 input token written to cache in USD.  |
| `audio_minute`                                    | *Nullable[str]*                                   | :heavy_check_mark:                                | Price per minute of audio in USD.                 |