"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from friendli_core.types import BaseModel


class DedicatedDetokenizationBodyTypedDict(TypedDict):
    model: str
    r"""ID of target endpoint. If you want to send request to specific adapter, use the format \"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\". Otherwise, you can just use \"YOUR_ENDPOINT_ID\" alone."""
    tokens: List[int]
    r"""A token sequence to detokenize."""


class DedicatedDetokenizationBody(BaseModel):
    model: str
    r"""ID of target endpoint. If you want to send request to specific adapter, use the format \"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\". Otherwise, you can just use \"YOUR_ENDPOINT_ID\" alone."""

    tokens: List[int]
    r"""A token sequence to detokenize."""
