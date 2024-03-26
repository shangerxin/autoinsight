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
    Button("Turn off the display on battery").click()
    # 1 2 3 5 10 15 20 25 30 45 1 hours
    Button("2 minutes").click()
    Button("Save changes").click()
    Wait(3)
    control_panel.close()

