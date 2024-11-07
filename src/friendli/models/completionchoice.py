"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class CompletionChoiceTypedDict(TypedDict):
    index: int
    r"""The index of the choice in the list of generated choices."""
    seed: int
    r"""Random seed used for the generation."""
    text: str
    r"""Generated text output."""
    tokens: List[int]
    r"""Generated output tokens."""


class CompletionChoice(BaseModel):
    index: int
    r"""The index of the choice in the list of generated choices."""

    seed: int
    r"""Random seed used for the generation."""

    text: str
    r"""Generated text output."""

    tokens: List[int]
    r"""Generated output tokens."""
