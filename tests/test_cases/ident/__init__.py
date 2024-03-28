import os
import sys
import unittest

PROJECT_PATH = os.getcwd().replace(r'tests\test_cases\ident\__init__.py', '')
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
current_dir = os.path.dirname(__file__)
