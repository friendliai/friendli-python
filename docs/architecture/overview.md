```mermaid
graph LR
    Friendli_Client_Public_API_["Friendli Client (Public API)"]
    SDK_Core["SDK Core"]
    Service_Modules["Service Modules"]
    Data_Models_Error_Handling["Data Models & Error Handling"]
    Platform_Abstractions["Platform Abstractions"]
    Hooks_Extensibility["Hooks & Extensibility"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Unclassified["Unclassified"]
    Friendli_Client_Public_API_ -- "delegates requests to" --> SDK_Core
    SDK_Core -- "utilizes" --> Data_Models_Error_Handling
    SDK_Core -- "adapts behavior based on" --> Platform_Abstractions
    SDK_Core -- "integrates and consumes" --> Hooks_Extensibility
    Service_Modules -- "utilize" --> SDK_Core
    Service_Modules -- "rely on" --> Data_Models_Error_Handling
    click Friendli_Client_Public_API_ href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Friendli_Client_Public_API_.md" "Details"
    click SDK_Core href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/SDK_Core.md" "Details"
    click Service_Modules href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Service_Modules.md" "Details"
    click Data_Models_Error_Handling href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Data_Models_Error_Handling.md" "Details"
    click Platform_Abstractions href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Platform_Abstractions.md" "Details"
    click Hooks_Extensibility href "https://github.com/CodeBoarding/friendli-python/blob/main/.codeboarding/Hooks_Extensibility.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

One paragraph explaining the functionality which is represented by this graph. What the main flow is and what is its purpose.

### Friendli Client (Public API) [[Expand]](./Friendli_Client_Public_API_.md)
The primary entry point for end-users, offering a high-level, consistent interface for interacting with the Friendli AI platform, supporting both synchronous and asynchronous operations.


**Related Classes/Methods**:

- `friendli_core.sdk`


### SDK Core [[Expand]](./SDK_Core.md)
The central orchestrator managing fundamental logic for API communication, request/response processing, and integrating foundational SDK abstractions and extensibility points.


**Related Classes/Methods**:

- `friendli_core.basesdk`


### Service Modules [[Expand]](./Service_Modules.md)
Encapsulate specific API domains (e.g., chat, completions, datasets), providing high-level, domain-specific methods that simplify interactions with particular parts of the Friendli API.


**Related Classes/Methods**:

- `friendli_core.chat`
- `friendli_core.completions`
- `friendli_core.dataset`
- `friendli_core.image`


### Data Models & Error Handling [[Expand]](./Data_Models_Error_Handling.md)
Defines standardized data structures for API requests and responses, along with a comprehensive set of error types, ensuring consistent data representation and robust error reporting.


**Related Classes/Methods**:

- `friendli_core.models`


### Platform Abstractions [[Expand]](./Platform_Abstractions.md)
Provides base structures and interfaces tailored for different operational modes or deployment types within the Friendli platform, enabling the SDK to adapt its behavior to the target environment.


**Related Classes/Methods**:

- `friendli_core.dedicated`
- `friendli_core.serverless`


### Hooks & Extensibility [[Expand]](./Hooks_Extensibility.md)
Offers an extensible mechanism for injecting custom logic at various stages of the request/response lifecycle, allowing for pre-processing, post-processing, and error handling customization.


**Related Classes/Methods**:

- `friendli_core._hooks`


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
