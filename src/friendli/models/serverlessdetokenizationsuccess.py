"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing_extensions import TypedDict


class ServerlessDetokenizationSuccessTypedDict(TypedDict):
    text: str
    r"""Detokenized text output."""


class ServerlessDetokenizationSuccess(BaseModel):
    text: str
    r"""Detokenized text output."""
