"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from friendli import models, utils
from friendli._hooks import HookContext
from friendli.types import OptionalNullable, UNSET
from friendli.utils import get_security_from_env
from typing import List, Mapping, Optional


class Rag(BaseSDK):
    def knowledge_retrieve(
        self,
        *,
        x_friendli_team: Optional[str] = None,
        query: Optional[str] = None,
        k: Optional[int] = None,
        knowledge_ids: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.KnowledgeRetrieveResult:
        r"""Knowledge retrieve

        Retrieve related documents from vector store by similarity.

        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param query: A text string used to find relevant information within the knowledge-base.
        :param k: Maximum number of top-ranked knowledge-base entries to return in results.
        :param knowledge_ids: A List of knowledge-base IDs. For now, only one knowledge-base is supported.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ServerlessKnowledgeRetrieveRequest(
            x_friendli_team=x_friendli_team,
            serverless_knowledge_retrieve_body=models.ServerlessKnowledgeRetrieveBody(
                query=query,
                k=k,
                knowledge_ids=knowledge_ids,
            ),
        )

        req = self._build_request(
            method="POST",
            path="/serverless/v1/knowledge/retrieve",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.serverless_knowledge_retrieve_body,
                False,
                False,
                "json",
                models.ServerlessKnowledgeRetrieveBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="serverlessKnowledgeRetrieve",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.KnowledgeRetrieveResult)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def knowledge_retrieve_async(
        self,
        *,
        x_friendli_team: Optional[str] = None,
        query: Optional[str] = None,
        k: Optional[int] = None,
        knowledge_ids: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.KnowledgeRetrieveResult:
        r"""Knowledge retrieve

        Retrieve related documents from vector store by similarity.

        :param x_friendli_team: ID of team to run requests as (optional parameter).
        :param query: A text string used to find relevant information within the knowledge-base.
        :param k: Maximum number of top-ranked knowledge-base entries to return in results.
        :param knowledge_ids: A List of knowledge-base IDs. For now, only one knowledge-base is supported.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ServerlessKnowledgeRetrieveRequest(
            x_friendli_team=x_friendli_team,
            serverless_knowledge_retrieve_body=models.ServerlessKnowledgeRetrieveBody(
                query=query,
                k=k,
                knowledge_ids=knowledge_ids,
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/serverless/v1/knowledge/retrieve",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.serverless_knowledge_retrieve_body,
                False,
                False,
                "json",
                models.ServerlessKnowledgeRetrieveBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="serverlessKnowledgeRetrieve",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.KnowledgeRetrieveResult)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )