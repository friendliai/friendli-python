"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatchoice import ChatChoice, ChatChoiceTypedDict
from .usage import Usage, UsageTypedDict
from friendli.types import BaseModel
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


Object = Literal["chat.completion"]
r"""The object type, which is always set to `chat.completion`."""


class ChatResultTypedDict(TypedDict):
    r"""Successfully generated a chat response."""

    id: NotRequired[str]
    r"""A unique ID of the chat completion."""
    object: NotRequired[Object]
    r"""The object type, which is always set to `chat.completion`."""
    choices: NotRequired[List[ChatChoiceTypedDict]]
    usage: NotRequired[UsageTypedDict]
    created: NotRequired[int]
    r"""The Unix timestamp (in seconds) for when the generation completed."""


class ChatResult(BaseModel):
    r"""Successfully generated a chat response."""

    id: Optional[str] = None
    r"""A unique ID of the chat completion."""

    object: Optional[Object] = None
    r"""The object type, which is always set to `chat.completion`."""

    choices: Optional[List[ChatChoice]] = None

    usage: Optional[Usage] = None

    created: Optional[int] = None
    r"""The Unix timestamp (in seconds) for when the generation completed."""
