from abc import abstractmethod
from typing import Tuple, Optional

from PIL import Image
from numpy import array
from requests import post, get, Response

from autoinsight.common.models.BoundingBox import BoundingBox
from .ServiceBase import ServiceBase


class OCRServiceBase(ServiceBase):

    @classmethod
    def _getImageFromURL(cls, auth, imageUrl, payload):
        if payload:
            result: Response = post(imageUrl, data=payload, auth=auth)
        else:
            result: Response = get(imageUrl, auth=auth)
        ok = 200
        if result.status_code == ok:
            mode = result.headers["mode"]
            width = int(result.headers["width"])
            height = int(result.headers["height"])
            image = Image.frombuffer(mode, (width, height), result.content)
        return image

    @abstractmethod
    def getTextFromImageFile(self, imagePath) -> str:
        pass

    @abstractmethod
    def getTextFromImageBinary(self, imageBinary: bytes, mode: str, size: Tuple[int, int]) -> str:
        pass

    @abstractmethod
    def getTextFromImage(self, image: Image) -> str:
        pass

    @abstractmethod
    def getTextFromImageUrl(self, imageUrl: str, payload: str, auth: Optional[Tuple[str, str]] = None) -> str:
        pass

    @abstractmethod
    def getTextFromImageArray(self, imageArray: array) -> str:
        pass

    @abstractmethod
    def getBoxFromImageFile(self, imagePath) -> Optional[list[BoundingBox]]:
        pass

    @abstractmethod
    def getBoxFromImageBinary(self, imageBinary: bytes, mode: str, size: Tuple[int, int]) -> Optional[list[BoundingBox]]:
        pass

    @abstractmethod
    def getBoxFromImage(self, image: Image) -> Optional[list[BoundingBox]]:
        pass

    @abstractmethod
    def getBoxFromImageUrl(self, imageUrl: str,
                           payload: str = None,
                           auth: Optional[Tuple[str, str]] = None) -> Optional[list[BoundingBox]]:
        pass

    @abstractmethod
    def getBoxFromImageArray(self, imageArray: array) -> Optional[list[BoundingBox]]:
        pass
