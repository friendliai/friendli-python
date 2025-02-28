"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List, Literal

import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict

from friendli.types import BaseModel
from friendli.utils import validate_const

from .chatchoice import ChatChoice, ChatChoiceTypedDict
from .chatusage import ChatUsage, ChatUsageTypedDict


class ServerlessChatCompleteSuccessTypedDict(TypedDict):
    choices: List[ChatChoiceTypedDict]
    created: int
    r"""The Unix timestamp (in seconds) for when the generation completed."""
    id: str
    r"""A unique ID of the chat completion."""
    model: str
    r"""The model to generate the completion. For dedicated endpoints, it returns the endpoint id"""
    usage: ChatUsageTypedDict
    object: Literal["chat.completion"]
    r"""The object type, which is always set to `chat.completion`."""


class ServerlessChatCompleteSuccess(BaseModel):
    choices: List[ChatChoice]

    created: int
    r"""The Unix timestamp (in seconds) for when the generation completed."""

    id: str
    r"""A unique ID of the chat completion."""

    model: str
    r"""The model to generate the completion. For dedicated endpoints, it returns the endpoint id"""

    usage: ChatUsage

    OBJECT: Annotated[
        Annotated[
            Literal["chat.completion"],
            AfterValidator(validate_const("chat.completion")),
        ],
        pydantic.Field(alias="object"),
    ] = "chat.completion"
    r"""The object type, which is always set to `chat.completion`."""
