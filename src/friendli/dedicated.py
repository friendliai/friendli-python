"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from friendli.friendli_chat import FriendliChat
from friendli.friendli_completions import FriendliCompletions
from friendli.friendli_token import FriendliToken


class Dedicated(BaseSDK):
    chat: FriendliChat
    completions: FriendliCompletions
    token: FriendliToken

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.chat = FriendliChat(self.sdk_configuration)
        self.completions = FriendliCompletions(self.sdk_configuration)
        self.token = FriendliToken(self.sdk_configuration)
