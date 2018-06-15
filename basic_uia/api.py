import time
import os
import importlib

import config as cf


def load_extend_api(module_class):
    """ 加载额外API """
    if os.path.exists(cf.EXTEND_API_FILE):
        extend_api_module = importlib.import_module(os.path.splitext(cf.EXTEND_API_FILE_NAME)[0])
        module_class.extend_api = extend_api_module.ExtendAPI(
            module_class.device,
            module_class.adb,
            module_class.log,
            # TO USE ORIGIN API
            module_class,
        )


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

    # ---------------------- 自定义API ------------------------

    def clean_recent(self):
        """ 清理后台 """
        self.device.press('recent')
        time.sleep(0.5)
        self.device(
            resourceId='com.coloros.recents:id/clear_button'
        ).click()

    def input_text(self, input_str):
        self.adb('shell am broadcast -a ADB_INPUT_TEXT --es msg ' + str(input_str))

    def enter_home_page(self):
        """ 返回首页第一屏 """
        for _ in range(5):
            self.device.press('home')
