# Introduction

autoinsight is a UI automation library for window. It is aim to provide simplified workflow to the automation developers
to help them create a easy to maintain and robust test scripts.

It is focus on Windows in the recent releases. It will be migrate to Linux in the future.

# Contribute to this project

- Donate
- [Contribute code](https://github.com/shangerxin/autoinsight/issues)
- Documentation

# Requirements

- OS
  Window

- Python 3.6+ 32/64 bit
- Install Google Tesseract 32/64 bit
  [tesseract wiki](https://github.com/UB-Mannheim/tesseract/wiki)

  Add tesseract.exe into the system environment variable PATH 
- 
- Install pywin32
  [pywin32 release](https://github.com/mhammond/pywin32/releases)

# Installation

- Install with pip

```
$ pip install autoinsight
```

# Quick demo

```python
from autoinsight import Button, WindowOS

def demo():
    camera = WindowOS().launchApp("camera")
    camera.setCurrent()
    Button("take photo").click()
    camera.close()

if __name__ == '__main__':
    demo()
```

# Configuration

# Development

## Setup development environment

- Setup

```
$ pip install -r requirements-dev.txt
```

- Install Google Tesseract ORC

- Run all test

```
$ nose2
```

- validate code syntax before commit

```
$ flake8
```

## Build

- Install the build dependency

```
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements-dev.txt
$ python -m build
```

## Test

- Run unit test on local machine before push to the repository

```
$ nose2
```

- Create a new test module with add the __init__.py to a new folder under the ./tests
- Name the test file with test_*.py
- Make sure each test case inherit from the unittest.TestCase
- Test

# Document and Help

- Follow syntax of the Sphinx project

# Roadmap

- 0.0.1 [Current version 0.0.8]
    1. Init the project

- 1.0.0

    1. Basic windows UI automation features
    2. Basic image based identification features
    3. Keyboard mouse handling etc.
    4. In the first version it will be built like a glue to the existing
       automation libraries like pywinauto, pyautogui etc.

    5. Action logging
    6. Snapshot
    7. Screen recording
    8. Support Google Chrome and Microsoft Edge interoperation
    9. OS interoperation
    10. Driver interoperation
    11. Integrate with image identification and computer vision

- 2.0.0
    1. Integrate with machine learning identification
    2. Integrate other browsers
    3. Add mobile support
    4. Integrate with cloud ML APIs

- 3.0.0
    1. Support NLP script
    2. Add GUI

- 4.0.0
    1. Support record and replay

- 5.0.0
    1. Support game automation

# Copyrights

[Apache Software License](http://www.apache.org/licenses/)
