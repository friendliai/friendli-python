"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing_extensions import TypedDict

from friendli_core.types import BaseModel

from .streamedcompletiondata import (
    StreamedCompletionData,
    StreamedCompletionDataTypedDict,
)


class ServerlessCompletionsStreamSuccessTypedDict(TypedDict):
    data: StreamedCompletionDataTypedDict


class ServerlessCompletionsStreamSuccess(BaseModel):
    data: StreamedCompletionData
