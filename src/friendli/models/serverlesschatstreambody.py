"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .message import Message, MessageTypedDict
from .responseformat import ResponseFormat, ResponseFormatTypedDict
from .tool import Tool, ToolTypedDict
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class ServerlessChatStreamBodyLogitBiasTypedDict(TypedDict):
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""


class ServerlessChatStreamBodyLogitBias(BaseModel):
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""


class ServerlessChatStreamBodyStreamOptionsTypedDict(TypedDict):
    r"""Options related to stream.
    It can only be used when `stream: true`.

    """

    include_usage: NotRequired[Nullable[bool]]
    r"""When set to `true`,
    the number of tokens used will be included at the end of the stream result in the form of
    `\"usage\": {\"completion_tokens\": number, \"prompt_tokens\": number, \"total_tokens\": number}`.

    """


class ServerlessChatStreamBodyStreamOptions(BaseModel):
    r"""Options related to stream.
    It can only be used when `stream: true`.

    """

    include_usage: OptionalNullable[bool] = UNSET
    r"""When set to `true`,
    the number of tokens used will be included at the end of the stream result in the form of
    `\"usage\": {\"completion_tokens\": number, \"prompt_tokens\": number, \"total_tokens\": number}`.

    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["include_usage"]
        nullable_fields = ["include_usage"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


ServerlessChatStreamBodyToolChoiceType = Literal["function"]
r"""The type of the tool. Currently, only `function` is supported."""


class ServerlessChatStreamBodyToolChoiceFunctionTypedDict(TypedDict):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""


class ServerlessChatStreamBodyToolChoiceFunction(BaseModel):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""


class ServerlessChatStreamBodyToolChoiceObjectTypedDict(TypedDict):
    type: ServerlessChatStreamBodyToolChoiceType
    r"""The type of the tool. Currently, only `function` is supported."""
    function: ServerlessChatStreamBodyToolChoiceFunctionTypedDict


class ServerlessChatStreamBodyToolChoiceObject(BaseModel):
    type: ServerlessChatStreamBodyToolChoiceType
    r"""The type of the tool. Currently, only `function` is supported."""

    function: ServerlessChatStreamBodyToolChoiceFunction


ServerlessChatStreamBodyToolChoiceTypedDict = TypeAliasType(
    "ServerlessChatStreamBodyToolChoiceTypedDict",
    Union[ServerlessChatStreamBodyToolChoiceObjectTypedDict, str],
)
r"""Determines the tool calling behavior of the model.
When set to `none`, the model will bypass tool execution and generate a response directly.
In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
You can also specify a particular tool by `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}`.

"""


ServerlessChatStreamBodyToolChoice = TypeAliasType(
    "ServerlessChatStreamBodyToolChoice",
    Union[ServerlessChatStreamBodyToolChoiceObject, str],
)
r"""Determines the tool calling behavior of the model.
When set to `none`, the model will bypass tool execution and generate a response directly.
In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
You can also specify a particular tool by `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}`.

"""


class ServerlessChatStreamBodyTypedDict(TypedDict):
    model: str
    r"""Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models)."""
    messages: List[MessageTypedDict]
    r"""A list of messages comprising the conversation so far."""
    eos_token: NotRequired[Nullable[List[int]]]
    r"""A list of endpoint sentence tokens."""
    frequency_penalty: NotRequired[Nullable[float]]
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled, taking into account their frequency in the preceding text. This penalization diminishes the model's tendency to reproduce identical lines verbatim."""
    logit_bias: NotRequired[Nullable[ServerlessChatStreamBodyLogitBiasTypedDict]]
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""
    logprobs: NotRequired[Nullable[bool]]
    r"""Whether to return log probabilities of the output tokens or not."""
    max_tokens: NotRequired[Nullable[int]]
    r"""The maximum number of tokens to generate. For decoder-only models like GPT, the length of your input tokens plus `max_tokens` should not exceed the model's maximum length (e.g., 2048 for OpenAI GPT-3). For encoder-decoder models like T5 or BlenderBot, `max_tokens` should not exceed the model's maximum output length. This is similar to Hugging Face's [`max_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_new_tokens) argument."""
    min_tokens: NotRequired[Nullable[int]]
    r"""The minimum number of tokens to generate. Default value is 0. This is similar to Hugging Face's [`min_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.min_new_tokens) argument.

    **This field is unsupported when `tools` or `response_format` is specified.**

    """
    n: NotRequired[Nullable[int]]
    r"""The number of independently generated results for the prompt. Not supported when using beam search. Defaults to 1. This is similar to Hugging Face's [`num_return_sequences`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_return_sequences) argument."""
    parallel_tool_calls: NotRequired[Nullable[bool]]
    r"""Whether to enable parallel function calling."""
    presence_penalty: NotRequired[Nullable[float]]
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled at least once in the existing text."""
    repetition_penalty: NotRequired[Nullable[float]]
    r"""Penalizes tokens that have already appeared in the generated result (plus the input tokens for decoder-only models). Should be greater than or equal to 1.0 (1.0 means no penalty). See [keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.repetition_penalty) argument."""
    response_format: NotRequired[ResponseFormatTypedDict]
    seed: NotRequired[Nullable[List[int]]]
    r"""Seed to control random procedure. If nothing is given, random seed is used for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""
    stop: NotRequired[Nullable[List[str]]]
    r"""When one of the stop phrases appears in the generation result, the API will stop generation. The stop phrases are excluded from the result. Defaults to empty list."""
    stream: NotRequired[Nullable[bool]]
    r"""Whether to stream generation result. When set true, each token will be sent as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) once generated."""
    stream_options: NotRequired[
        Nullable[ServerlessChatStreamBodyStreamOptionsTypedDict]
    ]
    r"""Options related to stream.
    It can only be used when `stream: true`.

    """
    temperature: NotRequired[Nullable[float]]
    r"""Sampling temperature. Smaller temperature makes the generation result closer to greedy, argmax (i.e., `top_k = 1`) sampling. Defaults to 1.0. This is similar to Hugging Face's [`temperature`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.temperature) argument."""
    timeout_microseconds: NotRequired[Nullable[int]]
    r"""Request timeout. Gives the `HTTP 429 Too Many Requests` response status code. Default behavior is no timeout."""
    tool_choice: NotRequired[ServerlessChatStreamBodyToolChoiceTypedDict]
    r"""Determines the tool calling behavior of the model.
    When set to `none`, the model will bypass tool execution and generate a response directly.
    In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
    Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
    You can also specify a particular tool by `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}`.

    """
    tools: NotRequired[Nullable[List[ToolTypedDict]]]
    r"""A list of tools the model may call.
    Currently, only functions are supported as a tool.
    A maximum of 128 functions is supported.
    Use this to provide a list of functions the model may generate JSON inputs for.

    **When `tools` is specified, `min_tokens` and `response_format` fields are unsupported.**

    """
    top_k: NotRequired[Nullable[int]]
    r"""The number of highest probability tokens to keep for sampling. Numbers between 0 and the vocab size of the model (both inclusive) are allowed. The default value is 0, which means that the API does not apply top-k filtering. This is similar to Hugging Face's [`top_k`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_k) argument."""
    top_logprobs: NotRequired[Nullable[int]]
    r"""The number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to true if this parameter is used."""
    top_p: NotRequired[Nullable[float]]
    r"""Tokens comprising the top `top_p` probability mass are kept for sampling. Numbers between 0.0 (exclusive) and 1.0 (inclusive) are allowed. Defaults to 1.0. This is similar to Hugging Face's [`top_p`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_p) argument."""


class ServerlessChatStreamBody(BaseModel):
    model: str
    r"""Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models)."""

    messages: List[Message]
    r"""A list of messages comprising the conversation so far."""

    eos_token: OptionalNullable[List[int]] = UNSET
    r"""A list of endpoint sentence tokens."""

    frequency_penalty: OptionalNullable[float] = UNSET
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled, taking into account their frequency in the preceding text. This penalization diminishes the model's tendency to reproduce identical lines verbatim."""

    logit_bias: OptionalNullable[ServerlessChatStreamBodyLogitBias] = UNSET
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""

    logprobs: OptionalNullable[bool] = UNSET
    r"""Whether to return log probabilities of the output tokens or not."""

    max_tokens: OptionalNullable[int] = UNSET
    r"""The maximum number of tokens to generate. For decoder-only models like GPT, the length of your input tokens plus `max_tokens` should not exceed the model's maximum length (e.g., 2048 for OpenAI GPT-3). For encoder-decoder models like T5 or BlenderBot, `max_tokens` should not exceed the model's maximum output length. This is similar to Hugging Face's [`max_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_new_tokens) argument."""

    min_tokens: OptionalNullable[int] = 0
    r"""The minimum number of tokens to generate. Default value is 0. This is similar to Hugging Face's [`min_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.min_new_tokens) argument.

    **This field is unsupported when `tools` or `response_format` is specified.**

    """

    n: OptionalNullable[int] = 1
    r"""The number of independently generated results for the prompt. Not supported when using beam search. Defaults to 1. This is similar to Hugging Face's [`num_return_sequences`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_return_sequences) argument."""

    parallel_tool_calls: OptionalNullable[bool] = UNSET
    r"""Whether to enable parallel function calling."""

    presence_penalty: OptionalNullable[float] = UNSET
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled at least once in the existing text."""

    repetition_penalty: OptionalNullable[float] = UNSET
    r"""Penalizes tokens that have already appeared in the generated result (plus the input tokens for decoder-only models). Should be greater than or equal to 1.0 (1.0 means no penalty). See [keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.repetition_penalty) argument."""

    response_format: Optional[ResponseFormat] = None

    seed: OptionalNullable[List[int]] = UNSET
    r"""Seed to control random procedure. If nothing is given, random seed is used for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""

    stop: OptionalNullable[List[str]] = UNSET
    r"""When one of the stop phrases appears in the generation result, the API will stop generation. The stop phrases are excluded from the result. Defaults to empty list."""

    stream: OptionalNullable[bool] = True
    r"""Whether to stream generation result. When set true, each token will be sent as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) once generated."""

    stream_options: OptionalNullable[ServerlessChatStreamBodyStreamOptions] = UNSET
    r"""Options related to stream.
    It can only be used when `stream: true`.

    """

    temperature: OptionalNullable[float] = 1
    r"""Sampling temperature. Smaller temperature makes the generation result closer to greedy, argmax (i.e., `top_k = 1`) sampling. Defaults to 1.0. This is similar to Hugging Face's [`temperature`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.temperature) argument."""

    timeout_microseconds: OptionalNullable[int] = UNSET
    r"""Request timeout. Gives the `HTTP 429 Too Many Requests` response status code. Default behavior is no timeout."""

    tool_choice: Optional[ServerlessChatStreamBodyToolChoice] = None
    r"""Determines the tool calling behavior of the model.
    When set to `none`, the model will bypass tool execution and generate a response directly.
    In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
    Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
    You can also specify a particular tool by `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}`.

    """

    tools: OptionalNullable[List[Tool]] = UNSET
    r"""A list of tools the model may call.
    Currently, only functions are supported as a tool.
    A maximum of 128 functions is supported.
    Use this to provide a list of functions the model may generate JSON inputs for.

    **When `tools` is specified, `min_tokens` and `response_format` fields are unsupported.**

    """

    top_k: OptionalNullable[int] = 0
    r"""The number of highest probability tokens to keep for sampling. Numbers between 0 and the vocab size of the model (both inclusive) are allowed. The default value is 0, which means that the API does not apply top-k filtering. This is similar to Hugging Face's [`top_k`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_k) argument."""

    top_logprobs: OptionalNullable[int] = UNSET
    r"""The number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to true if this parameter is used."""

    top_p: OptionalNullable[float] = 1
    r"""Tokens comprising the top `top_p` probability mass are kept for sampling. Numbers between 0.0 (exclusive) and 1.0 (inclusive) are allowed. Defaults to 1.0. This is similar to Hugging Face's [`top_p`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_p) argument."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "eos_token",
            "frequency_penalty",
            "logit_bias",
            "logprobs",
            "max_tokens",
            "min_tokens",
            "n",
            "parallel_tool_calls",
            "presence_penalty",
            "repetition_penalty",
            "response_format",
            "seed",
            "stop",
            "stream",
            "stream_options",
            "temperature",
            "timeout_microseconds",
            "tool_choice",
            "tools",
            "top_k",
            "top_logprobs",
            "top_p",
        ]
        nullable_fields = [
            "eos_token",
            "frequency_penalty",
            "logit_bias",
            "logprobs",
            "max_tokens",
            "min_tokens",
            "n",
            "parallel_tool_calls",
            "presence_penalty",
            "repetition_penalty",
            "seed",
            "stop",
            "stream",
            "stream_options",
            "temperature",
            "timeout_microseconds",
            "tools",
            "top_k",
            "top_logprobs",
            "top_p",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
