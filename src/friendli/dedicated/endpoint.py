# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK."""

from __future__ import annotations

import io
from typing import IO, Any, Dict, Mapping, Optional, Union

from friendli_core import models, utils
from friendli_core.sdk import AsyncFriendliCore, SyncFriendliCore
from friendli_core.types import UNSET, OptionalNullable

from ..config import Config


class SyncEndpoint:
    def __init__(self, core: SyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    def wandb_artifact_create(
        self,
        *,
        wandb_artifact_version_name: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        accelerator: OptionalNullable[
            Union[models.AcceleratorRequirement, models.AcceleratorRequirementTypedDict]
        ] = UNSET,
        autoscaling_policy: OptionalNullable[
            Union[models.AutoscalingPolicy, models.AutoscalingPolicyTypedDict]
        ] = UNSET,
        idempotency_key: OptionalNullable[str] = UNSET,
        name: OptionalNullable[str] = UNSET,
        project_id: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointWandbArtifactCreateResponse:
        """Create endpoint from W&B artifact

        Create an endpoint from Weights & Biases artifact. If the idempotency key is provided, the API will check if the endpoint already exists, and rollout the existing endpoint if it does. In such cases, the project id must be provided.

        :param wandb_artifact_version_name: The specific model artifact version from Weights & Biases. The referred artifact will be used to create a new endpoint in Friendli Dedicated Endpoints or rollout an existing one.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param accelerator: Specifies the instance type for the endpoint.
        :param autoscaling_policy: Defines autoscaling settings for the endpoint.
        :param idempotency_key: Used by Friendli Dedicated Endpoints to track which webhook automation triggered an endpoint rollout. If the `idempotencyKey` is provided, the API will check if the endpoint already exists, and rollout the existing endpoint if it does. In such cases, the `projectId` must be provided. Any unique value can be used.
        :param name: Specifies the name of your endpoint. If not provided, a name will be automatically generated for you.
        :param project_id: Specifies where endpoint will be created in your Friendli Dedicated Endpoints. If not provided, a new project will be created within your default team.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.wandb_artifact_create(
            wandb_artifact_version_name=wandb_artifact_version_name,
            x_friendli_team=x_friendli_team,
            accelerator=accelerator,
            autoscaling_policy=autoscaling_policy,
            idempotency_key=idempotency_key,
            name=name,
            project_id=project_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def create(
        self,
        *,
        advanced: Union[
            models.EndpointAdvancedConfig, models.EndpointAdvancedConfigTypedDict
        ],
        hf_model_repo: str,
        instance_option_id: str,
        name: str,
        project_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        autoscaling_policy: OptionalNullable[
            Union[models.AutoscalingPolicy, models.AutoscalingPolicyTypedDict]
        ] = UNSET,
        hf_model_repo_revision: OptionalNullable[str] = UNSET,
        initial_version_comment: OptionalNullable[str] = UNSET,
        simplescale: OptionalNullable[
            Union[
                models.EndpointSimplescaleConfig,
                models.EndpointSimplescaleConfigTypedDict,
            ]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Create a new endpoint

        Create a new endpoint and return its status

        :param advanced: Endpoint advanced config.
        :param hf_model_repo: HF ID of the model.
        :param instance_option_id: The ID of the instance option.
        :param name: The name of the endpoint.
        :param project_id: The ID of the project that owns the endpoint.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param autoscaling_policy: The auto scaling configuration of the endpoint.
        :param hf_model_repo_revision: HF commit hash of the model.
        :param initial_version_comment: The comment for the initial version.
        :param simplescale: The simple scaling configuration of the endpoint.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.create(
            advanced=advanced,
            hf_model_repo=hf_model_repo,
            instance_option_id=instance_option_id,
            name=name,
            project_id=project_id,
            x_friendli_team=x_friendli_team,
            autoscaling_policy=autoscaling_policy,
            hf_model_repo_revision=hf_model_repo_revision,
            initial_version_comment=initial_version_comment,
            simplescale=simplescale,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def list(
        self,
        *,
        project_id: OptionalNullable[str] = "",
        cursor: OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointListResponse:
        """List all endpoints

        List all endpoint statuses

        :param project_id: The ID of the project. If omitted, query all endpoints under the team.
        :param cursor: Cursor for pagination
        :param limit: Limit of items per page
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.list(
            project_id=project_id,
            cursor=cursor,
            limit=limit,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Get endpoint status

        Get the status of an endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.get(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def update(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        advanced: OptionalNullable[
            Union[models.EndpointAdvancedConfig, models.EndpointAdvancedConfigTypedDict]
        ] = UNSET,
        autoscaling_policy: OptionalNullable[
            Union[models.AutoscalingPolicy, models.AutoscalingPolicyTypedDict]
        ] = UNSET,
        hf_model_repo: OptionalNullable[str] = UNSET,
        hf_model_repo_revision: OptionalNullable[str] = UNSET,
        instance_option_id: OptionalNullable[str] = UNSET,
        name: OptionalNullable[str] = UNSET,
        new_version_comment: OptionalNullable[str] = UNSET,
        simplescale: OptionalNullable[
            Union[
                models.EndpointSimplescaleConfig,
                models.EndpointSimplescaleConfigTypedDict,
            ]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointSpec:
        """Update endpoint spec

        Update the specification of a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param advanced: The advanced configuration of the endpoint.
        :param autoscaling_policy: The auto scaling configuration of the endpoint.
        :param hf_model_repo: HF ID of the model.
        :param hf_model_repo_revision: HF commit hash of the model.
        :param instance_option_id: The ID of the instance option.
        :param name: The name of the endpoint.
        :param new_version_comment: Comment for the new version.
        :param simplescale: The simple scaling configuration of the endpoint.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.update(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            advanced=advanced,
            autoscaling_policy=autoscaling_policy,
            hf_model_repo=hf_model_repo,
            hf_model_repo_revision=hf_model_repo_revision,
            instance_option_id=instance_option_id,
            name=name,
            new_version_comment=new_version_comment,
            simplescale=simplescale,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def delete(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete endpoint

        Delete a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.delete(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_version(
        self,
        *,
        endpoint_id: str,
        cursor: OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Dict[str, models.DedicatedEndpointSpec]:
        """Get endpoint versions

        Get versions of a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param cursor: Cursor for pagination
        :param limit: Limit of items per page
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.get_version(
            endpoint_id=endpoint_id,
            cursor=cursor,
            limit=limit,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def get_status(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Get endpoint status

        Get the status of a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.get_status(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def sleep(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Sleep endpoint

        Put a specific endpoint to sleep

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.sleep(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def wake(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Wake endpoint

        Wake up a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.wake(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def terminate(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Terminate endpoint

        Terminate a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.terminate(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    def restart(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Restart endpoint

        Restart a FAILED or TERMINATED endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.restart(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )


class AsyncEndpoint:
    def __init__(self, core: AsyncFriendliCore, config: Config):
        self._core = core
        self._config = config

    async def wandb_artifact_create(
        self,
        *,
        wandb_artifact_version_name: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        accelerator: OptionalNullable[
            Union[models.AcceleratorRequirement, models.AcceleratorRequirementTypedDict]
        ] = UNSET,
        autoscaling_policy: OptionalNullable[
            Union[models.AutoscalingPolicy, models.AutoscalingPolicyTypedDict]
        ] = UNSET,
        idempotency_key: OptionalNullable[str] = UNSET,
        name: OptionalNullable[str] = UNSET,
        project_id: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointWandbArtifactCreateResponse:
        """Create endpoint from W&B artifact

        Create an endpoint from Weights & Biases artifact. If the idempotency key is provided, the API will check if the endpoint already exists, and rollout the existing endpoint if it does. In such cases, the project id must be provided.

        :param wandb_artifact_version_name: The specific model artifact version from Weights & Biases. The referred artifact will be used to create a new endpoint in Friendli Dedicated Endpoints or rollout an existing one.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param accelerator: Specifies the instance type for the endpoint.
        :param autoscaling_policy: Defines autoscaling settings for the endpoint.
        :param idempotency_key: Used by Friendli Dedicated Endpoints to track which webhook automation triggered an endpoint rollout. If the `idempotencyKey` is provided, the API will check if the endpoint already exists, and rollout the existing endpoint if it does. In such cases, the `projectId` must be provided. Any unique value can be used.
        :param name: Specifies the name of your endpoint. If not provided, a name will be automatically generated for you.
        :param project_id: Specifies where endpoint will be created in your Friendli Dedicated Endpoints. If not provided, a new project will be created within your default team.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.wandb_artifact_create(
            wandb_artifact_version_name=wandb_artifact_version_name,
            x_friendli_team=x_friendli_team,
            accelerator=accelerator,
            autoscaling_policy=autoscaling_policy,
            idempotency_key=idempotency_key,
            name=name,
            project_id=project_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def create(
        self,
        *,
        advanced: Union[
            models.EndpointAdvancedConfig, models.EndpointAdvancedConfigTypedDict
        ],
        hf_model_repo: str,
        instance_option_id: str,
        name: str,
        project_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        autoscaling_policy: OptionalNullable[
            Union[models.AutoscalingPolicy, models.AutoscalingPolicyTypedDict]
        ] = UNSET,
        hf_model_repo_revision: OptionalNullable[str] = UNSET,
        initial_version_comment: OptionalNullable[str] = UNSET,
        simplescale: OptionalNullable[
            Union[
                models.EndpointSimplescaleConfig,
                models.EndpointSimplescaleConfigTypedDict,
            ]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Create a new endpoint

        Create a new endpoint and return its status

        :param advanced: Endpoint advanced config.
        :param hf_model_repo: HF ID of the model.
        :param instance_option_id: The ID of the instance option.
        :param name: The name of the endpoint.
        :param project_id: The ID of the project that owns the endpoint.
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param autoscaling_policy: The auto scaling configuration of the endpoint.
        :param hf_model_repo_revision: HF commit hash of the model.
        :param initial_version_comment: The comment for the initial version.
        :param simplescale: The simple scaling configuration of the endpoint.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.create(
            advanced=advanced,
            hf_model_repo=hf_model_repo,
            instance_option_id=instance_option_id,
            name=name,
            project_id=project_id,
            x_friendli_team=x_friendli_team,
            autoscaling_policy=autoscaling_policy,
            hf_model_repo_revision=hf_model_repo_revision,
            initial_version_comment=initial_version_comment,
            simplescale=simplescale,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def list(
        self,
        *,
        project_id: OptionalNullable[str] = "",
        cursor: OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointListResponse:
        """List all endpoints

        List all endpoint statuses

        :param project_id: The ID of the project. If omitted, query all endpoints under the team.
        :param cursor: Cursor for pagination
        :param limit: Limit of items per page
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.list(
            project_id=project_id,
            cursor=cursor,
            limit=limit,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointSpec:
        """Get endpoint specification

        Get the specification of an endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.get(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def update(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        advanced: OptionalNullable[
            Union[models.EndpointAdvancedConfig, models.EndpointAdvancedConfigTypedDict]
        ] = UNSET,
        autoscaling_policy: OptionalNullable[
            Union[models.AutoscalingPolicy, models.AutoscalingPolicyTypedDict]
        ] = UNSET,
        hf_model_repo: OptionalNullable[str] = UNSET,
        hf_model_repo_revision: OptionalNullable[str] = UNSET,
        instance_option_id: OptionalNullable[str] = UNSET,
        name: OptionalNullable[str] = UNSET,
        new_version_comment: OptionalNullable[str] = UNSET,
        simplescale: OptionalNullable[
            Union[
                models.EndpointSimplescaleConfig,
                models.EndpointSimplescaleConfigTypedDict,
            ]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointSpec:
        """Update endpoint spec

        Update the specification of a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param advanced: The advanced configuration of the endpoint.
        :param autoscaling_policy: The auto scaling configuration of the endpoint.
        :param hf_model_repo: HF ID of the model.
        :param hf_model_repo_revision: HF commit hash of the model.
        :param instance_option_id: The ID of the instance option.
        :param name: The name of the endpoint.
        :param new_version_comment: Comment for the new version.
        :param simplescale: The simple scaling configuration of the endpoint.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.update(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            advanced=advanced,
            autoscaling_policy=autoscaling_policy,
            hf_model_repo=hf_model_repo,
            hf_model_repo_revision=hf_model_repo_revision,
            instance_option_id=instance_option_id,
            name=name,
            new_version_comment=new_version_comment,
            simplescale=simplescale,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def delete(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Delete endpoint

        Delete a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.delete(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_version(
        self,
        *,
        endpoint_id: str,
        cursor: OptionalNullable[Union[bytes, IO[bytes], io.BufferedReader]] = UNSET,
        limit: OptionalNullable[int] = 20,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Dict[str, models.DedicatedEndpointSpec]:
        """Get endpoint versions

        Get versions of a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param cursor: Cursor for pagination
        :param limit: Limit of items per page
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.get_version(
            endpoint_id=endpoint_id,
            cursor=cursor,
            limit=limit,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def get_status(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Get endpoint status

        Get the status of a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._core.dedicated.endpoint.get_status(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def sleep(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Sleep endpoint

        Put a specific endpoint to sleep

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.sleep(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def wake(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Wake endpoint

        Wake up a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.wake(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def terminate(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Terminate endpoint

        Terminate a specific endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self.core.dedicated.endpoint.terminate(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )

    async def restart(
        self,
        *,
        endpoint_id: str,
        x_friendli_team: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DedicatedEndpointStatus:
        """Restart endpoint

        Restart a FAILED or TERMINATED endpoint

        :param endpoint_id: The ID of the endpoint
        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return await self._core.dedicated.endpoint.restart(
            endpoint_id=endpoint_id,
            x_friendli_team=x_friendli_team,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
