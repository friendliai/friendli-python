# ServerlessKnowledgeRetrievalBody

Knowledge retrieval request.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `query`                                                                      | *str*                                                                        | :heavy_check_mark:                                                           | A text string used to find relevant information within the knowledge-base.   | Chicken dinner                                                               |
| `k`                                                                          | *int*                                                                        | :heavy_check_mark:                                                           | Maximum number of top-ranked knowledge-base entries to return in results.    | 1                                                                            |
| `knowledge_ids`                                                              | List[*str*]                                                                  | :heavy_check_mark:                                                           | A List of knowledge-base IDs. For now, only one knowledge-base is supported. | [<br/>"knowledge-base-id-1"<br/>]                                            |