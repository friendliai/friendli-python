# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from friendli_core.types import UNSET, BaseModel, OptionalNullable
from friendli_core.utils import FieldMetadata, HeaderMetadata


class Config(BaseModel):
    x_friendli_team: Annotated[
        OptionalNullable[str],
        pydantic.Field(alias="X-Friendli-Team"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = UNSET
