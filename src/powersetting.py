from autoinsight import Button, Wait, WindowOS


if __name__ == '__main__':
    window = WindowOS()
    control_panel = window.launchApp("control panel")
    control_panel.setCurrent()
    Button("Power Options").click()
    Button("Change plan settings").click()
    Button("Turn off the display on battery").click()
    # 1 2 3 5 10 15 20 25 30 45 1 hours
    Button("20 minutes").click()
    Button("Save changes").click()
    Wait(3)
    control_panel.close()

