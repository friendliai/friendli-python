# ListSamplesResponse

List samples response.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `data`                                                                      | List[List[*str*]]                                                           | :heavy_check_mark:                                                          | List of items.                                                              |
| `next_cursor`                                                               | *OptionalNullable[bytes]*                                                   | :heavy_minus_sign:                                                          | Next cursor to use for pagination. `None` indicates no more items to fetch. |