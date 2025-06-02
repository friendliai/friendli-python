# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import logging
from typing import Any, Mapping, Optional

from friendli_core.types import UNSET, BaseModel, OptionalNullable
from friendli_core.utils.retries import RetryConfig

DEFAULT_SPLIT_NAME = "train"


class Config(BaseModel):
    x_friendli_team: OptionalNullable[str] = UNSET
    retries: OptionalNullable[RetryConfig] = UNSET
    server_url: Optional[str] = None
    timeout_ms: Optional[int] = None
    http_headers: Optional[Mapping[str, str]] = None

    def model_post_init(self, __context: Any) -> None:
        if self.x_friendli_team == UNSET:
            logging.warning(
                "`x_friendli_team` is not provided. API calls may fail.",
            )
