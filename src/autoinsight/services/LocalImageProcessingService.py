from os.path import isfile
from typing import Optional, Union, Sequence

import cv2 as cv
import colour
import numpy as np
from PIL.Image import Image, open as imageopen, fromarray

from .ImageProcessingServiceBase import ImageProcessingServiceBase
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.decorator.Log import log
from autoinsight.common.models.Size import Size
from autoinsight.common.EnumTypes import CVImageTypes

IMG = Union[str, Image, np.array]


class LocalImageProcessingService(ImageProcessingServiceBase):
    @log
    def getImageResolution(self, image: IMG) -> Optional[Size]:
        image = self._img2pil(image)
        result = Size(*image.size)
        image.close()
        return result

    @log
    def compareBrightness(self, imageA: IMG, imageB: IMG) -> int:
        """
        Compare two image brightness

        @param imageA PIL image
        @param imageB PIL image
        @return negative, 0, positive integer
        """
        imageA = self._img2pil(imageA)
        imageB = self._img2pil(imageB)
        cvImageA = self._pil2cv(imageA)
        cvImageB = self._pil2cv(imageB)
        histA = cv.calcHist([self._toGray(cvImageA)], [0], None, [256], [0, 256])
        histB = cv.calcHist([self._toGray(cvImageB)], [0], None, [256], [0, 256])
        result = np.sum((histA - histB) * np.array([[x] for x in range(0, 256)]))
        imageA.close()
        imageB.close()
        return int(result)

    @log
    def compareSharpness(self, imageA: IMG, imageB: IMG) -> int:
        pass

    @log
    def compareNoise(self, imageA: IMG, imageB: IMG) -> int:
        pass

    @log
    def compareFocusResult(self, imageA: IMG, imageB: IMG, rectangle: Rectangle) -> int:
        pass

    @log
    def compareImageISO(self, imageA: IMG, imageB: IMG) -> int:
        pass

    @log
    def compareVideoISO(self, videoA: Image, videoB: Image, checkpoint: float = 0.0) -> int:
        pass

    @log
    def compareImageContrast(self, imageA: IMG, imageB: IMG) -> int:
        imageA = self._img2pil(imageA)
        imageB = self._img2pil(imageB)
        cvImageA = self._toGray(self._pil2cv(imageA))
        cvImageB = self._toGray(self._pil2cv(imageB))
        histA = cv.calcHist([cvImageA], [0], None, [256], [0, 256])
        histB = cv.calcHist([cvImageB], [0], None, [256], [0, 256])
        contrastMeasureA = self._measureContrast(histA.flatten())
        contrastMeasureB = self._measureContrast(histB.flatten())
        return contrastMeasureA - contrastMeasureB

    @log
    def compareVideoContrast(self, videoA, videoB, checkpoint: float = 0.0) -> int:
        pass

    @log
    def compareImageGamma(self, imageA: IMG, imageB: IMG) -> int:
        """
        TODO: Add gamma calculation logic
        """
        return self.compareBrightness(imageA, imageB)

    @log
    def compareVideoGamma(self, videoA, videoB, checkpoint: float = 0.0) -> int:
        pass

    @log
    def getBSODInfo(self, image) -> str:
        pass

    @log
    def getImageColorTemperature(self, image: IMG) -> float:
        r, g, b = self.getImageRGBMean(image)
        # Assuming sRGB encoded colour values.
        RGB = np.array([r, g, b])
        # Conversion to tristimulus values.
        XYZ = colour.sRGB_to_XYZ(RGB / 255)
        # Conversion to chromaticity coordinates.
        xy = colour.XYZ_to_xy(XYZ)
        # Conversion to correlated colour temperature in K.
        return colour.xy_to_CCT(xy, 'hernandez1999')

    @log
    def getVideoColorTemperature(self, video, checkpoint: float = 0.0) -> int:
        pass

    @log
    def getImageHSVMean(self, image: IMG):
        image = self._img2pil(image)
        cvimage = self._pil2cv(image, CVImageTypes.BGR)
        hsv = cv.cvtColor(cvimage, cv.COLOR_BGR2HSV)
        image.close()
        return np.mean(hsv, axis=(0, 1))

    @log
    def getVideoHSVMean(self, video, checkpoint: float = 0.0) -> int:
        pass

    @log
    def getImageRGBMean(self, image: IMG) -> Sequence[int]:
        image = self._img2pil(image)
        cvimage = self._pil2cv(image, CVImageTypes.RGB)
        image.close()
        return np.mean(cvimage, axis=(0, 1))

    @log
    def getVideoRGBMean(self, video, checkpoint: float) -> Sequence[int]:
        pass

    @log
    def getBrightestRegion(self, image: IMG) -> Rectangle:
        pass

    @log
    def getDarkestRegion(self, image: IMG) -> Rectangle:
        pass

    @log
    def getImageISO(self, image: IMG) -> int:
        pass

    @log
    def getVideoISO(self, video, checkpoint: float = 0.0) -> int:
        pass

    @log
    def isVideoStutter(self, video) -> bool:
        pass

    @log
    def isVideoFlicker(self, video) -> bool:
        pass

    @log
    def isContainObject(self, image: IMG, target: IMG) -> bool:
        image = self._img2pil(image)
        target = self._img2pil(target)
        cvimage = self._toGray(self._pil2cv(image))
        cvtarget = self._toGray(self._pil2cv(target))
        image.close()
        target.close()
        return np.any(np.where(cv.matchTemplate(cvimage, cvtarget, cv.TM_CCOEFF_NORMED) > 0.4))

    @log
    def isPrivacyLEDOn(self, imageA: IMG, imageB: IMG) -> bool:
        pass

    @log
    def isImageCorrupted(self, image: IMG) -> bool:
        pass

    @classmethod
    @log
    def _img2pil(cls, image: IMG) -> Image:
        if isinstance(image, str) and isfile(image):
            return imageopen(image)
        elif isinstance(image, np.ndarray):
            return fromarray(image)
        else:
            return image

    @classmethod
    @log
    def _toGray(cls, image: np.ndarray):
        if len(image.shape) > 2:
            image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        return image

    @classmethod
    @log
    def _pil2np(cls, image: IMG):
        return np.frombuffer(image.tobytes(), dtype=np.uint8)

    @classmethod
    @log
    def _pil2cv(cls, image: IMG, imageType: CVImageTypes = CVImageTypes.RGB):
        image = cls._img2pil(image)

        if imageType == CVImageTypes.RGB:
            nparray = cls._pil2np(image.convert('RGB'))
            # 3 or 4 base on your image mode is RGB or RGBA
            nparray.shape = (*reversed(image.size), 3)
            return nparray
        elif imageType == CVImageTypes.RGBA:
            nparray = cls._pil2np(image.convert('RGBA'))
            nparray.shape = (*reversed(image.size), 4)
            return nparray
        else:
            nparray = cls._pil2np(image.convert('RGB'))
            nparray.shape = (*reversed(image.size), 3)
            return cv.cvtColor(nparray, cv.COLOR_RGB2BGR)

    @classmethod
    @log
    def _measureContrast(cls, histogram: np.ndarray) -> int:
        leftIndex = next(i for i in range(len(histogram)) if histogram[i] != 0)
        rightIndex = next(i for i in range(len(histogram) - 1, -1, -1) if histogram[i] != 0)
        points = []
        i, j, leftValue, rightValue, previous = 0, 0, 0, 0, 0

        while True:
            left = leftIndex + i
            right = rightIndex - j
            leftValue -= histogram[left]
            rightValue += histogram[right]
            total = leftValue + rightValue

            if total < 0:
                leftValue += rightValue
                j += 1
            elif total > 0:
                rightValue += leftValue
                i += 1
            else:
                i += 1
                j += 1

            value = min(abs(leftValue), abs(rightValue)) * 2

            if total * previous <= 0:
                points.append(value)
            else:
                points[-1] += value

            if left >= right:
                break
            else:
                previous = total

        points.reverse()
        return int(sum(((i + 1) * v for i, v in enumerate(points))))
