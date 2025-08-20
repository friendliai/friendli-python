# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import logging
from typing import Any, Mapping, Optional

from friendli.core.types import UNSET, BaseModel, OptionalNullable
from friendli.core.utils.retries import RetryConfig  # noqa: TC001

DEFAULT_SPLIT_NAME = "train"


class Config(BaseModel):
    """Config."""

    x_friendli_team: OptionalNullable[str] = UNSET
    retries: OptionalNullable[RetryConfig] = UNSET
    server_url: Optional[str] = None
    timeout_ms: Optional[int] = None
    http_headers: Optional[Mapping[str, str]] = None

    def model_post_init(self, context: Any) -> None:  # noqa: ANN401
        """Model post init."""
        _ = context
        if self.x_friendli_team == UNSET:
            logging.warning(
                "`x_friendli_team` is not provided. API calls may fail.",
            )
