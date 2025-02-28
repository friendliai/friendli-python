"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Union

from typing_extensions import TypeAliasType

from .completionsmodelbodywithprompt import (
    CompletionsModelBodyWithPrompt,
    CompletionsModelBodyWithPromptTypedDict,
)
from .completionsmodelbodywithtokens import (
    CompletionsModelBodyWithTokens,
    CompletionsModelBodyWithTokensTypedDict,
)

DedicatedCompletionsBodyTypedDict = TypeAliasType(
    "DedicatedCompletionsBodyTypedDict",
    Union[
        CompletionsModelBodyWithPromptTypedDict, CompletionsModelBodyWithTokensTypedDict
    ],
)


DedicatedCompletionsBody = TypeAliasType(
    "DedicatedCompletionsBody",
    Union[CompletionsModelBodyWithPrompt, CompletionsModelBodyWithTokens],
)
