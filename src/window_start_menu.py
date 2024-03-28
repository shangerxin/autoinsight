from autoinsight import StartMenu, SearchBox, WindowOS, Wait


if __name__ == '__main__':
    WindowOS().setCurrent()
    StartMenu().click()
    Wait(5)
    SearchBox().type('Intel DCAI demo')
