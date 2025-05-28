# DedicatedEndpointVersionHistoryResponse

Dedicated endpoint version history response.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | Dict[str, [models.DedicatedEndpointSpec](../models/dedicatedendpointspec.md)] | :heavy_minus_sign:                                                            | The response data containing endpoint versions.                               |
| `next_cursor`                                                                 | *OptionalNullable[bytes]*                                                     | :heavy_minus_sign:                                                            | The next cursor for pagination.                                               |