"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing import List, Literal
from typing_extensions import TypedDict


FileBuiltInToolType = Literal["file:text"]
r"""The type of the file parser tool. Only .txt and .pdf files are supported."""


class FileBuiltInToolTypedDict(TypedDict):
    type: FileBuiltInToolType
    r"""The type of the file parser tool. Only .txt and .pdf files are supported."""
    files: List[str]
    r"""A List of file IDs."""


class FileBuiltInTool(BaseModel):
    type: FileBuiltInToolType
    r"""The type of the file parser tool. Only .txt and .pdf files are supported."""

    files: List[str]
    r"""A List of file IDs."""
