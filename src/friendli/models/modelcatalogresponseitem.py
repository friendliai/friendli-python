"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from pydantic import model_serializer
from typing_extensions import TypedDict

from friendli.types import UNSET_SENTINEL, BaseModel, Nullable

from .functionality import Functionality, FunctionalityTypedDict
from .pricingmodel import PricingModel, PricingModelTypedDict


class ModelCatalogResponseItemTypedDict(TypedDict):
    r"""Model listing in `/models` API."""

    context_length: int
    created: int
    description: str
    functionality: FunctionalityTypedDict
    r"""Functionality of the model."""
    hugging_face_url: str
    id: str
    license: str
    name: str
    policy: Nullable[str]
    pricing: PricingModelTypedDict
    r"""Price per 1M tokens in USD currency."""


class ModelCatalogResponseItem(BaseModel):
    r"""Model listing in `/models` API."""

    context_length: int

    created: int

    description: str

    functionality: Functionality
    r"""Functionality of the model."""

    hugging_face_url: str

    id: str

    license: str

    name: str

    policy: Nullable[str]

    pricing: PricingModel
    r"""Price per 1M tokens in USD currency."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["policy"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
