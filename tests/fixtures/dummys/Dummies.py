from collections import namedtuple

DummyControl = namedtuple("DummyControl", ["friendly_class_name", "id"])

DummyAutomationInstance = namedtuple("DummyAutomationInstance", ["get_elements_info"])

DummyTarget = namedtuple("DummyTarget", ["friendly_class_name", "aliases"])


def dummy_func(value):
    def func():
        return value
    return func
