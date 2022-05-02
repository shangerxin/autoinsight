from typing import Tuple, Optional, Literal, Iterable

import pytesseract
from PIL import Image
from numpy import array

from autoinsight.common.models.Box import Box
from autoinsight.common.models.BoundingBox import BoundingBox
from .OCRService import OCRServiceBase


class TesseractOCRService(OCRServiceBase):

    def getTextFromImageFile(self, imagePath) -> str:
        return pytesseract.image_to_string(Image.open(imagePath))

    def getTextFromImageBinary(self, imageBinary: bytes, mode: str, size: Tuple[int, int]) -> str:
        mode: Literal["1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"] = mode
        return pytesseract.image_to_string(Image.frombuffer(mode, size, imageBinary))

    def getTextFromImage(self, image: Image) -> str:
        return pytesseract.image_to_string(image)

    def getTextFromImageUrl(self, imageUrl: str, payload: str, auth: Optional[Tuple[str, str]] = None) -> str:
        image = self._getImageFromURL(auth, imageUrl, payload)
        return pytesseract.image_to_string(image)

    def getTextFromImageArray(self, imageArray: array) -> str:
        return pytesseract.image_to_string(array)

    def getBoxFromImageFile(self, imagePath) -> Optional[list[BoundingBox]]:
        return pytesseract.image_to_boxes(Image.open(imagePath))

    def getBoxFromImageBinary(self,
                              imageBinary: bytes,
                              mode: str,
                              size: Tuple[int, int]) -> Optional[list[BoundingBox]]:
        mode: Literal["1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"] = mode
        return pytesseract.image_to_boxes(Image.frombuffer(mode, size, imageBinary))

    def getBoxFromImage(self, image: Image) -> Optional[list[BoundingBox]]:
        return self._parseBox(pytesseract.image_to_boxes(image))

    def getBoxFromImageUrl(self, imageUrl: str,
                           payload: str = None,
                           auth: Tuple[str, str] = None) -> Optional[list[BoundingBox]]:
        image = self._getImageFromURL(auth, imageUrl, payload)
        return pytesseract.image_to_boxes(image)

    def getBoxFromImageArray(self, imageArray: array) -> Optional[list[BoundingBox]]:
        return pytesseract.image_to_boxes(array)

    @classmethod
    def _parseBox(cls, boxesDescription: str) -> Optional[list[BoundingBox]]:
        if boxesDescription:
            boxes: list = []
            for line in boxesDescription.split("\n"):
                if line:
                    items: Iterable[str] = line.split(" ")
                    char = items[0]
                    left, top, width, height = [int(item) for item in items[1:5]]
                    boxes.append(BoundingBox(char,
                                             Box(left, top, width, height)))
            return boxes
