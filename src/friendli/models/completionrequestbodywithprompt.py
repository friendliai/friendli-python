"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .textresponseformat import TextResponseFormat, TextResponseFormatTypedDict
from .tokensequence import TokenSequence, TokenSequenceTypedDict
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class CompletionRequestBodyWithPromptTypedDict(TypedDict):
    prompt: str
    r"""The prompt (i.e., input text) to generate completion for. Either `prompt` or `tokens` field is required."""
    model: str
    r"""Code of the model to use. See [available model list](https://docs.friendli.ai/guides/serverless_endpoints/pricing#text-generation-models)."""
    bad_word_tokens: NotRequired[Nullable[List[TokenSequenceTypedDict]]]
    r"""Same as the above `bad_words` field, but receives token sequences instead of text phrases. This is similar to Hugging Face's [`bad_word_ids`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.bad_words_ids) argument."""
    bad_words: NotRequired[Nullable[List[str]]]
    r"""Text phrases that should not be generated.
    For a bad word phrase that contains N tokens, if the first N-1 tokens appears at the last of the generated result, the logit for the last token of the phrase is set to -inf.
    Before checking whether a bard word is included in the result, the word is converted into tokens.
    We recommend using `bad_word_tokens` because it is clearer.
    For example, after tokenization, phrases \"clear\" and \" clear\" can result in different token sequences due to the prepended space character.
    Defaults to empty list.

    """
    beam_compat_no_post_normalization: NotRequired[Nullable[bool]]
    beam_compat_pre_normalization: NotRequired[Nullable[bool]]
    beam_search_type: NotRequired[Nullable[str]]
    r"""One of `DETERMINISTIC`, `NAIVE_SAMPLING`, and `STOCHASTIC`. Which beam search type to use. `DETERMINISTIC` means the standard, deterministic beam search, which is similar to Hugging Face's [`beam_search`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationMixin.beam_search). Argmuents for controlling random sampling such as `top_k` and `top_p` are not allowed for this option. `NAIVE_SAMPLING` is similar to Hugging Face's [`beam_sample`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationMixin.beam_sample). `STOCHASTIC` means stochastic beam search (more details in [Kool et al. (2019)](https://proceedings.mlr.press/v97/kool19a.html)). This option is ignored if `num_beams` is not provided. Defaults to `DETERMINISTIC`."""
    early_stopping: NotRequired[Nullable[bool]]
    r"""Whether to stop the beam search when at least `num_beams` beams are finished with the EOS token. Only allowed for beam search. Defaults to false. This is similar to Hugging Face's [`early_stopping`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.early_stopping) argument."""
    embedding_to_replace: NotRequired[Nullable[List[float]]]
    r"""A list of flattened embedding vectors used for replacing the tokens at the specified indices provided via `token_index_to_replace`."""
    encoder_no_repeat_ngram: NotRequired[Nullable[int]]
    r"""If this exceeds 1, every ngram of that size occurring in the input token sequence cannot appear in the generated result. 1 means that this mechanism is disabled (i.e., you cannot prevent 1-gram from being generated repeatedly). Only allowed for encoder-decoder models. Defaults to 1. This is similar to Hugging Face's [`encoder_no_repeat_ngram_size`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.encoder_no_repeat_ngram_size) argument."""
    encoder_repetition_penalty: NotRequired[Nullable[float]]
    r"""Penalizes tokens that have already appeared in the input tokens. Should be greater than or equal to 1.0. 1.0 means no penalty. Only allowed for encoder-decoder models. See [Keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`encoder_repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.encoder_repetition_penalty) argument."""
    eos_token: NotRequired[Nullable[List[int]]]
    r"""A list of endpoint sentence tokens."""
    forced_output_tokens: NotRequired[Nullable[List[int]]]
    r"""A token sequence that is enforced as a generation output. This option can be used when evaluating the model for the datasets with multi-choice problems (e.g., [HellaSwag](https://huggingface.co/datasets/hellaswag), [MMLU](https://huggingface.co/datasets/cais/mmlu)). Use this option with `include_output_logprobs` to get logprobs for the evaluation."""
    frequency_penalty: NotRequired[Nullable[float]]
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled, taking into account their frequency in the preceding text. This penalization diminishes the model's tendency to reproduce identical lines verbatim."""
    include_output_logits: NotRequired[Nullable[bool]]
    r"""Whether to include the output logits to the generation output."""
    include_output_logprobs: NotRequired[Nullable[bool]]
    r"""Whether to include the output logprobs to the generation output."""
    length_penalty: NotRequired[Nullable[float]]
    r"""Coefficient for exponential length penalty that is used with beam search. Only allowed for beam search. Defaults to 1.0. This is similar to Hugging Face's [`length_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.length_penalty) argument."""
    max_tokens: NotRequired[Nullable[int]]
    r"""The maximum number of tokens to generate. For decoder-only models like GPT, the length of your input tokens plus `max_tokens` should not exceed the model's maximum length (e.g., 2048 for OpenAI GPT-3). For encoder-decoder models like T5 or BlenderBot, `max_tokens` should not exceed the model's maximum output length. This is similar to Hugging Face's [`max_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_new_tokens) argument."""
    max_total_tokens: NotRequired[Nullable[int]]
    r"""The maximum number of tokens including both the generated result and the input tokens. Only allowed for decoder-only models. Only one argument between `max_tokens` and `max_total_tokens` is allowed. Default value is the model's maximum length. This is similar to Hugging Face's [`max_length`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_length) argument."""
    min_tokens: NotRequired[Nullable[int]]
    r"""The minimum number of tokens to generate. Default value is 0. This is similar to Hugging Face's [`min_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.min_new_tokens) argument."""
    min_total_tokens: NotRequired[Nullable[int]]
    r"""The minimum number of tokens including both the generated result and the input tokens. Only allowed for decoder-only models. Only one argument between `min_tokens` and `min_total_tokens` is allowed. This is similar to Hugging Face's [`min_length`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.min_length) argument."""
    n: NotRequired[Nullable[int]]
    r"""The number of independently generated results for the prompt. Not supported when using beam search. Defaults to 1. This is similar to Hugging Face's [`num_return_sequences`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_return_sequences) argument."""
    no_repeat_ngram: NotRequired[Nullable[int]]
    r"""If this exceeds 1, every ngram of that size can only occur once among the generated result (plus the input tokens for decoder-only models). 1 means that this mechanism is disabled (i.e., you cannot prevent 1-gram from being generated repeatedly). Defaults to 1. This is similar to Hugging Face's [`no_repeat_ngram_size`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.no_repeat_ngram_size) argument."""
    num_beams: NotRequired[Nullable[int]]
    r"""Number of beams for beam search. Numbers between 1 and 31 (both inclusive) are allowed. Default behavior is no beam search. This is similar to Hugging Face's [`num_beams`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_beams) argument."""
    presence_penalty: NotRequired[Nullable[float]]
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled at least once in the existing text."""
    repetition_penalty: NotRequired[Nullable[float]]
    r"""Penalizes tokens that have already appeared in the generated result (plus the input tokens for decoder-only models). Should be greater than or equal to 1.0 (1.0 means no penalty). See [keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.repetition_penalty) argument."""
    response_format: NotRequired[Nullable[TextResponseFormatTypedDict]]
    r"""The enforced format of the model's output.

    Note that the content of the output message may be truncated if it exceeds the `max_tokens`.
    You can check this by verifying that the `finish_reason` of the output message is `length`.

    ***Important***
    You must explicitly instruct the model to produce the desired output format using a system prompt or user message (e.g., `You are an API generating a valid JSON as output.`).
    Otherwise, the model may result in an unending stream of whitespace or other characters.

    """
    seed: NotRequired[Nullable[List[int]]]
    r"""Seed to control random procedure. If nothing is given, the API generate the seed randomly, use it for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""
    stop: NotRequired[Nullable[List[str]]]
    r"""When one of the stop phrases appears in the generation result, the API will stop generation.
    The stop phrases are excluded from the result.
    This option is incompatible with beam search (specified by `num_beams`); use `stop_tokens` for that case instead.
    Defaults to empty list.

    """
    stop_tokens: NotRequired[Nullable[List[TokenSequenceTypedDict]]]
    r"""Stop generating further tokens when generated token corresponds to any of the tokens in the sequence.
    If beam search is enabled, all of the active beams should contain the stop token to terminate generation.

    """
    stream: NotRequired[Nullable[bool]]
    r"""Whether to stream generation result. When set true, each token will be sent as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) once generated. Not supported when using beam search."""
    temperature: NotRequired[Nullable[float]]
    r"""Sampling temperature. Smaller temperature makes the generation result closer to greedy, argmax (i.e., `top_k = 1`) sampling. Defaults to 1.0. This is similar to Hugging Face's [`temperature`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.temperature) argument."""
    timeout_microseconds: NotRequired[Nullable[int]]
    r"""Request timeout. Gives the `HTTP 429 Too Many Requests` response status code. Default behavior is no timeout."""
    token_index_to_replace: NotRequired[Nullable[List[int]]]
    r"""A list of token indices where to replace the embeddings of input tokens provided via either `tokens` or `prompt`."""
    top_k: NotRequired[Nullable[int]]
    r"""The number of highest probability tokens to keep for sampling. Numbers between 0 and the vocab size of the model (both inclusive) are allowed. The default value is 0, which means that the API does not apply top-k filtering. This is similar to Hugging Face's [`top_k`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_k) argument."""
    top_p: NotRequired[Nullable[float]]
    r"""Tokens comprising the top `top_p` probability mass are kept for sampling. Numbers between 0.0 (exclusive) and 1.0 (inclusive) are allowed. Defaults to 1.0. This is similar to Hugging Face's [`top_p`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_p) argument."""


class CompletionRequestBodyWithPrompt(BaseModel):
    prompt: str
    r"""The prompt (i.e., input text) to generate completion for. Either `prompt` or `tokens` field is required."""

    model: str
    r"""Code of the model to use. See [available model list](https://docs.friendli.ai/guides/serverless_endpoints/pricing#text-generation-models)."""

    bad_word_tokens: OptionalNullable[List[TokenSequence]] = UNSET
    r"""Same as the above `bad_words` field, but receives token sequences instead of text phrases. This is similar to Hugging Face's [`bad_word_ids`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.bad_words_ids) argument."""

    bad_words: OptionalNullable[List[str]] = UNSET
    r"""Text phrases that should not be generated.
    For a bad word phrase that contains N tokens, if the first N-1 tokens appears at the last of the generated result, the logit for the last token of the phrase is set to -inf.
    Before checking whether a bard word is included in the result, the word is converted into tokens.
    We recommend using `bad_word_tokens` because it is clearer.
    For example, after tokenization, phrases \"clear\" and \" clear\" can result in different token sequences due to the prepended space character.
    Defaults to empty list.

    """

    beam_compat_no_post_normalization: OptionalNullable[bool] = UNSET

    beam_compat_pre_normalization: OptionalNullable[bool] = UNSET

    beam_search_type: OptionalNullable[str] = "DETERMINISTIC"
    r"""One of `DETERMINISTIC`, `NAIVE_SAMPLING`, and `STOCHASTIC`. Which beam search type to use. `DETERMINISTIC` means the standard, deterministic beam search, which is similar to Hugging Face's [`beam_search`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationMixin.beam_search). Argmuents for controlling random sampling such as `top_k` and `top_p` are not allowed for this option. `NAIVE_SAMPLING` is similar to Hugging Face's [`beam_sample`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationMixin.beam_sample). `STOCHASTIC` means stochastic beam search (more details in [Kool et al. (2019)](https://proceedings.mlr.press/v97/kool19a.html)). This option is ignored if `num_beams` is not provided. Defaults to `DETERMINISTIC`."""

    early_stopping: OptionalNullable[bool] = False
    r"""Whether to stop the beam search when at least `num_beams` beams are finished with the EOS token. Only allowed for beam search. Defaults to false. This is similar to Hugging Face's [`early_stopping`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.early_stopping) argument."""

    embedding_to_replace: OptionalNullable[List[float]] = UNSET
    r"""A list of flattened embedding vectors used for replacing the tokens at the specified indices provided via `token_index_to_replace`."""

    encoder_no_repeat_ngram: OptionalNullable[int] = 1
    r"""If this exceeds 1, every ngram of that size occurring in the input token sequence cannot appear in the generated result. 1 means that this mechanism is disabled (i.e., you cannot prevent 1-gram from being generated repeatedly). Only allowed for encoder-decoder models. Defaults to 1. This is similar to Hugging Face's [`encoder_no_repeat_ngram_size`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.encoder_no_repeat_ngram_size) argument."""

    encoder_repetition_penalty: OptionalNullable[float] = UNSET
    r"""Penalizes tokens that have already appeared in the input tokens. Should be greater than or equal to 1.0. 1.0 means no penalty. Only allowed for encoder-decoder models. See [Keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`encoder_repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.encoder_repetition_penalty) argument."""

    eos_token: OptionalNullable[List[int]] = UNSET
    r"""A list of endpoint sentence tokens."""

    forced_output_tokens: OptionalNullable[List[int]] = UNSET
    r"""A token sequence that is enforced as a generation output. This option can be used when evaluating the model for the datasets with multi-choice problems (e.g., [HellaSwag](https://huggingface.co/datasets/hellaswag), [MMLU](https://huggingface.co/datasets/cais/mmlu)). Use this option with `include_output_logprobs` to get logprobs for the evaluation."""

    frequency_penalty: OptionalNullable[float] = UNSET
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled, taking into account their frequency in the preceding text. This penalization diminishes the model's tendency to reproduce identical lines verbatim."""

    include_output_logits: OptionalNullable[bool] = UNSET
    r"""Whether to include the output logits to the generation output."""

    include_output_logprobs: OptionalNullable[bool] = UNSET
    r"""Whether to include the output logprobs to the generation output."""

    length_penalty: OptionalNullable[float] = UNSET
    r"""Coefficient for exponential length penalty that is used with beam search. Only allowed for beam search. Defaults to 1.0. This is similar to Hugging Face's [`length_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.length_penalty) argument."""

    max_tokens: OptionalNullable[int] = UNSET
    r"""The maximum number of tokens to generate. For decoder-only models like GPT, the length of your input tokens plus `max_tokens` should not exceed the model's maximum length (e.g., 2048 for OpenAI GPT-3). For encoder-decoder models like T5 or BlenderBot, `max_tokens` should not exceed the model's maximum output length. This is similar to Hugging Face's [`max_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_new_tokens) argument."""

    max_total_tokens: OptionalNullable[int] = UNSET
    r"""The maximum number of tokens including both the generated result and the input tokens. Only allowed for decoder-only models. Only one argument between `max_tokens` and `max_total_tokens` is allowed. Default value is the model's maximum length. This is similar to Hugging Face's [`max_length`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.max_length) argument."""

    min_tokens: OptionalNullable[int] = 0
    r"""The minimum number of tokens to generate. Default value is 0. This is similar to Hugging Face's [`min_new_tokens`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.min_new_tokens) argument."""

    min_total_tokens: OptionalNullable[int] = UNSET
    r"""The minimum number of tokens including both the generated result and the input tokens. Only allowed for decoder-only models. Only one argument between `min_tokens` and `min_total_tokens` is allowed. This is similar to Hugging Face's [`min_length`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.min_length) argument."""

    n: OptionalNullable[int] = 1
    r"""The number of independently generated results for the prompt. Not supported when using beam search. Defaults to 1. This is similar to Hugging Face's [`num_return_sequences`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_return_sequences) argument."""

    no_repeat_ngram: OptionalNullable[int] = 1
    r"""If this exceeds 1, every ngram of that size can only occur once among the generated result (plus the input tokens for decoder-only models). 1 means that this mechanism is disabled (i.e., you cannot prevent 1-gram from being generated repeatedly). Defaults to 1. This is similar to Hugging Face's [`no_repeat_ngram_size`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.no_repeat_ngram_size) argument."""

    num_beams: OptionalNullable[int] = UNSET
    r"""Number of beams for beam search. Numbers between 1 and 31 (both inclusive) are allowed. Default behavior is no beam search. This is similar to Hugging Face's [`num_beams`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.num_beams) argument."""

    presence_penalty: OptionalNullable[float] = UNSET
    r"""Number between -2.0 and 2.0. Positive values penalizes tokens that have been sampled at least once in the existing text."""

    repetition_penalty: OptionalNullable[float] = UNSET
    r"""Penalizes tokens that have already appeared in the generated result (plus the input tokens for decoder-only models). Should be greater than or equal to 1.0 (1.0 means no penalty). See [keskar et al., 2019](https://arxiv.org/abs/1909.05858) for more details. This is similar to Hugging Face's [`repetition_penalty`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.repetition_penalty) argument."""

    response_format: OptionalNullable[TextResponseFormat] = UNSET
    r"""The enforced format of the model's output.

    Note that the content of the output message may be truncated if it exceeds the `max_tokens`.
    You can check this by verifying that the `finish_reason` of the output message is `length`.

    ***Important***
    You must explicitly instruct the model to produce the desired output format using a system prompt or user message (e.g., `You are an API generating a valid JSON as output.`).
    Otherwise, the model may result in an unending stream of whitespace or other characters.

    """

    seed: OptionalNullable[List[int]] = UNSET
    r"""Seed to control random procedure. If nothing is given, the API generate the seed randomly, use it for sampling, and return the seed along with the generated result. When using the `n` argument, you can pass a list of seed values to control all of the independent generations."""

    stop: OptionalNullable[List[str]] = UNSET
    r"""When one of the stop phrases appears in the generation result, the API will stop generation.
    The stop phrases are excluded from the result.
    This option is incompatible with beam search (specified by `num_beams`); use `stop_tokens` for that case instead.
    Defaults to empty list.

    """

    stop_tokens: OptionalNullable[List[TokenSequence]] = UNSET
    r"""Stop generating further tokens when generated token corresponds to any of the tokens in the sequence.
    If beam search is enabled, all of the active beams should contain the stop token to terminate generation.

    """

    stream: OptionalNullable[bool] = UNSET
    r"""Whether to stream generation result. When set true, each token will be sent as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) once generated. Not supported when using beam search."""

    temperature: OptionalNullable[float] = 1
    r"""Sampling temperature. Smaller temperature makes the generation result closer to greedy, argmax (i.e., `top_k = 1`) sampling. Defaults to 1.0. This is similar to Hugging Face's [`temperature`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.generationconfig.temperature) argument."""

    timeout_microseconds: OptionalNullable[int] = UNSET
    r"""Request timeout. Gives the `HTTP 429 Too Many Requests` response status code. Default behavior is no timeout."""

    token_index_to_replace: OptionalNullable[List[int]] = UNSET
    r"""A list of token indices where to replace the embeddings of input tokens provided via either `tokens` or `prompt`."""

    top_k: OptionalNullable[int] = 0
    r"""The number of highest probability tokens to keep for sampling. Numbers between 0 and the vocab size of the model (both inclusive) are allowed. The default value is 0, which means that the API does not apply top-k filtering. This is similar to Hugging Face's [`top_k`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_k) argument."""

    top_p: OptionalNullable[float] = 1
    r"""Tokens comprising the top `top_p` probability mass are kept for sampling. Numbers between 0.0 (exclusive) and 1.0 (inclusive) are allowed. Defaults to 1.0. This is similar to Hugging Face's [`top_p`](https://huggingface.co/docs/transformers/v4.26.0/en/main_classes/text_generation#transformers.GenerationConfig.top_p) argument."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "bad_word_tokens",
            "bad_words",
            "beam_compat_no_post_normalization",
            "beam_compat_pre_normalization",
            "beam_search_type",
            "early_stopping",
            "embedding_to_replace",
            "encoder_no_repeat_ngram",
            "encoder_repetition_penalty",
            "eos_token",
            "forced_output_tokens",
            "frequency_penalty",
            "include_output_logits",
            "include_output_logprobs",
            "length_penalty",
            "max_tokens",
            "max_total_tokens",
            "min_tokens",
            "min_total_tokens",
            "n",
            "no_repeat_ngram",
            "num_beams",
            "presence_penalty",
            "repetition_penalty",
            "response_format",
            "seed",
            "stop",
            "stop_tokens",
            "stream",
            "temperature",
            "timeout_microseconds",
            "token_index_to_replace",
            "top_k",
            "top_p",
        ]
        nullable_fields = [
            "bad_word_tokens",
            "bad_words",
            "beam_compat_no_post_normalization",
            "beam_compat_pre_normalization",
            "beam_search_type",
            "early_stopping",
            "embedding_to_replace",
            "encoder_no_repeat_ngram",
            "encoder_repetition_penalty",
            "eos_token",
            "forced_output_tokens",
            "frequency_penalty",
            "include_output_logits",
            "include_output_logprobs",
            "length_penalty",
            "max_tokens",
            "max_total_tokens",
            "min_tokens",
            "min_total_tokens",
            "n",
            "no_repeat_ngram",
            "num_beams",
            "presence_penalty",
            "repetition_penalty",
            "response_format",
            "seed",
            "stop",
            "stop_tokens",
            "stream",
            "temperature",
            "timeout_microseconds",
            "token_index_to_replace",
            "top_k",
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
