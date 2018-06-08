import time
from basic_uia.basecase import BaseTestCase


class TestCase(BaseTestCase):
    def before(self):
        # unlock
        self.device.wakeup()
        self.device.swipe(500, 1000, 500, 0, steps=10)

        # 调用adb命令
        self.adb('shell am start -n com.nearme.instant.platform/a.a.a.bdf')
        # 上面这一句即：
        # adb -s YOUR_DEVICE_ID shell am start -n ......
        # 其他调用同理

        time.sleep(1)
        self.device.press('home')
        time.sleep(1)
    
    def after(self):
        # 这里可以添加一些后置操作
        # 如果不用 可以不要这个函数
        pass
    
    def start(self):
        # 调用公用API，见 basic_uia/api.py
        # self.api.xxx()

        # 启动快捷入口
        self.device.swipe(500, 400, 500, 1000, steps=10)
        time.sleep(2)
        self.assertTrue(self.device(text="搜索").exists)
        self.device(text="搜索").set_text("饿了么")
        time.sleep(2)
        self.assertTrue(self.device(text="秒开").exists)
        self.device(text="秒开").click()
        time.sleep(2)
        self.assertTrue(self.device(text="饿了么").exists)
