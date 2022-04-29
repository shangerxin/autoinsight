import unittest


class TestImport(unittest.TestCase):
    def test_import(self):
        import autoinsight

        self.assertTrue(autoinsight)
