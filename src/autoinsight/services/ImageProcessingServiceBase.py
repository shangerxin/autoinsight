from abc import abstractmethod

from .ServiceBase import ServiceBase
from ..common.models.Rectangle import Rectangle


class ImageProcessingServiceBase(ServiceBase):
    @abstractmethod
    def getImageResolution(self, image):
        pass

    @abstractmethod
    def isImageCorrupted(self, image) -> bool:
        pass

    @abstractmethod
    def compareBrightness(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def getBSODInfo(self, image) -> str:
        pass

    @abstractmethod
    def isVideoStutter(self, video) -> bool:
        pass

    @abstractmethod
    def isVideoFlicker(self, video) -> bool:
        pass

    @abstractmethod
    def isContainObject(self, image, target) -> bool:
        pass

    @abstractmethod
    def isContainText(self, image, text: str) -> bool:
        pass

    @abstractmethod
    def compareSharpness(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareNoise(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def isPrivacyLEDOn(self, imageA, imageB) -> bool:
        pass

    @abstractmethod
    def getImageColorTemperature(self, image) -> int:
        pass

    @abstractmethod
    def getVideoColorTemperature(self, video, time) -> int:
        pass

    @abstractmethod
    def getImageHSB(self, image):
        pass

    @abstractmethod
    def getVideoHSB(self, video, time) -> int:
        pass

    @abstractmethod
    def compareFocusResult(self, imageA, imageB, rectangle) -> int:
        pass

    @abstractmethod
    def getBrightestRegion(self, image) -> Rectangle:
        pass

    @abstractmethod
    def getDarkestRegion(self, image) -> Rectangle:
        pass

    @abstractmethod
    def getImageISO(self, image) -> int:
        pass

    @abstractmethod
    def getVideoISO(self, video, time) -> int:
        pass

    @abstractmethod
    def compareImageISO(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareVideoISO(self, videoA, videoB, time) -> int:
        pass

    @abstractmethod
    def compareImageContrast(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareVideoContrast(self, videoA, videoB, time) -> int:
        pass

    @abstractmethod
    def compareImageGamma(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareVideoGamma(self, videoA, videoB, time) -> int:
        pass
