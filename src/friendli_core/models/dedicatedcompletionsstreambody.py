"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Union

from typing_extensions import TypeAliasType

from .completionsstreamdedicatedbodywithprompt import (
    CompletionsStreamDedicatedBodyWithPrompt,
    CompletionsStreamDedicatedBodyWithPromptTypedDict,
)
from .completionsstreamdedicatedbodywithtokens import (
    CompletionsStreamDedicatedBodyWithTokens,
    CompletionsStreamDedicatedBodyWithTokensTypedDict,
)

DedicatedCompletionsStreamBodyTypedDict = TypeAliasType(
    "DedicatedCompletionsStreamBodyTypedDict",
    Union[
        CompletionsStreamDedicatedBodyWithPromptTypedDict,
        CompletionsStreamDedicatedBodyWithTokensTypedDict,
    ],
)


DedicatedCompletionsStreamBody = TypeAliasType(
    "DedicatedCompletionsStreamBody",
    Union[
        CompletionsStreamDedicatedBodyWithPrompt,
        CompletionsStreamDedicatedBodyWithTokens,
    ],
)
