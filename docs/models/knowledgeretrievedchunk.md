# KnowledgeRetrievedChunk

Knowledge retrieved chunk.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `text`                                             | *str*                                              | :heavy_check_mark:                                 | Retrieved text matching the search query.          |
| `score`                                            | *float*                                            | :heavy_check_mark:                                 | Numerical relevance score of the retrieved result. |
| `content_chunk_id`                                 | *str*                                              | :heavy_check_mark:                                 | ID of specific text segment.                       |
| `content_id`                                       | *str*                                              | :heavy_check_mark:                                 | ID of content in knowledge-base.                   |