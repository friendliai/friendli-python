"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .streamedcompletiontokencomplete import (
    StreamedCompletionTokenComplete,
    StreamedCompletionTokenCompleteTypedDict,
)
from .streamedcompletiontokensampled import (
    StreamedCompletionTokenSampled,
    StreamedCompletionTokenSampledTypedDict,
)
from friendli.types import BaseModel
from friendli.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypedDict


StreamedCompletionResultDataTypedDict = Union[
    StreamedCompletionTokenCompleteTypedDict, StreamedCompletionTokenSampledTypedDict
]


StreamedCompletionResultData = Annotated[
    Union[
        Annotated[StreamedCompletionTokenSampled, Tag("token_sampled")],
        Annotated[StreamedCompletionTokenComplete, Tag("complete")],
    ],
    Discriminator(lambda m: get_discriminator(m, "event", "event")),
]


class StreamedCompletionResultTypedDict(TypedDict):
    data: StreamedCompletionResultDataTypedDict


class StreamedCompletionResult(BaseModel):
    data: StreamedCompletionResultData
