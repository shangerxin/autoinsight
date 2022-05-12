import unittest

from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase


@unittest.skip
class TestConfigurationService(unittest.TestCase):
    def setUp(self) -> None:
        self.cs = ConfigurationServiceBase()

    def test_load(self):
        config = self.cs.load("""
            a: 1
            b:
            c: 3
            d: 4
        """)

        self.assertTrue(config)
        self.assertEqual(1, config.a)
        self.assertEqual(None, config.b)
        self.assertEqual(3, config.c)
        self.assertEqual(4, config.d)
