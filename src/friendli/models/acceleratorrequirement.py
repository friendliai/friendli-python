"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing_extensions import TypedDict

from friendli.types import BaseModel


class AcceleratorRequirementTypedDict(TypedDict):
    r"""Accelerator requirement."""

    count: int
    r"""Specifies the number of instances."""
    type: str
    r"""Specifies the instance type."""


class AcceleratorRequirement(BaseModel):
    r"""Accelerator requirement."""

    count: int
    r"""Specifies the number of instances."""

    type: str
    r"""Specifies the instance type."""
