# DedicatedEndpointSpec

Dedicated endpoint specification.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the endpoint.                                  |
| `gpu_type`                                                 | *str*                                                      | :heavy_check_mark:                                         | The type of GPU to use for the endpoint.                   |
| `num_gpu`                                                  | *int*                                                      | :heavy_check_mark:                                         | The number of GPUs to use per replica.                     |
| `instance_id`                                              | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The ID of the instance.                                    |
| `project_id`                                               | *str*                                                      | :heavy_check_mark:                                         | The ID of the project that owns the endpoint.              |
| `creator_id`                                               | *str*                                                      | :heavy_check_mark:                                         | The ID of the user who created the endpoint.               |
| `team_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | The ID of the team that owns the endpoint.                 |
| `autoscaling_min`                                          | *int*                                                      | :heavy_check_mark:                                         | The minimum number of replicas to maintain.                |
| `autoscaling_max`                                          | *int*                                                      | :heavy_check_mark:                                         | The maximum number of replicas allowed.                    |
| `autoscaling_cooldown`                                     | *int*                                                      | :heavy_check_mark:                                         | The cooldown period in seconds between scaling operations. |
| `max_batch_size`                                           | *int*                                                      | :heavy_check_mark:                                         | The maximum batch size for inference requests.             |
| `max_input_length`                                         | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | The maximum allowed input length.                          |
| `tokenizer_skip_special_tokens`                            | *bool*                                                     | :heavy_check_mark:                                         | Whether to skip special tokens in tokenizer output.        |
| `tokenizer_add_special_tokens`                             | *bool*                                                     | :heavy_check_mark:                                         | Whether to add special tokens in tokenizer input.          |
| `curr_replica_cnt`                                         | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | The current number of replicas.                            |
| `desired_replica_cnt`                                      | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | The desired number of replicas.                            |
| `updated_replica_cnt`                                      | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | The updated number of replicas.                            |