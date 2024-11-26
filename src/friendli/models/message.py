"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assistantmessage import AssistantMessage, AssistantMessageTypedDict
from .systemmessage import SystemMessage, SystemMessageTypedDict
from .toolmessage import ToolMessage, ToolMessageTypedDict
from .usermessage import UserMessage, UserMessageTypedDict
from friendli.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType


MessageTypedDict = TypeAliasType(
    "MessageTypedDict",
    Union[
        SystemMessageTypedDict,
        UserMessageTypedDict,
        AssistantMessageTypedDict,
        ToolMessageTypedDict,
    ],
)


Message = Annotated[
    Union[
        Annotated[SystemMessage, Tag("system")],
        Annotated[UserMessage, Tag("user")],
        Annotated[AssistantMessage, Tag("assistant")],
        Annotated[ToolMessage, Tag("tool")],
    ],
    Discriminator(lambda m: get_discriminator(m, "role", "role")),
]
