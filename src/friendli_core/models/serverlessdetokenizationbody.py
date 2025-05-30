"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from friendli_core.types import BaseModel


class ServerlessDetokenizationBodyTypedDict(TypedDict):
    model: str
    r"""Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models)."""
    tokens: List[int]
    r"""A token sequence to detokenize."""


class ServerlessDetokenizationBody(BaseModel):
    model: str
    r"""Code of the model to use. See [available model list](https://friendli.ai/docs/guides/serverless_endpoints/pricing#text-generation-models)."""

    tokens: List[int]
    r"""A token sequence to detokenize."""
