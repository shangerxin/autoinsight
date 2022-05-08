import unittest

from autoinsight.common.EnumTypes import OSTypes


class TestExtendEnum(unittest.TestCase):
    def test_extend_enum_fromstr_with_OSTypes(self):
        window = OSTypes.fromStr("Windows")
        linux = OSTypes.fromStr("Linux")
        unknown = OSTypes.fromStr("Unknown")
        default = OSTypes.fromStr("Unknown", OSTypes.Any)

        self.assertEqual(window, OSTypes.Windows)
        self.assertEqual(linux, OSTypes.Linux)
        self.assertEqual(unknown, None)
        self.assertEqual(default, OSTypes.Any)

    def test_value_to_str(self):
        self.assertEqual("Windows", OSTypes.Windows.str)
