# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Mapping, Optional, Union

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncAudio:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def transcribe(
        self,
        *,
        file: Union[models.FileModel, models.FileModelTypedDict],
        model: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        chunking_strategy: OptionalNullable[
            Union[models.ChunkingStrategy, models.ChunkingStrategyTypedDict]
        ] = UNSET,
        language: OptionalNullable[str] = UNSET,
        temperature: OptionalNullable[float] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedAudioTranscriptionSuccess:
        """Audio transcriptions

        Given an audio file, the model transcribes it into text.

        :param file: The audio file object (not file name) to transcribe, in one of these formats: mp3, wav, flac, ogg, and many other standard audio formats.
        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param chunking_strategy: Controls how the audio is cut into chunks. When set to `\\"auto\\"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block.
        :param language: The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.
        :param temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.audio.transcribe(
            file=file,
            model=model,
            x_friendli_team=x_friendli_team,
            chunking_strategy=chunking_strategy,
            language=language,
            temperature=temperature,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncAudio:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def transcribe(
        self,
        *,
        file: Union[models.FileModel, models.FileModelTypedDict],
        model: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        chunking_strategy: OptionalNullable[
            Union[models.ChunkingStrategy, models.ChunkingStrategyTypedDict]
        ] = UNSET,
        language: OptionalNullable[str] = UNSET,
        temperature: OptionalNullable[float] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedAudioTranscriptionSuccess:
        """Audio transcriptions

        Given an audio file, the model transcribes it into text.

        :param file: The audio file object (not file name) to transcribe, in one of these formats: mp3, wav, flac, ogg, and many other standard audio formats.
        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param chunking_strategy: Controls how the audio is cut into chunks. When set to `\\"auto\\"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block.
        :param language: The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.
        :param temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.audio.transcribe(
            file=file,
            model=model,
            x_friendli_team=x_friendli_team,
            chunking_strategy=chunking_strategy,
            language=language,
            temperature=temperature,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
