# Rag
(*serverless.rag*)

## Overview

### Available Operations

* [knowledge_retrieve](#knowledge_retrieve) - Knowledge retrieve

## knowledge_retrieve

Retrieve related documents from vector store by similarity.

### Example Usage

```python
from friendli import SyncFriendli
import os

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:

    res = friendli.serverless.rag.knowledge_retrieve(
        query="Chicken dinner",
        k=1,
        knowledge_ids=[
            "knowledge-base-id-1",
        ],
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_friendli_team`                                                            | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | ID of team to run requests as (optional parameter).                          |                                                                              |
| `query`                                                                      | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | A text string used to find relevant information within the knowledge-base.   | Chicken dinner                                                               |
| `k`                                                                          | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Maximum number of top-ranked knowledge-base entries to return in results.    | 1                                                                            |
| `knowledge_ids`                                                              | List[*str*]                                                                  | :heavy_minus_sign:                                                           | A List of knowledge-base IDs. For now, only one knowledge-base is supported. | [<br/>"knowledge-base-id-1"<br/>]                                            |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.KnowledgeRetrieveResult](../../models/knowledgeretrieveresult.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |