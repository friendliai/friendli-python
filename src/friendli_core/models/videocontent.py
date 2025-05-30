"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Literal

import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict

from friendli_core.types import BaseModel
from friendli_core.utils import validate_const

from .videodata import VideoData, VideoDataTypedDict


class VideoContentTypedDict(TypedDict):
    video_url: VideoDataTypedDict
    type: Literal["video_url"]
    r"""The type of the message content."""


class VideoContent(BaseModel):
    video_url: VideoData

    TYPE: Annotated[
        Annotated[Literal["video_url"], AfterValidator(validate_const("video_url"))],
        pydantic.Field(alias="type"),
    ] = "video_url"
    r"""The type of the message content."""
