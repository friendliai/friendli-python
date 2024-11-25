"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filebuiltintool import FileBuiltInTool, FileBuiltInToolTypedDict
from .functiontool import FunctionTool, FunctionToolTypedDict
from .otherbuiltintool import OtherBuiltInTool, OtherBuiltInToolTypedDict
from .ragbuiltintool import RagBuiltInTool, RagBuiltInToolTypedDict
from friendli.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated


ToolAssistedChatToolTypedDict = Union[
    OtherBuiltInToolTypedDict,
    FunctionToolTypedDict,
    FileBuiltInToolTypedDict,
    RagBuiltInToolTypedDict,
]


ToolAssistedChatTool = Annotated[
    Union[
        Annotated[FunctionTool, Tag("function")],
        Annotated[FileBuiltInTool, Tag("file:text")],
        Annotated[OtherBuiltInTool, Tag("math:calculator")],
        Annotated[OtherBuiltInTool, Tag("math:statistics")],
        Annotated[OtherBuiltInTool, Tag("math:calendar")],
        Annotated[OtherBuiltInTool, Tag("web:search")],
        Annotated[OtherBuiltInTool, Tag("web:url")],
        Annotated[OtherBuiltInTool, Tag("code:python-interpreter")],
        Annotated[RagBuiltInTool, Tag("rag:knowledge-base")],
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]
