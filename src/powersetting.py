from autoinsight.ident.context.WindowOS import WindowOS
from autoinsight import Button, Wait
from multiprocess import freeze_support


if __name__ == '__main__':
    freeze_support()
    window = WindowOS()
    control_panel = window.launchApp("control panel")
    control_panel.setCurrent()
    Button("Power Options").click()
    Button("Change plan settings").click()
    Wait(10)
    control_panel.close()

