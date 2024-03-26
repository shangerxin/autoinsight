from autoinsight import StartMenu, SearchBox, WindowOS, Wait
from multiprocess import freeze_support


if __name__ == '__main__':
    freeze_support()
    WindowOS().setCurrent()
    StartMenu().click()
    Wait(5)
    SearchBox().type('Intel DCAI demo')
