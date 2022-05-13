import unittest

from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase


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
        self.assertEqual(1, config["a"])
        self.assertEqual(None, config["b"])
        self.assertEqual(3, config["c"])
        self.assertEqual(4, config["d"])

    def test_merge(self):
        config0 = {
            "a": 1,
            "b": 2
        }

        config1 = {
            "b": 3,
            "d": 5,
            "e": {
                "f": [2]
            }
        }

        config2 = {
            "e": {"g": 3},
            "a": 7
        }

        config = self.cs.merge(config0, config1, config2)

        self.assertDictEqual({
            "a": 7,
            "b": 3,
            "d": 5,
            "e": {
                "g": 3
            }
        }, config)

    def test_convert_to_config(self):
        self.assertTrue(self.cs.config)

        self.assertEqual(self.cs.config.ident.wait_seconds_for_object, 30)
        self.assertEqual(self.cs.config.common.log_level, "info")
        self.assertEqual(self.cs.config.script.is_snapshot_before_action, False)
