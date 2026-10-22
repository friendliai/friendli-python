# UsageResponse

Usage response.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `data`                                                                | List[[models.UsageBucket](../models/usagebucket.md)]                  | :heavy_check_mark:                                                    | The items in this page.                                               |                                                                       |
| `has_more`                                                            | *bool*                                                                | :heavy_check_mark:                                                    | Whether more items are available beyond this page.                    | false                                                                 |
| `next_page`                                                           | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | A cursor to fetch the next page. Null when there are no more results. |                                                                       |