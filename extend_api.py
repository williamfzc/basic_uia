"""
此部分用于自定义API
可以组合一些简单动作
"""
import time


class ExtendAPI(object):
    def __init__(self, device, adb, log):
        self.device = device
        self.adb = adb
        self.log = log

    # 新增的用例模仿着这条写就可以啦
    # 调用的方法与case中调用是一样的
    # 主要目的是为了简化重复率比较高的工作
    def screen_off_and_on(self):
        self.log.info('Now in class: ' + __name__)
        self.device.sleep()
        time.sleep(1)
        self.device.wakeup()
        self.device.swipe(500, 1000, 500, 0, steps=10)
        time.sleep(1)
        self.device.press('home')
        time.sleep(1)
