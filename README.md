# Introduction
autoinsight is a UI automation library for window. It is aim to provide simplified workflow to the automation developers to help them create a easy to maintain and robust test scripts.

It is focus on Windows in the recent releases. It will be migrate to Linux in the future.

# Development
- Setup
```
$ pip install -r requirement-dev.txt
```

- run all test
```
$ nose2
```

- validate code syntax with
```
$ flake8
```

# Build
- Install all the development dependency
```
$ python -m pip install --upgrade pip
$ python -m pip install -r requirement.txt
```


# Roadmap
- 0.0.1
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

- 3.0.0
    1. Support NLP script
    2. Add GUI

- 4.0.0
    1. Support record and replay

- 5.0.0
    1. Support game automation
