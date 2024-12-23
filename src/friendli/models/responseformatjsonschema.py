"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


Type = Literal["json_schema"]
r"""The type of the response format: `json_schema`"""


class SchemaTypedDict(TypedDict):
    r"""The schema for the response format, described as a JSON Schema object."""


class Schema(BaseModel):
    r"""The schema for the response format, described as a JSON Schema object."""


class JSONSchemaTypedDict(TypedDict):
    schema_: SchemaTypedDict
    r"""The schema for the response format, described as a JSON Schema object."""
    name: NotRequired[Nullable[str]]
    r"""The name of the response format."""


class JSONSchema(BaseModel):
    schema_: Annotated[Schema, pydantic.Field(alias="schema")]
    r"""The schema for the response format, described as a JSON Schema object."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the response format."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name"]
        nullable_fields = ["name"]
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


class ResponseFormatJSONSchemaTypedDict(TypedDict):
    type: Type
    r"""The type of the response format: `json_schema`"""
    json_schema: JSONSchemaTypedDict


class ResponseFormatJSONSchema(BaseModel):
    type: Type
    r"""The type of the response format: `json_schema`"""

    json_schema: JSONSchema