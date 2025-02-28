# Knowledge
(*serverless.knowledge*)

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve contexts from chosen knowledge base

## retrieve

Retrieve related documents from knowledge base by similarity.

### Example Usage

```python
import os

from friendli import SyncFriendli

with SyncFriendli(
    token=os.getenv("FRIENDLI_TOKEN", ""),
) as friendli:
    res = friendli.serverless.knowledge.retrieve(
        k=1,
        knowledge_ids=[
            "knowledge-base-id-1",
        ],
        query="Chicken dinner",
    )

    # Handle response
    print(res)
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `k`                                                                          | *int*                                                                        | :heavy_check_mark:                                                           | Maximum number of top-ranked knowledge-base entries to return in results.    | 1                                                                            |
| `knowledge_ids`                                                              | List[*str*]                                                                  | :heavy_check_mark:                                                           | A List of knowledge-base IDs. For now, only one knowledge-base is supported. | [<br/>"knowledge-base-id-1"<br/>]                                            |
| `query`                                                                      | *str*                                                                        | :heavy_check_mark:                                                           | A text string used to find relevant information within the knowledge-base.   | Chicken dinner                                                               |
| `x_friendli_team`                                                            | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | ID of team to run requests as (optional parameter).                          |                                                                              |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.ServerlessKnowledgeRetrievalSuccess](../../models/serverlessknowledgeretrievalsuccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |