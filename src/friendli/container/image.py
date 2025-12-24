# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Mapping, Optional, Union

from friendli.core.types import UNSET, OptionalNullable

if TYPE_CHECKING:
    from friendli.core import models, utils
    from friendli.core.sdk import AsyncFriendliCore, SyncFriendliCore

    from ..config import Config


class SyncImage:
    """SyncImage."""

    def __init__(self, core: SyncFriendliCore, config: Config) -> None:
        """Initialize the SyncImage class."""
        self._core = core
        self._config = config

    def generate(
        self,
        *,
        prompt: str,
        model: OptionalNullable[str] = UNSET,
        num_inference_steps: Optional[int] = 20,
        guidance_scale: Optional[float] = 0,
        seed: OptionalNullable[int] = UNSET,
        response_format: OptionalNullable[
            models.ContainerImageGenerationBodyResponseFormat
        ] = UNSET,
        control_images: OptionalNullable[
            Union[List[models.ImageInput], List[models.ImageInputTypedDict]]
        ] = UNSET,
        controlnet_weights: OptionalNullable[List[float]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerImageGenerateSuccess:
        """Image generations

        Given a description, the model generates image.

        :param prompt: A text description of the desired image.
        :param model: Routes the request to a specific adapter.
        :param num_inference_steps: The number of inference steps to use during image generation. Defaults to 20. Supported range: [1, 50].
        :param guidance_scale: Adjusts the alignment of the generated image with the input prompt. Higher values (e.g., 8-10) make the output more faithful to the prompt, while lower values (e.g., 1-5) encourage more creative freedom. Defaults to 0. This parameter may be irrelevant for certain models, such as `FLUX.Schnell`.
        :param seed: The seed to use for image generation.
        :param response_format: The format in which the generated image will be returned. One of `raw` and `jpeg`.
        :param control_images: Optional input images used to condition or guide the generation process (e.g., for ControlNet or image editing models). This field is only applicable when using ControlNet or image editing models.
        :param controlnet_weights: A list of weights that determine the influence of each ControlNet model in the generation process. Each value must be within [0, 1], where 0 disables the corresponding ControlNet and 1 applies it fully. When multiple ControlNet models are used, the list length must match the number of control images. If omitted, all ControlNet models default to full influence (1.0). This field is only applicable when using ControlNet models.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.image.generate(
            prompt=prompt,
            model=model,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            seed=seed,
            response_format=response_format,
            control_images=control_images,
            controlnet_weights=controlnet_weights,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def edit(
        self,
        *,
        image: Union[
            models.ContainerImageEditBodyImage,
            models.ContainerImageEditBodyImageTypedDict,
        ],
        prompt: str,
        model: OptionalNullable[str] = UNSET,
        num_inference_steps: Optional[int] = 20,
        guidance_scale: Optional[float] = 0,
        seed: OptionalNullable[int] = UNSET,
        response_format: OptionalNullable[
            models.ContainerImageEditBodyResponseFormat
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerImageGenerateSuccess:
        """Image edits

        Given an image and a description, the model edits the image.

        :param image: The image(s) to edit. Must be in a supported image format.
        :param prompt: A text description of the desired image.
        :param model: Routes the request to a specific adapter.
        :param num_inference_steps: The number of inference steps to use during image generation. Defaults to 20. Supported range: [1, 50].
        :param guidance_scale: Adjusts the alignment of the generated image with the input prompt. Higher values (e.g., 8-10) make the output more faithful to the prompt, while lower values (e.g., 1-5) encourage more creative freedom. Defaults to 0. This parameter may be irrelevant for certain models, such as `FLUX.Schnell`.
        :param seed: The seed to use for image generation.
        :param response_format: The format in which the generated image will be returned. One of `raw` and `jpeg`.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.container.image.edit(
            image=image,
            prompt=prompt,
            model=model,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            seed=seed,
            response_format=response_format,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncImage:
    """AsyncImage."""

    def __init__(self, core: AsyncFriendliCore, config: Config) -> None:
        """Initialize the AsyncImage class."""
        self._core = core
        self._config = config

    async def generate(
        self,
        *,
        prompt: str,
        model: OptionalNullable[str] = UNSET,
        num_inference_steps: Optional[int] = 20,
        guidance_scale: Optional[float] = 0,
        seed: OptionalNullable[int] = UNSET,
        response_format: OptionalNullable[
            models.ContainerImageGenerationBodyResponseFormat
        ] = UNSET,
        control_images: OptionalNullable[
            Union[List[models.ImageInput], List[models.ImageInputTypedDict]]
        ] = UNSET,
        controlnet_weights: OptionalNullable[List[float]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerImageGenerateSuccess:
        """Image generations

        Given a description, the model generates image.

        :param prompt: A text description of the desired image.
        :param model: Routes the request to a specific adapter.
        :param num_inference_steps: The number of inference steps to use during image generation. Defaults to 20. Supported range: [1, 50].
        :param guidance_scale: Adjusts the alignment of the generated image with the input prompt. Higher values (e.g., 8-10) make the output more faithful to the prompt, while lower values (e.g., 1-5) encourage more creative freedom. Defaults to 0. This parameter may be irrelevant for certain models, such as `FLUX.Schnell`.
        :param seed: The seed to use for image generation.
        :param response_format: The format in which the generated image will be returned. One of `raw` and `jpeg`.
        :param control_images: Optional input images used to condition or guide the generation process (e.g., for ControlNet or image editing models). This field is only applicable when using ControlNet or image editing models.
        :param controlnet_weights: A list of weights that determine the influence of each ControlNet model in the generation process. Each value must be within [0, 1], where 0 disables the corresponding ControlNet and 1 applies it fully. When multiple ControlNet models are used, the list length must match the number of control images. If omitted, all ControlNet models default to full influence (1.0). This field is only applicable when using ControlNet models.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.image.generate(
            prompt=prompt,
            model=model,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            seed=seed,
            response_format=response_format,
            control_images=control_images,
            controlnet_weights=controlnet_weights,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def edit(
        self,
        *,
        image: Union[
            models.ContainerImageEditBodyImage,
            models.ContainerImageEditBodyImageTypedDict,
        ],
        prompt: str,
        model: OptionalNullable[str] = UNSET,
        num_inference_steps: Optional[int] = 20,
        guidance_scale: Optional[float] = 0,
        seed: OptionalNullable[int] = UNSET,
        response_format: OptionalNullable[
            models.ContainerImageEditBodyResponseFormat
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ContainerImageGenerateSuccess:
        """Image edits

        Given an image and a description, the model edits the image.

        :param image: The image(s) to edit. Must be in a supported image format.
        :param prompt: A text description of the desired image.
        :param model: Routes the request to a specific adapter.
        :param num_inference_steps: The number of inference steps to use during image generation. Defaults to 20. Supported range: [1, 50].
        :param guidance_scale: Adjusts the alignment of the generated image with the input prompt. Higher values (e.g., 8-10) make the output more faithful to the prompt, while lower values (e.g., 1-5) encourage more creative freedom. Defaults to 0. This parameter may be irrelevant for certain models, such as `FLUX.Schnell`.
        :param seed: The seed to use for image generation.
        :param response_format: The format in which the generated image will be returned. One of `raw` and `jpeg`.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.container.image.edit(
            image=image,
            prompt=prompt,
            model=model,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            seed=seed,
            response_format=response_format,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
