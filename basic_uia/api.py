import time
import os
import importlib

import config as cf
import basic_uia.logger as logger

KEY_MAP = {
    'q': 16,
    'w': 17,
    'e': 18,
    'r': 19,
    't': 20,
    'y': 21,
    'u': 22,
    'i': 23,
    'o': 24,
    'p': 25,

    'a': 30,
    's': 31,
    'd': 32,
    'f': 33,
    'g': 34,
    'h': 35,
    'j': 36,
    'k': 37,
    'l': 38,

    'z': 44,
    'x': 45,
    'c': 46,
    'v': 47,
    'b': 48,
    'n': 49,
    'm': 50,
}


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

    def single_type_input(self, single_letter):
        letter = str(single_letter.lower())
        hex_value = hex(KEY_MAP[letter])
        self.device.press(hex_value)

    def long_type_input(self, full_str):
        target_str = str(full_str).lower()
        for each_letter in list(target_str):
            self.single_type_input(each_letter)

    def enter_home_page(self):
        """ 返回首页第一屏 """
        for _ in range(5):
            self.device.press('home')
