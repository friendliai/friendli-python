"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .completionsmodelstreambodywithprompt import (
    CompletionsModelStreamBodyWithPrompt,
    CompletionsModelStreamBodyWithPromptTypedDict,
)
from .completionsmodelstreambodywithtokens import (
    CompletionsModelStreamBodyWithTokens,
    CompletionsModelStreamBodyWithTokensTypedDict,
)
from typing import Union
from typing_extensions import TypeAliasType


DedicatedCompletionsStreamBodyTypedDict = TypeAliasType(
    "DedicatedCompletionsStreamBodyTypedDict",
    Union[
        CompletionsModelStreamBodyWithPromptTypedDict,
        CompletionsModelStreamBodyWithTokensTypedDict,
    ],
)


DedicatedCompletionsStreamBody = TypeAliasType(
    "DedicatedCompletionsStreamBody",
    Union[CompletionsModelStreamBodyWithPrompt, CompletionsModelStreamBodyWithTokens],
)
