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
