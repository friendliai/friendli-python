# DedicatedEndpointListResponse

Dedicated endpoint list response.


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `data`                                                                            | Dict[str, [models.DedicatedEndpointStatus](../models/dedicatedendpointstatus.md)] | :heavy_minus_sign:                                                                | The response data containing endpoint statuses.                                   |
| `next_cursor`                                                                     | *OptionalNullable[bytes]*                                                         | :heavy_minus_sign:                                                                | The next cursor for pagination.                                                   |