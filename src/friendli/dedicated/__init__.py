# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

from ..config import Config
from .audio import AsyncAudio, SyncAudio
from .chat import AsyncChat, SyncChat
from .chat_render import AsyncChatRender, SyncChatRender
from .completions import AsyncCompletions, SyncCompletions
from .embeddings import AsyncEmbeddings, SyncEmbeddings
from .endpoint import AsyncEndpoint, SyncEndpoint
from .image import AsyncImage, SyncImage
from .token import AsyncToken, SyncToken


class SyncDedicated:
    """SyncDedicated."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncDedicated class."""
        self._core = core
        self._config = config

        self.chat = SyncChat(core=self._core, config=self._config)
        self.chat_render = SyncChatRender(core=self._core, config=self._config)
        self.completions = SyncCompletions(core=self._core, config=self._config)
        self.embeddings = SyncEmbeddings(core=self._core, config=self._config)
        self.token = SyncToken(core=self._core, config=self._config)
        self.image = SyncImage(core=self._core, config=self._config)
        self.audio = SyncAudio(core=self._core, config=self._config)
        self.endpoint = SyncEndpoint(core=self._core, config=self._config)


class AsyncDedicated:
    """AsyncDedicated."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncDedicated class."""
        self._core = core
        self._config = config

        self.chat = AsyncChat(core=self._core, config=self._config)
        self.chat_render = AsyncChatRender(core=self._core, config=self._config)
        self.completions = AsyncCompletions(core=self._core, config=self._config)
        self.embeddings = AsyncEmbeddings(core=self._core, config=self._config)
        self.token = AsyncToken(core=self._core, config=self._config)
        self.image = AsyncImage(core=self._core, config=self._config)
        self.audio = AsyncAudio(core=self._core, config=self._config)
        self.endpoint = AsyncEndpoint(core=self._core, config=self._config)
