# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK Utils."""

from __future__ import annotations

from hashlib import sha256
from typing import TYPE_CHECKING

import httpx

from friendli.core.utils import *  # noqa: F403

if TYPE_CHECKING:
    from friendli.core.models import DedicatedDatasetModality


def digest(*, data: bytes) -> str:
    """Compute the SHA-256 digest of the data."""
    return "sha256:" + sha256(data).hexdigest()


def download_from_url(*, url: str) -> bytes:
    """Download content from a URL.

    Args:
        url: URL to download from

    Returns:
        bytes: Downloaded content

    Raises:
        httpx.HTTPStatusError: If download fails
    """
    res: httpx.Response = httpx.get(url, follow_redirects=True)
    res.raise_for_status()
    return res.content


def check_modality(
    *,
    dataset_modality: DedicatedDatasetModality,
    message_modality: DedicatedDatasetModality,
) -> DedicatedDatasetModality:
    """Check if the message modality is compatible with the dataset modality.

    Args:
        dataset_modality: Dataset modality to check against
        message_modality: Message modality to be checked

    Returns:
        DedicatedDatasetModality: The input message modality object, returned unchanged
            for convenience.

    Raises:
        ValueError: If message modality is not a subset of dataset modality
    """
    if not all(
        modal in dataset_modality.input_modals
        for modal in message_modality.input_modals
    ):
        msg = (
            f"Input modality mismatch - Dataset supports "
            f"{dataset_modality.input_modals} but got {message_modality.input_modals}. "
            f"Please check the input modalities."
        )
        raise ValueError(msg)

    if not all(
        modal in dataset_modality.output_modals
        for modal in message_modality.output_modals
    ):
        msg = (
            f"Output modality mismatch - Dataset supports "
            f"{dataset_modality.output_modals} but got "
            f"{message_modality.output_modals}. "
            f"Please check the output modalities."
        )
        raise ValueError(msg)

    return message_modality
