"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing import List, Literal
from typing_extensions import TypedDict


RagBuiltInToolType = Literal["rag:knowledge-base"]
r"""The type of the rag knowledge-base tool."""


class RagBuiltInToolTypedDict(TypedDict):
    type: RagBuiltInToolType
    r"""The type of the rag knowledge-base tool."""
    knowledge_base_ids: List[str]
    r"""A List of knowledge-base IDs. For now, only one knowledge-base is supported."""


class RagBuiltInTool(BaseModel):
    type: RagBuiltInToolType
    r"""The type of the rag knowledge-base tool."""

    knowledge_base_ids: List[str]
    r"""A List of knowledge-base IDs. For now, only one knowledge-base is supported."""
