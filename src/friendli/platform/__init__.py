# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore

from ..config import Config
from ..platform.files import AsyncFiles, SyncFiles


class SyncPlatform:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

        self.files = SyncFiles(core=self._core, config=self._config)


class AsyncPlatform:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

        self.files = AsyncFiles(core=self._core, config=self._config)
