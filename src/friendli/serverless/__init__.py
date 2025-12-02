# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

from ..config import Config
from .chat import AsyncChat, SyncChat
from .chat_render import AsyncChatRender, SyncChatRender
from .completions import AsyncCompletions, SyncCompletions
from .knowledge import AsyncKnowledge, SyncKnowledge
from .model import AsyncModel, SyncModel
from .token import AsyncToken, SyncToken
from .tool_assisted_chat import AsyncToolAssistedChat, SyncToolAssistedChat


class SyncServerless:
    """Friendli Python SDK Serverless."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncServerless class."""
        self._core = core
        self._config = config

        self.chat = SyncChat(core=self._core, config=self._config)
        self.chat_render = SyncChatRender(core=self._core, config=self._config)
        self.completions = SyncCompletions(core=self._core, config=self._config)
        self.token = SyncToken(core=self._core, config=self._config)
        self.knowledge = SyncKnowledge(core=self._core, config=self._config)
        self.model = SyncModel(core=self._core, config=self._config)
        self.tool_assisted_chat = SyncToolAssistedChat(
            core=self._core, config=self._config
        )


class AsyncServerless:
    """Friendli Python SDK Serverless."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncServerless class."""
        self._core = core
        self._config = config

        self.chat = AsyncChat(core=self._core, config=self._config)
        self.chat_render = AsyncChatRender(core=self._core, config=self._config)
        self.completions = AsyncCompletions(core=self._core, config=self._config)
        self.token = AsyncToken(core=self._core, config=self._config)
        self.knowledge = AsyncKnowledge(core=self._core, config=self._config)
        self.model = AsyncModel(core=self._core, config=self._config)
        self.tool_assisted_chat = AsyncToolAssistedChat(
            core=self._core, config=self._config
        )
