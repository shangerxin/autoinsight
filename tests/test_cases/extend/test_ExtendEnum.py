import unittest

from autoinsight.common.EnumTypes import OSTypes


class TestExtendEnum(unittest.TestCase):
    def test_extend_enum_fromstr_with_OSTypes(self):
        window = OSTypes.fromStr("Windows")
        linux = OSTypes.fromStr("Linux")
        unknown = OSTypes.fromStr("Unknown")

        self.assertEqual(window, OSTypes.Windows)
        self.assertEqual(linux, OSTypes.Linux)
        self.assertEqual(unknown, None)
