import time
import os
import importlib
import config as cf
import basic_uia.logger as logger


def load_extend_api(module_class):
    if os.path.exists(cf.EXTEND_API_FILE):
        extend_api_module = importlib.import_module(os.path.splitext(cf.EXTEND_API_FILE_NAME)[0])
        module_class.extend_api = extend_api_module.ExtendAPI(
            module_class.device, module_class.adb, module_class.log)
        logger.info('extend api ready.')
    else:
        logger.info('no extend api detected.')


class CustomAPI(object):
    def __init__(self, device_instance, adb_instance, log_instance):
        self.device = device_instance
        self.adb = adb_instance
        self.log = log_instance
        load_extend_api(self)

    def __getattr__(self, item):
        if not hasattr(self.extend_api, item):
            raise ModuleNotFoundError('{} not found in extend api'.format(item))
        target_func = getattr(self.extend_api, item)
        return target_func

    def clean_recent(self):
        self.device.press('recent')
        time.sleep(1)
        self.device(
            resourceId='com.coloros.recents:id/clear_button'
        ).click()
