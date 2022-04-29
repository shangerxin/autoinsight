import os
import sys
import unittest

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
current_dir = os.path.dirname(__file__)

if __name__ == "__main__:":
    loader = unittest.TestLoader()
    tests = loader.discover(current_dir, pattern="test*.py")
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTest(test)

    unittest.TextTestRunner().run(suite)
