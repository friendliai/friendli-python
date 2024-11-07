"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .completionchoice import CompletionChoice, CompletionChoiceTypedDict
from .usage import Usage, UsageTypedDict
from friendli.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class CompletionResponseTypedDict(TypedDict):
    choices: List[CompletionChoiceTypedDict]
    usage: UsageTypedDict


class CompletionResponse(BaseModel):
    choices: List[CompletionChoice]

    usage: Usage
