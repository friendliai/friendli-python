"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .completionscompletebody import (
    CompletionsCompleteBody,
    CompletionsCompleteBodyTypedDict,
)
from friendli.types import BaseModel
from friendli.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ServerlessCompletionsCompleteRequestTypedDict(TypedDict):
    completions_complete_body: CompletionsCompleteBodyTypedDict
    x_friendli_team: NotRequired[str]
    r"""ID of team to run requests as (optional parameter)."""


class ServerlessCompletionsCompleteRequest(BaseModel):
    completions_complete_body: Annotated[
        CompletionsCompleteBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_friendli_team: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Friendli-Team"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of team to run requests as (optional parameter)."""