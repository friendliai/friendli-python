# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore

from ..config import Config
from .chat import AsyncChat, SyncChat
from .completions import AsyncCompletions, SyncCompletions
from .token import AsyncToken, SyncToken


class SyncContainer:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

        self.chat = SyncChat(core=self._core, config=self._config)
        self.completions = SyncCompletions(core=self._core, config=self._config)
        self.token = SyncToken(core=self._core, config=self._config)


class AsyncContainer:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

        self.chat = AsyncChat(core=self._core, config=self._config)
        self.completions = AsyncCompletions(core=self._core, config=self._config)
        self.token = AsyncToken(core=self._core, config=self._config)
