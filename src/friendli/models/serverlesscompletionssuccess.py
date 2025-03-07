"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List, Literal

import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict

from friendli.types import BaseModel
from friendli.utils import validate_const

from .completionschoice import CompletionsChoice, CompletionsChoiceTypedDict
from .usage import Usage, UsageTypedDict


class ServerlessCompletionsSuccessTypedDict(TypedDict):
    choices: List[CompletionsChoiceTypedDict]
    id: str
    r"""A unique ID of the completion."""
    model: str
    r"""The model to generate the completion. For dedicated endpoints, it returns the endpoint id"""
    usage: UsageTypedDict
    object: Literal["text_completion"]
    r"""The object type, which is always set to `text_completion`."""


class ServerlessCompletionsSuccess(BaseModel):
    choices: List[CompletionsChoice]

    id: str
    r"""A unique ID of the completion."""

    model: str
    r"""The model to generate the completion. For dedicated endpoints, it returns the endpoint id"""

    usage: Usage

    OBJECT: Annotated[
        Annotated[
            Literal["text_completion"],
            AfterValidator(validate_const("text_completion")),
        ],
        pydantic.Field(alias="object"),
    ] = "text_completion"
    r"""The object type, which is always set to `text_completion`."""
