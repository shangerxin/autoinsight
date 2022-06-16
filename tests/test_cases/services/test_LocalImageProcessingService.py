import unittest

from autoinsight.services.LocalImageProcessingService import LocalImageProcessingService
from tests.fixtures import imagePath


class TestLocalImageProcessingService(unittest.TestCase):
    def setUp(self) -> None:
        self.ims: LocalImageProcessingService = LocalImageProcessingService()

    def test_getImageResolution(self):
        size = self.ims.getImageResolution(image=imagePath("800x600-white.png"))
        self.assertEqual(size.width, 800)
        self.assertEqual(size.height, 600)

    def test_compareBrightness(self):
        imageA = imagePath("brightness-darker.png")
        imageB = imagePath("brightness-lighter.png")
        result = self.ims.compareBrightness(imageA, imageB)

        self.assertTrue(result < 0)

    def test_getImageHSV(self):
        h, s, v = self.ims.getImageHSVMean(imagePath("saturation-lower.png"))
        h1, s1, v1, = self.ims.getImageHSVMean(imagePath("saturation-normal.png"))
        self.assertTrue(s < s1)

        h, s, v = self.ims.getImageHSVMean(imagePath("brightness-darker.png"))
        h1, s1, v1 = self.ims.getImageHSVMean(imagePath("brightness-lighter.png"))
        self.assertTrue(v < v1)

        h, s, v = self.ims.getImageHSVMean(imagePath("hue-0.png"))
        h1, s1, v1, = self.ims.getImageHSVMean(imagePath("hue-180.png"))
        self.assertTrue(h < h1)

    def test_compareImageContrast(self):
        result = self.ims.compareImageContrast(imagePath("contrast-higher.png"), imagePath("contrast-lower.png"))
        self.assertTrue(result > 0)

    def test_isContainObject(self):
        image = imagePath("awb-normal.png")
        target = imagePath("target.png")
        unknown = imagePath("white.png")

        self.assertTrue(self.ims.isContainObject(image, target))
        self.assertFalse(self.ims.isContainObject(unknown, target))

    def test_getImageRGBMean(self):
        white = imagePath("white.png")
        result = self.ims.getImageRGBMean(white)
        self.assertSequenceEqual((255, 255, 255), tuple(result))

        blue = imagePath("blue.png")
        result = self.ims.getImageRGBMean(blue)
        self.assertSequenceEqual((0, 0, 255), tuple(result))

        red = imagePath("red.png")
        result = self.ims.getImageRGBMean(red)
        self.assertSequenceEqual((255, 0, 0), tuple(result))

    def test_getImageColorTemperature(self):
        warm = imagePath("warm.png")
        cold = imagePath("cold.png")

        self.assertTrue(self.ims.getImageColorTemperature(warm) < self.ims.getImageColorTemperature(cold))
