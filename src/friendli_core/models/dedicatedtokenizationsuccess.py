"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from friendli_core.types import BaseModel


class DedicatedTokenizationSuccessTypedDict(TypedDict):
    tokens: List[int]
    r"""A list of token IDs."""


class DedicatedTokenizationSuccess(BaseModel):
    tokens: List[int]
    r"""A list of token IDs."""
