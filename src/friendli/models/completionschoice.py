"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .completionslogprobs import CompletionsLogprobs, CompletionsLogprobsTypedDict
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


CompletionsChoiceFinishReason = Literal["stop", "length"]
r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits. `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length."""


class CompletionsChoiceTypedDict(TypedDict):
    index: NotRequired[int]
    r"""The index of the choice in the list of generated choices."""
    seed: NotRequired[int]
    r"""Random seed used for the generation."""
    text: NotRequired[str]
    r"""Generated text output."""
    tokens: NotRequired[List[int]]
    r"""Generated output tokens."""
    finish_reason: NotRequired[CompletionsChoiceFinishReason]
    r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits. `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length."""
    logprobs: NotRequired[Nullable[CompletionsLogprobsTypedDict]]
    r"""Log probability information for the choice."""


class CompletionsChoice(BaseModel):
    index: Optional[int] = None
    r"""The index of the choice in the list of generated choices."""

    seed: Optional[int] = None
    r"""Random seed used for the generation."""

    text: Optional[str] = None
    r"""Generated text output."""

    tokens: Optional[List[int]] = None
    r"""Generated output tokens."""

    finish_reason: Optional[CompletionsChoiceFinishReason] = None
    r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits. `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length."""

    logprobs: OptionalNullable[CompletionsLogprobs] = UNSET
    r"""Log probability information for the choice."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "index",
            "seed",
            "text",
            "tokens",
            "finish_reason",
            "logprobs",
        ]
        nullable_fields = ["logprobs"]
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
