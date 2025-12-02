# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Optional, Union

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

    from ..config import Config


class SyncAudio:
    """SyncAudio."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncAudio class."""
        self._core = core
        self._config = config

    def transcribe(
        self,
        *,
        file: bytes,
        model: OptionalNullable[str] = UNSET,
        chunking_strategy: OptionalNullable[
            Union[
                models.ContainerAudioTranscriptionBodyChunkingStrategy,
                models.ContainerAudioTranscriptionBodyChunkingStrategyTypedDict,
            ]
        ] = UNSET,
        language: OptionalNullable[str] = UNSET,
        temperature: OptionalNullable[float] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerAudioTranscriptionSuccess:
        """Audio transcriptions

        Given an audio file, the model transcribes it into text.

        :param file: The audio file object (not file name) to transcribe, in one of these formats: mp3, wav, flac, ogg, and many other standard audio formats.
        :param model: Routes the request to a specific adapter.
        :param chunking_strategy: Controls how the audio is cut into chunks. When set to `\\"auto\\"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block.
        :param language: The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.
        :param temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.audio.transcribe(
            file=file,
            model=model,
            chunking_strategy=chunking_strategy,
            language=language,
            temperature=temperature,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncAudio:
    """AsyncAudio."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncAudio class."""
        self._core = core
        self._config = config

    async def transcribe(
        self,
        *,
        file: bytes,
        model: OptionalNullable[str] = UNSET,
        chunking_strategy: OptionalNullable[
            Union[
                models.ContainerAudioTranscriptionBodyChunkingStrategy,
                models.ContainerAudioTranscriptionBodyChunkingStrategyTypedDict,
            ]
        ] = UNSET,
        language: OptionalNullable[str] = UNSET,
        temperature: OptionalNullable[float] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerAudioTranscriptionSuccess:
        """Audio transcriptions

        Given an audio file, the model transcribes it into text.

        :param file: The audio file object (not file name) to transcribe, in one of these formats: mp3, wav, flac, ogg, and many other standard audio formats.
        :param model: Routes the request to a specific adapter.
        :param chunking_strategy: Controls how the audio is cut into chunks. When set to `\\"auto\\"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block.
        :param language: The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.
        :param temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.audio.transcribe(
            file=file,
            model=model,
            chunking_strategy=chunking_strategy,
            language=language,
            temperature=temperature,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
