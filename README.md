# Introduction
autoui is a UI automation library for window. It is aim to provide simplified workflow to the automation developers to help them create a easy to maintain and robust test scripts.

It is focus on Windows in the first release. It will be migrate to Linux in the future.

# Development
- run all test
```
$ nosetests
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
    automation libraries like pywinauot, pyautogui etc.

    5. Action logging
    6. Snapshot
    7. Screen recording
