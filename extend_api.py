"""
此部分用于自定义API
可以组合一些简单动作
"""
import time


class ExtendAPI(object):
    def __init__(self, device, adb, log, origin_api):
        # 调用uiautomator.device
        self.device = device
        # 调用adb命令
        # 例如 self.adb('shell am start ...')
        self.adb = adb
        # 打印分析日志
        self.log = log
        # 使用原生API（basic_uia/api.py）
        # 主要用于 在扩展API中调用原生API
        self.origin_api = origin_api

    # 新增的用例模仿着这条写就可以啦
    # 调用的方法与case中调用是一样的
    # 主要目的是为了简化重复率比较高的工作
    def screen_off_and_on(self):
        self.log.info('LOG FROM ' + __name__)
        self.device.screen_off()
        time.sleep(1)
        self.device.screen_on()
        time.sleep(1)
        self.device.swipe(500, 1000, 500, 0, duration=0.5)
        time.sleep(1)
        self.origin_api.clean_recent()
        time.sleep(1)
        self.device.press('home')
        time.sleep(1)
