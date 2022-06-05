import unittest
import os

from autoinsight.script.Script import Script
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
        self.assertTrue(self.cs.config.common.log_format)
        self.assertEqual(self.cs.config.script.action_delay_seconds, 1)

    def test_update_config_from_script(self):
        script = Script(runtimeConfig={"dummy": "key", "ident": {"search_depth": 100}})
        self.cs.updateConfig(script)

        with self.assertRaises(AttributeError):
            self.cs.config.dummy
        self.assertEqual(os.path.join(script.location, "output"), self.cs.config.script.output_root)
        self.assertEqual(100, self.cs.config.ident.search_depth)
