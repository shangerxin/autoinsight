import uiauto

# explicit configure execution ambiance
uiauto.ambiance()

with Script(config=config()):
    os = OSContext()
    app = AppConext()

    os.setCurrent()
    Button().highlight() \
            .click()
    TextBox().type()

    Panel().snapshot()
    Button.text
    DropDown.value
    app.snapShot()
    app.setCurrent()

    Step.parallel(lambda x: action)

    os.Launch()
    os.snapShot()

    app.close()
