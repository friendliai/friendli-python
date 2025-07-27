```mermaid
graph LR
    Hook_Contexts_DTOs_["Hook Contexts (DTOs)"]
    Hook_Interface["Hook Interface"]
    SDK_Hooks_Orchestrator["SDK Hooks Orchestrator"]
    Hook_Contexts_DTOs_ -- "provides data to" --> Hook_Interface
    SDK_Hooks_Orchestrator -- "interacts with" --> Hook_Contexts_DTOs_
    SDK_Hooks_Orchestrator -- "orchestrates" --> Hook_Interface
    Hook_Interface -- "receives" --> Hook_Contexts_DTOs_
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

Offers an extensible mechanism for injecting custom logic at various stages of the request/response lifecycle, allowing for pre-processing, post-processing, and error handling customization.

### Hook Contexts (DTOs)
A set of specialized Data Transfer Objects (DTOs) that encapsulate and pass relevant data and state through different stages of the API request/response lifecycle. These contexts provide the necessary information for hooks to operate on.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/types.py#L11-L30" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.types.HookContext` (11:30)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/types.py#L33-L41" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.types.BeforeRequestContext` (33:41)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/types.py#L44-L52" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.types.AfterSuccessContext` (44:52)</a>
- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/types.py#L55-L63" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.types.AfterErrorContext` (55:63)</a>


### Hook Interface
Defines the abstract interface or base class that custom hooks must implement. It establishes the contract for various hook methods (e.g., `before_request`, `after_success`, `after_error`), ensuring a consistent extensibility point for SDK users.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/types.py#L99-L114" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.types.Hooks` (99:114)</a>


### SDK Hooks Orchestrator
The central manager responsible for registering, storing, and orchestrating the execution of various custom hooks at the appropriate stages of the SDK's request/response lifecycle. It acts as a facade for the entire hooks mechanism.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/friendli-python/blob/main/src/friendli_core/_hooks/sdkhooks.py#L21-L78" target="_blank" rel="noopener noreferrer">`friendli_core._hooks.sdkhooks.SDKHooks` (21:78)</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
