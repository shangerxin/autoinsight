from abc import abstractmethod
from typing import Optional, Sequence

from .ServiceBase import ServiceBase
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.common.models.Size import Size


class ImageProcessingServiceBase(ServiceBase):
    @abstractmethod
    def getImageResolution(self, image) -> Optional[Size]:
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
    def getVideoColorTemperature(self, video, checkpoint) -> int:
        pass

    @abstractmethod
    def getImageHSVMean(self, image) -> Sequence[int]:
        pass

    @abstractmethod
    def getVideoHSVMean(self, video, checkpoint) -> int:
        pass

    @abstractmethod
    def getImageRGBMean(self, image) -> Sequence[int]:
        pass

    @abstractmethod
    def getVideoRGBMean(self, video, checkpoint) -> Sequence[int]:
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
    def getVideoISO(self, video, checkpoint) -> int:
        pass

    @abstractmethod
    def compareImageISO(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareVideoISO(self, videoA, videoB, checkpoint) -> int:
        pass

    @abstractmethod
    def compareImageContrast(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareVideoContrast(self, videoA, videoB, checkpoint) -> int:
        pass

    @abstractmethod
    def compareImageGamma(self, imageA, imageB) -> int:
        pass

    @abstractmethod
    def compareVideoGamma(self, videoA, videoB, checkpoint) -> int:
        pass
