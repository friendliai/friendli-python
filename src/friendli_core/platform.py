"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from abc import abstractmethod

from friendli_core.files import AsyncFiles, SyncFiles

from .basesdk import AsyncSDK, BaseSDK, SyncSDK
from .sdkconfiguration import SDKConfiguration


class BasePlatform(BaseSDK):
    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    @abstractmethod
    def _init_sdks(self):
        pass


class SyncPlatform(BasePlatform, SyncSDK):
    files: SyncFiles

    def _init_sdks(self):
        self.files = SyncFiles(self.sdk_configuration)


class AsyncPlatform(BasePlatform, AsyncSDK):
    files: AsyncFiles

    def _init_sdks(self):
        self.files = AsyncFiles(self.sdk_configuration)
