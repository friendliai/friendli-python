"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List, Union

from typing_extensions import TypeAliasType, TypedDict

from friendli_core.types import BaseModel

from .b64imageitem import B64ImageItem, B64ImageItemTypedDict
from .urlimageitem import URLImageItem, URLImageItemTypedDict

DataTypedDict = TypeAliasType(
    "DataTypedDict", Union[List[URLImageItemTypedDict], List[B64ImageItemTypedDict]]
)


Data = TypeAliasType("Data", Union[List[URLImageItem], List[B64ImageItem]])


class DedicatedImageGenerateSuccessTypedDict(TypedDict):
    data: DataTypedDict


class DedicatedImageGenerateSuccess(BaseModel):
    data: Data
