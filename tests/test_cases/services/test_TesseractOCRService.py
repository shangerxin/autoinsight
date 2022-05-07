import os.path
import unittest

from PIL import Image

from autoinsight.common.models.Box import Box
from autoinsight.common.models.BoundingBox import BoundingBox
from autoinsight.services.TesseractOCRService import TesseractOCRService

import tests.fixtures as fixtures


class TestTesseractOCRService(unittest.TestCase):
    def setUp(self):
        self.ocr: TesseractOCRService = TesseractOCRService()
        self.image = Image.open(os.path.join(fixtures.fixtureImageRoot, "tk_window_input_ok_button_gray.png"))

    def test_getText(self):
        result = self.ocr.getTextFromImage(self.image)
        self.assertEqual("OK", result.strip())

    def test_getbox(self):
        result: list[BoundingBox] = self.ocr.getBoxFromImage(self.image)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], BoundingBox("O", Box(left=208, top=11, width=218, height=23)))
        self.assertEqual(result[1], BoundingBox("K", Box(left=220, top=11, width=227, height=23)))
