from .ImageProcessingServiceBase import ImageProcessingServiceBase
from ..common.models.Rectangle import Rectangle


class LocalImageProcessingService(ImageProcessingServiceBase):
    def getImageResolution(self, image):
        pass

    def isImageCorrupted(self, image) -> bool:
        pass

    def compareBrightness(self, imageA, imageB) -> int:
        pass

    def getBSODInfo(self, image) -> str:
        pass

    def isVideoStutter(self, video) -> bool:
        pass

    def isVideoFlicker(self, video) -> bool:
        pass

    def isContainObject(self, image, target) -> bool:
        pass

    def isContainText(self, image, text: str) -> bool:
        pass

    def compareSharpness(self, imageA, imageB) -> int:
        pass

    def compareNoise(self, imageA, imageB) -> int:
        pass

    def isPrivacyLEDOn(self, imageA, imageB) -> bool:
        pass

    def getImageColorTemperature(self, image) -> int:
        pass

    def getVideoColorTemperature(self, video, time) -> int:
        pass

    def getImageHSB(self, image):
        pass

    def getVideoHSB(self, video, time) -> int:
        pass

    def compareFocusResult(self, imageA, imageB, rectangle) -> int:
        pass

    def getBrightestRegion(self, image) -> Rectangle:
        pass

    def getDarkestRegion(self, image) -> Rectangle:
        pass

    def getImageISO(self, image) -> int:
        pass

    def getVideoISO(self, video, time) -> int:
        pass

    def compareImageISO(self, imageA, imageB) -> int:
        pass

    def compareVideoISO(self, videoA, videoB, time) -> int:
        pass

    def compareImageContrast(self, imageA, imageB) -> int:
        pass

    def compareVideoContrast(self, videoA, videoB, time) -> int:
        pass

    def compareImageGamma(self, imageA, imageB) -> int:
        pass

    def compareVideoGamma(self, videoA, videoB, time) -> int:
        pass
