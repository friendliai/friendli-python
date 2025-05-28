# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import Any, Coroutine, Mapping, Optional

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncImage:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def generate(
        self,
        *,
        model: str,
        num_inference_steps: int,
        prompt: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        guidance_scale: OptionalNullable[float] = UNSET,
        response_format: OptionalNullable[
            models.DedicatedImageGenerationBodyResponseFormat
        ] = "url",
        seed: OptionalNullable[int] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedImageGenerateSuccess:
        """Image generations

        Given a description, the model generates image(s).

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param num_inference_steps: The number of inference steps to use during image generation. Supported range: [1, 50].
        :param prompt: A text description of the desired image(s).
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param guidance_scale: Adjusts the alignment of the generated image with the input prompt. Higher values (e.g., 8-10) make the output more faithful to the prompt, while lower values (e.g., 1-5) encourage more creative freedom. This parameter may be irrelevant for certain models, such as `FLUX.Schnell`.
        :param response_format: The format in which the generated image(s) will be returned. One of `url(default)`, `raw`, `png`, `jpeg`, and `jpg`.
        :param seed: The seed to use for image generation.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.image.generate(
            model=model,
            num_inference_steps=num_inference_steps,
            prompt=prompt,
            x_friendli_team=x_friendli_team,
            guidance_scale=guidance_scale,
            response_format=response_format,
            seed=seed,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncImage:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def generate(
        self,
        *,
        model: str,
        num_inference_steps: int,
        prompt: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        guidance_scale: OptionalNullable[float] = UNSET,
        response_format: OptionalNullable[
            models.DedicatedImageGenerationBodyResponseFormat
        ] = "url",
        seed: OptionalNullable[int] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedImageGenerateSuccess:
        """Image generations

        Given a description, the model generates image(s).

        :param model: ID of target endpoint. If you want to send request to specific adapter, use the format \\"YOUR_ENDPOINT_ID:YOUR_ADAPTER_ROUTE\\". Otherwise, you can just use \\"YOUR_ENDPOINT_ID\\" alone.
        :param num_inference_steps: The number of inference steps to use during image generation. Supported range: [1, 50].
        :param prompt: A text description of the desired image(s).
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param guidance_scale: Adjusts the alignment of the generated image with the input prompt. Higher values (e.g., 8-10) make the output more faithful to the prompt, while lower values (e.g., 1-5) encourage more creative freedom. This parameter may be irrelevant for certain models, such as `FLUX.Schnell`.
        :param response_format: The format in which the generated image(s) will be returned. One of `url(default)`, `raw`, `png`, `jpeg`, and `jpg`.
        :param seed: The seed to use for image generation.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.image.generate(
            model=model,
            prompt=prompt,
            x_friendli_team=x_friendli_team,
            num_inference_steps=num_inference_steps,
            response_format=response_format,
            seed=seed,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
