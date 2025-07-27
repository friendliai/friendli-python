```mermaid
graph LR
    Service_Modules["Service Modules"]
    Security_Utility["Security Utility"]
    JSON_Unmarshalling_Utility["JSON Unmarshalling Utility"]
    Event_Streaming_Utility["Event Streaming Utility"]
    Hook_Context_Management["Hook Context Management"]
    Service_Modules -- "calls" --> Security_Utility
    Service_Modules -- "invokes" --> JSON_Unmarshalling_Utility
    Service_Modules -- "interacts with" --> Event_Streaming_Utility
    Service_Modules -- "utilizes" --> Hook_Context_Management
    click Service_Modules href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Service_Modules.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

These components are chosen based on their fundamental architectural importance in a Client-side SDK. The `Service Modules` are the primary interface for users, encapsulating domain logic. The `Security Utility` is essential for authentication, a core cross-cutting concern. `JSON Unmarshalling Utility` and `Event Streaming Utility` are vital for handling diverse API response formats. Finally, `Hook Context Management` provides the necessary extensibility, aligning with the "Extensibility" principle mentioned in the project context. This set of components provides a clear, modular, and functional breakdown of the SDK's core responsibilities.

### Service Modules [[Expand]](./Service_Modules.md)
These modules encapsulate the core API domain logic for specific functionalities like Chat, Completions, Dataset management, and Image processing. They provide high-level, domain-specific methods that abstract the underlying API interactions, supporting both asynchronous and synchronous operations. This component is central to the SDK's usability, offering a clear interface for developers to interact with different parts of the Friendli API.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/chat.py#L18-L372" target="_blank" rel="noopener noreferrer">`friendli_core.chat.SyncChat` (18:372)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/chat.py#L375-L729" target="_blank" rel="noopener noreferrer">`friendli_core.chat.AsyncChat` (375:729)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/completions.py#L18-L194" target="_blank" rel="noopener noreferrer">`friendli_core.completions.SyncCompletions` (18:194)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/completions.py#L197-L373" target="_blank" rel="noopener noreferrer">`friendli_core.completions.AsyncCompletions` (197:373)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/dataset.py#L19-L1528" target="_blank" rel="noopener noreferrer">`friendli_core.dataset.SyncDataset` (19:1528)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/dataset.py#L1531-L3040" target="_blank" rel="noopener noreferrer">`friendli_core.dataset.AsyncDataset` (1531:3040)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/image.py#L18-L118" target="_blank" rel="noopener noreferrer">`friendli_core.image.SyncImage` (18:118)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/image.py#L121-L221" target="_blank" rel="noopener noreferrer">`friendli_core.image.AsyncImage` (121:221)</a>


### Security Utility
Responsible for securely retrieving and managing API credentials, typically from environment variables or other configuration sources. This component ensures that API requests are properly authenticated.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/utils/security.py#L57-L69" target="_blank" rel="noopener noreferrer">`friendli_core.utils.security.get_security_from_env` (57:69)</a>


### JSON Unmarshalling Utility
Handles the deserialization of JSON responses received from the Friendli API into structured Python objects. This component is crucial for converting raw API data into usable formats within the SDK.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/utils/unmarshal_json_response.py#L11-L24" target="_blank" rel="noopener noreferrer">`friendli_core.utils.unmarshal_json_response.unmarshal_json_response` (11:24)</a>


### Event Streaming Utility
Provides mechanisms for processing and managing streaming responses from the API, particularly for operations that return continuous data streams (e.g., chat completions). It abstracts the complexities of handling server-sent events or similar streaming protocols.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/utils/eventstreaming.py#L19-L42" target="_blank" rel="noopener noreferrer">`friendli_core.utils.eventstreaming.EventStream` (19:42)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/utils/eventstreaming.py#L45-L68" target="_blank" rel="noopener noreferrer">`friendli_core.utils.eventstreaming.EventStreamAsync` (45:68)</a>


### Hook Context Management
Manages an extensibility mechanism that allows developers to inject custom logic (hooks) at various points during the API interaction lifecycle. This component supports the SDK's extensibility, enabling custom pre-processing, post-processing, or error handling.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/types.py#L11-L30" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.types.HookContext` (11:30)</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
