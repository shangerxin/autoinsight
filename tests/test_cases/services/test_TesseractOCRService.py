import os.path
import unittest

from PIL import Image

from autoinsight.common.models.Box import Box
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
