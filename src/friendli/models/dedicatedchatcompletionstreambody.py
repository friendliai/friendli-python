"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import model_serializer
from typing_extensions import NotRequired, TypeAliasType, TypedDict

from friendli.types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable

from .chatcompletebodytoolchoice import (
    ChatCompleteBodyToolChoice,
    ChatCompleteBodyToolChoiceTypedDict,
)
from .message import Message, MessageTypedDict
from .responseformat import ResponseFormat, ResponseFormatTypedDict
from .streamoptions import StreamOptions, StreamOptionsTypedDict
from .tool import Tool, ToolTypedDict


class DedicatedChatCompletionStreamBodyLogitBiasTypedDict(TypedDict):
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""


class DedicatedChatCompletionStreamBodyLogitBias(BaseModel):
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""


DedicatedChatCompletionStreamBodySeedTypedDict = TypeAliasType(
    "DedicatedChatCompletionStreamBodySeedTypedDict", Union[List[int], int]
)
r"""Seed to control random procedure. If nothing is given, random seed is used for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""


DedicatedChatCompletionStreamBodySeed = TypeAliasType(
    "DedicatedChatCompletionStreamBodySeed", Union[List[int], int]
)
r"""Seed to control random procedure. If nothing is given, random seed is used for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""


DedicatedChatCompletionStreamBodyToolChoiceTypedDict = TypeAliasType(
    "DedicatedChatCompletionStreamBodyToolChoiceTypedDict",
    Union[ChatCompleteBodyToolChoiceTypedDict, str],
)
r"""Determines the tool calling behavior of the model.
When set to `none`, the model will bypass tool execution and generate a response directly.
In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
You can also specify a particular tool by `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}`.

"""


DedicatedChatCompletionStreamBodyToolChoice = TypeAliasType(
    "DedicatedChatCompletionStreamBodyToolChoice",
    Union[ChatCompleteBodyToolChoice, str],
)
r"""Determines the tool calling behavior of the model.
When set to `none`, the model will bypass tool execution and generate a response directly.
In `auto` mode (the default), the model dynamically decides whether to call a tool or respond with a message.
Alternatively, setting `required` ensures that the model invokes at least one tool before responding to the user.
You can also specify a particular tool by `{\"type\": \"function\", \"function\": {\"name\": \"my_function\"}}`.

"""


class DedicatedChatCompletionStreamBodyTypedDict(TypedDict):
    messages: List[MessageTypedDict]
    r"""A list of messages comprising the conversation so far."""
    model: str
    r"""ID of target endpoint. If you want to send request to specific adapter, use the format \"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\". Otherwise, you can just use \"YOUR_ENDPOINT_ID\" alone."""
    eos_token: NotRequired[Nullable[List[int]]]
    r"""A list of endpoint sentence tokens."""
    frequency_penalty: NotRequired[Nullable[float]]
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled, taking into account their frequency in the preceding text. This penalization diminishes the model's tendency to reproduce identical lines verbatim."""
    logit_bias: NotRequired[
        Nullable[DedicatedChatCompletionStreamBodyLogitBiasTypedDict]
    ]
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""
    logprobs: NotRequired[Nullable[bool]]
    r"""Whether to return log probabilities of the output tokens or not."""
    max_tokens: NotRequired[Nullable[int]]
    r"""The maximum number of tokens to generate. For decoder-only models like GPT, the length of your input tokens plus `max_tokens` should not exceed the model's maximum length (e.g., 2048 for OpenAI GPT-3). For encoder-decoder models like T5 or BlenderBot, `max_tokens` should not exceed the model's maximum output length. This is similar to Hugging Face's [`max_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_new_tokens) argument."""
    min_p: NotRequired[Nullable[float]]
    r"""A scaling factor used to determine the minimum token probability threshold. This threshold is calculated as `min_p` multiplied by the probability of the most likely token. Tokens with probabilities below this scaled threshold are excluded from sampling. Values range from 0.0 (inclusive) to 1.0 (inclusive). Higher values result in stricter filtering, while lower values allow for greater diversity. The default value of 0.0 disables filtering, allowing all tokens to be considered for sampling."""
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
    r"""Penalizes tokens that have already appeared in the generated result (plus the input tokens for decoder-only models). Should be positive value (1.0 means no penalty). See [keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.repetition_penalty) argument."""
    response_format: NotRequired[Nullable[ResponseFormatTypedDict]]
    r"""The enforced format of the model's output.

    Note that the content of the output message may be truncated if it exceeds the `max_tokens`. You can check this by verifying that the `finish_reason` of the output message is `length`.

    For more detailed information, please refer [here](https://friendli.ai/docs/guides/serverless_endpoints/structured-outputs).

    ***Important***
    You must explicitly instruct the model to produce the desired output format using a system prompt or user message (e.g., `You are an API generating a valid JSON as output.`).
    Otherwise, the model may result in an unending stream of whitespace or other characters.

    **This field is unsupported when `tools` is specified.**
    **When `response_format` is specified, `min_tokens` field is unsupported.**


    """
    seed: NotRequired[Nullable[DedicatedChatCompletionStreamBodySeedTypedDict]]
    r"""Seed to control random procedure. If nothing is given, random seed is used for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""
    stop: NotRequired[Nullable[List[str]]]
    r"""When one of the stop phrases appears in the generation result, the API will stop generation. The stop phrases are excluded from the result. Defaults to empty list."""
    stream: NotRequired[Nullable[bool]]
    r"""Whether to stream generation result. When set true, each token will be sent as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) once generated."""
    stream_options: NotRequired[Nullable[StreamOptionsTypedDict]]
    r"""Options related to stream.
    It can only be used when `stream: true`.

    """
    temperature: NotRequired[Nullable[float]]
    r"""Sampling temperature. Smaller temperature makes the generation result closer to greedy, argmax (i.e., `top_k = 1`) sampling. Defaults to 1.0. This is similar to Hugging Face's [`temperature`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.temperature) argument."""
    tool_choice: NotRequired[DedicatedChatCompletionStreamBodyToolChoiceTypedDict]
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
    r"""Limits sampling to the top k tokens with the highest probabilities. Values range from 0 (no filtering) to the model's vocabulary size (inclusive). The default value of 0 applies no filtering, allowing all tokens."""
    top_logprobs: NotRequired[Nullable[int]]
    r"""The number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to true if this parameter is used."""
    top_p: NotRequired[Nullable[float]]
    r"""Keeps only the smallest set of tokens whose cumulative probabilities reach `top_p` or higher. Values range from 0.0 (exclusive) to 1.0 (inclusive). The default value of 1.0 includes all tokens, allowing maximum diversity."""


class DedicatedChatCompletionStreamBody(BaseModel):
    messages: List[Message]
    r"""A list of messages comprising the conversation so far."""

    model: str
    r"""ID of target endpoint. If you want to send request to specific adapter, use the format \"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\". Otherwise, you can just use \"YOUR_ENDPOINT_ID\" alone."""

    eos_token: OptionalNullable[List[int]] = UNSET
    r"""A list of endpoint sentence tokens."""

    frequency_penalty: OptionalNullable[float] = UNSET
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled, taking into account their frequency in the preceding text. This penalization diminishes the model's tendency to reproduce identical lines verbatim."""

    logit_bias: OptionalNullable[DedicatedChatCompletionStreamBodyLogitBias] = UNSET
    r"""Accepts a JSON object that maps tokens to an associated bias value. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model."""

    logprobs: OptionalNullable[bool] = UNSET
    r"""Whether to return log probabilities of the output tokens or not."""

    max_tokens: OptionalNullable[int] = UNSET
    r"""The maximum number of tokens to generate. For decoder-only models like GPT, the length of your input tokens plus `max_tokens` should not exceed the model's maximum length (e.g., 2048 for OpenAI GPT-3). For encoder-decoder models like T5 or BlenderBot, `max_tokens` should not exceed the model's maximum output length. This is similar to Hugging Face's [`max_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_new_tokens) argument."""

    min_p: OptionalNullable[float] = UNSET
    r"""A scaling factor used to determine the minimum token probability threshold. This threshold is calculated as `min_p` multiplied by the probability of the most likely token. Tokens with probabilities below this scaled threshold are excluded from sampling. Values range from 0.0 (inclusive) to 1.0 (inclusive). Higher values result in stricter filtering, while lower values allow for greater diversity. The default value of 0.0 disables filtering, allowing all tokens to be considered for sampling."""

    min_tokens: OptionalNullable[int] = UNSET
    r"""The minimum number of tokens to generate. Default value is 0. This is similar to Hugging Face's [`min_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.min_new_tokens) argument.

    **This field is unsupported when `tools` or `response_format` is specified.**

    """

    n: OptionalNullable[int] = UNSET
    r"""The number of independently generated results for the prompt. Not supported when using beam search. Defaults to 1. This is similar to Hugging Face's [`num_return_sequences`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_return_sequences) argument."""

    parallel_tool_calls: OptionalNullable[bool] = UNSET
    r"""Whether to enable parallel function calling."""

    presence_penalty: OptionalNullable[float] = UNSET
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled at least once in the existing text."""

    repetition_penalty: OptionalNullable[float] = UNSET
    r"""Penalizes tokens that have already appeared in the generated result (plus the input tokens for decoder-only models). Should be positive value (1.0 means no penalty). See [keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.repetition_penalty) argument."""

    response_format: OptionalNullable[ResponseFormat] = UNSET
    r"""The enforced format of the model's output.

    Note that the content of the output message may be truncated if it exceeds the `max_tokens`. You can check this by verifying that the `finish_reason` of the output message is `length`.

    For more detailed information, please refer [here](https://friendli.ai/docs/guides/serverless_endpoints/structured-outputs).

    ***Important***
    You must explicitly instruct the model to produce the desired output format using a system prompt or user message (e.g., `You are an API generating a valid JSON as output.`).
    Otherwise, the model may result in an unending stream of whitespace or other characters.

    **This field is unsupported when `tools` is specified.**
    **When `response_format` is specified, `min_tokens` field is unsupported.**


    """

    seed: OptionalNullable[DedicatedChatCompletionStreamBodySeed] = UNSET
    r"""Seed to control random procedure. If nothing is given, random seed is used for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""

    stop: OptionalNullable[List[str]] = UNSET
    r"""When one of the stop phrases appears in the generation result, the API will stop generation. The stop phrases are excluded from the result. Defaults to empty list."""

    stream: OptionalNullable[bool] = True
    r"""Whether to stream generation result. When set true, each token will be sent as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) once generated."""

    stream_options: OptionalNullable[StreamOptions] = UNSET
    r"""Options related to stream.
    It can only be used when `stream: true`.

    """

    temperature: OptionalNullable[float] = UNSET
    r"""Sampling temperature. Smaller temperature makes the generation result closer to greedy, argmax (i.e., `top_k = 1`) sampling. Defaults to 1.0. This is similar to Hugging Face's [`temperature`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.temperature) argument."""

    tool_choice: Optional[DedicatedChatCompletionStreamBodyToolChoice] = None
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

    top_k: OptionalNullable[int] = UNSET
    r"""Limits sampling to the top k tokens with the highest probabilities. Values range from 0 (no filtering) to the model's vocabulary size (inclusive). The default value of 0 applies no filtering, allowing all tokens."""

    top_logprobs: OptionalNullable[int] = UNSET
    r"""The number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to true if this parameter is used."""

    top_p: OptionalNullable[float] = UNSET
    r"""Keeps only the smallest set of tokens whose cumulative probabilities reach `top_p` or higher. Values range from 0.0 (exclusive) to 1.0 (inclusive). The default value of 1.0 includes all tokens, allowing maximum diversity."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "eos_token",
            "frequency_penalty",
            "logit_bias",
            "logprobs",
            "max_tokens",
            "min_p",
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
            "min_p",
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
