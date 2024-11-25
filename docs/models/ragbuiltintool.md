# RagBuiltInTool


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `type`                                                                       | [models.RagBuiltInToolType](../models/ragbuiltintooltype.md)                 | :heavy_check_mark:                                                           | The type of the rag knowledge-base tool.                                     |
| `knowledge_base_ids`                                                         | List[*str*]                                                                  | :heavy_check_mark:                                                           | A List of knowledge-base IDs. For now, only one knowledge-base is supported. |