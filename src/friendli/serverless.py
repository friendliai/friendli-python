"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from friendli.chat import Chat
from friendli.completions import Completions
from friendli.token import Token
from friendli.toolassistedchat import ToolAssistedChat


class Serverless(BaseSDK):
    chat: Chat
    completions: Completions
    token: Token
    tool_assisted_chat: ToolAssistedChat

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.chat = Chat(self.sdk_configuration)
        self.completions = Completions(self.sdk_configuration)
        self.token = Token(self.sdk_configuration)
        self.tool_assisted_chat = ToolAssistedChat(self.sdk_configuration)
