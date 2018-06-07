import time


class CustomAPI(object):
    def __init__(self, device_instance):
        self._device_instance = device_instance

    def clean_recent(self):
        self._device_instance.press('recent')
        time.sleep(1)
        self._device_instance(
            resourceId='com.coloros.recents:id/clear_button'
        ).click()
