```mermaid
graph LR
    Core_Client_Public_API_["Core Client (Public API)"]
    Service_Modules["Service Modules"]
    Data_Models["Data Models"]
    HTTP_Client_Transport_Layer["HTTP Client/Transport Layer"]
    Error_Handling["Error Handling"]
    Configuration_Management["Configuration Management"]
    Utility_Functions["Utility Functions"]
    Core_Client_Public_API_ -- "uses" --> Service_Modules
    Core_Client_Public_API_ -- "uses" --> Configuration_Management
    Core_Client_Public_API_ -- "uses" --> Data_Models
    Core_Client_Public_API_ -- "uses" --> Utility_Functions
    Service_Modules -- "uses" --> HTTP_Client_Transport_Layer
    Service_Modules -- "uses" --> Data_Models
    Service_Modules -- "uses" --> Error_Handling
    Service_Modules -- "uses" --> Utility_Functions
    HTTP_Client_Transport_Layer -- "uses" --> Configuration_Management
    HTTP_Client_Transport_Layer -- "uses" --> Error_Handling
    click Service_Modules href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Service_Modules.md" "Details"
    click Error_Handling href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Error_Handling.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

Final Component Overview for the `Friendli Client (Public API)` subsystem, structured according to Client-side SDK patterns.

### Core Client (Public API)
The primary entry point for end-users, offering a high-level, consistent interface for interacting with the Friendli AI platform, supporting both synchronous and asynchronous operations. It acts as the orchestrator, delegating requests to specific service modules.


**Related Classes/Methods**:

- `friendli_core.sdk`


### Service Modules [[Expand]](./Service_Modules.md)
Encapsulate the logic for interacting with specific API endpoints (e.g., chat, completions, images, audio). Each module handles the construction of requests, serialization of data models, and deserialization of responses for its domain.


**Related Classes/Methods**:

- `friendli_core.chat`
- `friendli_core.completions`
- `friendli_core.images` (1:1)
- `friendli_core.audio`


### Data Models
Define the structure of data exchanged with the Friendli AI platform, including request bodies, response objects, and various parameters. Ensures type safety and consistency across all API interactions within the SDK.


**Related Classes/Methods**:

- `friendli_core.models` (1:1)


### HTTP Client/Transport Layer
Handles the low-level HTTP communication with the Friendli AI platform. This includes managing connections, sending requests, receiving responses, and abstracting away network-level concerns like retries and timeouts.


**Related Classes/Methods**:

- `friendli_core.http_client` (1:1)


### Error Handling [[Expand]](./Error_Handling.md)
Manages and standardizes error responses from both the API and the network layer. It provides custom exception classes and mechanisms for users to gracefully handle API-related issues and network errors, ensuring a consistent error reporting experience.


**Related Classes/Methods**:

- `friendli_core.errors` (1:1)


### Configuration Management
Centralizes and manages SDK-wide configuration settings, such as API keys, base URLs, default timeouts, and retry policies. It provides a consistent and accessible way to configure the SDK's behavior.


**Related Classes/Methods**:

- `friendli_core.config` (1:1)


### Utility Functions
Provides common helper functions and reusable functionalities that support various parts of the SDK, such as authentication token management, data validation, or specific data transformations that are not tied to a particular API domain.


**Related Classes/Methods**:

- `friendli_core.utils` (1:1)




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
