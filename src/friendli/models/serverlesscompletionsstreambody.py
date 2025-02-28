"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Union

from typing_extensions import TypeAliasType

from .completionsstreambodywithprompt import (
    CompletionsStreamBodyWithPrompt,
    CompletionsStreamBodyWithPromptTypedDict,
)
from .completionsstreambodywithtokens import (
    CompletionsStreamBodyWithTokens,
    CompletionsStreamBodyWithTokensTypedDict,
)

ServerlessCompletionsStreamBodyTypedDict = TypeAliasType(
    "ServerlessCompletionsStreamBodyTypedDict",
    Union[
        CompletionsStreamBodyWithPromptTypedDict,
        CompletionsStreamBodyWithTokensTypedDict,
    ],
)


ServerlessCompletionsStreamBody = TypeAliasType(
    "ServerlessCompletionsStreamBody",
    Union[CompletionsStreamBodyWithPrompt, CompletionsStreamBodyWithTokens],
)
