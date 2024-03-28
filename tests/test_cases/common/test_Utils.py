import unittest
import os
import re

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
        self.assertEqual(0.6, secondScore)

    def test_isIEqual(self):
        str0 = "abc"
        str1 = "aBc"
        self.assertTrue(utils.isIEqual(str0, str1))

        str2 = "dbC"
        self.assertFalse(utils.isIEqual(str1, str2))

    def test_makeDirs(self):
        curPath = os.path.dirname(__file__)
        subdirs = os.path.join(curPath, "a", "bc")

        utils.makeDirs(subdirs)
        self.assertTrue(os.path.isdir(subdirs))

        tempFilePath = os.path.join(subdirs, "tmp.txt")
        fh = open(tempFilePath, "w+")
        fh.close()
        utils.makeDirs(subdirs, isRecreate=False)
        self.assertTrue(os.path.isfile(tempFilePath))

        utils.makeDirs(subdirs, isRecreate=True)
        self.assertFalse(os.path.isfile(tempFilePath))

    def test_decorateFileName(self):
        name = "abc.txt"
        decoratedName = utils.decorateFileName(name)
        self.assertTrue(re.match(r"UTC\d{8}-\d{6}\.\d{3}-abc\.txt", decoratedName))

        name = r"c:\abc.txt"
        decoratedName = utils.decorateFileName(name)
        self.assertTrue(re.match(r"c:\\UTC\d{8}-\d{6}\.\d{3}-abc\.txt", decoratedName))
