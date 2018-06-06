device = None


def before():
    device.wakeup()


def after():
    device.sleep()


def run():
    device.swipe(500, 1000, 500, 0, steps=10)
    device.wait.update()
    device.press.home()

