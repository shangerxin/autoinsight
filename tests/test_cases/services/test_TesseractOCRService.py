import os.path
import unittest
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
sys.path.insert(0, PROJECT_PATH)

from PIL import Image

from autoinsight.common.models.BoundingBox import BoundingBox
from autoinsight.services.TesseractOCRService import TesseractOCRService
from autoinsight.common.Utils import first
import tests.fixtures as fixtures


class TestTesseractOCRService(unittest.TestCase):
    def setUp(self):
        self.ocr: TesseractOCRService = TesseractOCRService()
        self.image = Image.open(os.path.join(fixtures.fixtureImageRoot, "tk_window_input_ok_button_gray.png"))

    def test_getText(self):
        result = self.ocr.getTextFromImage(self.image)
        self.assertTrue("OK" in result)

    def test_getbox(self):
        result: list[BoundingBox] = self.ocr.getBoxFromImage(self.image)

        self.assertTrue(result)
        self.assertTrue(first(result, filterFunc=lambda x: x.char == "O"))
        self.assertTrue(first(result, filterFunc=lambda x: x.char == "K"))


if __name__ == '__main__':
    unittest.main()
