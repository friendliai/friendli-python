"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .streamedcompletiondata import (
    StreamedCompletionData,
    StreamedCompletionDataTypedDict,
)
from friendli.types import BaseModel
from typing_extensions import TypedDict


class ServerlessCompletionsStreamSuccessTypedDict(TypedDict):
    data: StreamedCompletionDataTypedDict


class ServerlessCompletionsStreamSuccess(BaseModel):
    data: StreamedCompletionData
