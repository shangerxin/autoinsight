import unittest

import autoinsight.common.Utils as utils


class TestUtils(unittest.TestCase):
    def test_GUID_unique_validation(self):
        guid0 = utils.GUID()
        guid1 = utils.GUID()

        self.assertNotEqual(guid0, guid1)

        strGuid0 = utils.strGUID()
        strGuid1 = utils.strGUID()

        self.assertNotEqual(strGuid0, strGuid1)

    def test_GUID_conversions(self):
        guid = utils.GUID()
        strGuid = str(guid)

        self.assertEqual(guid, utils.strToGUID(strGuid))

    def test_unique_list(self):
        words = ['Brightness at 132Button', 'Brightness at 132', 'Button5']
        uniqueWords = utils.toUniqueList(words)
        self.assertEqual(["brightness", "at", "132", "button", "5"], uniqueWords)

        words = ['Switch to Video mode', 'Button6', 'Switch to Video modeButton']
        uniqueWords = utils.toUniqueList(words)
        self.assertEqual(["switch", "to", "video", "mode", "button", "6"], uniqueWords)

    def test_matchScore(self):
        words = ['Brightness at 132Button', 'Brightness at 132', 'Button5']
        query = "button 5"

        score, secondScore = utils.matchScore(query, descriptions=words)

        self.assertEqual(1, score)
        self.assertEqual(2 / 5, secondScore)

    def test_isIEqual(self):
        str0 = "abc"
        str1 = "aBc"
        self.assertTrue(utils.isIEqual(str0, str1))

        str2 = "dbC"
        self.assertFalse(utils.isIEqual(str1, str2))
