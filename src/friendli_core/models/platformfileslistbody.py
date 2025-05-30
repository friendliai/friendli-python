"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Literal

from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict

from friendli_core.types import (
    UNSET,
    UNSET_SENTINEL,
    BaseModel,
    Nullable,
    OptionalNullable,
)

Order = Literal["asc", "desc"]
r"""Sort order by `created` timestamp. Use `asc` for ascending or `desc` for descending. Defaults to `desc`."""


class PlatformFilesListBodyTypedDict(TypedDict):
    after: NotRequired[Nullable[str]]
    r"""File ID after which to fetch the next page of results. Optional."""
    limit: NotRequired[Nullable[int]]
    r"""Maximum number of files to return, between [1, 10,000]. Defaults to 10,000."""
    order: NotRequired[Nullable[Order]]
    r"""Sort order by `created` timestamp. Use `asc` for ascending or `desc` for descending. Defaults to `desc`."""
    purpose: NotRequired[Nullable[str]]
    r"""Return files with the specified purpose. Optional."""


class PlatformFilesListBody(BaseModel):
    after: OptionalNullable[str] = UNSET
    r"""File ID after which to fetch the next page of results. Optional."""

    limit: OptionalNullable[int] = 10000
    r"""Maximum number of files to return, between [1, 10,000]. Defaults to 10,000."""

    order: OptionalNullable[Order] = "desc"
    r"""Sort order by `created` timestamp. Use `asc` for ascending or `desc` for descending. Defaults to `desc`."""

    purpose: OptionalNullable[str] = UNSET
    r"""Return files with the specified purpose. Optional."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["after", "limit", "order", "purpose"]
        nullable_fields = ["after", "limit", "order", "purpose"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
