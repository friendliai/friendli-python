"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Literal

import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict

from friendli_core.types import BaseModel
from friendli_core.utils import validate_const

from .toolstatusdata import ToolStatusData, ToolStatusDataTypedDict


class StreamedToolAssistedChatToolStatusTypedDict(TypedDict):
    data: ToolStatusDataTypedDict
    event: Literal["tool_status"]


class StreamedToolAssistedChatToolStatus(BaseModel):
    data: ToolStatusData

    EVENT: Annotated[
        Annotated[
            Literal["tool_status"], AfterValidator(validate_const("tool_status"))
        ],
        pydantic.Field(alias="event"),
    ] = "tool_status"
