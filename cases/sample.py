import time
from basic_uia.basecase import BaseTestCase


class TestCase(BaseTestCase):
    def before(self):
        # unlock
        self.device.wakeup()
        self.device.swipe(500, 1000, 500, 0, steps=10)
        time.sleep(2)
    
    def after(self):
        self.device.sleep()
    
    def start(self):
        # 启动快捷入口
        self.device.swipe(500, 400, 500, 1000, steps=10)
        time.sleep(2)
    
        if self.device(text="搜索").exists:
            self.device(text="搜索").set_text("饿了么")
            time.sleep(2)
            self.assertTrue(self.device(text="秒开").exists)
            self.device(text="秒开").click()
            time.sleep(2)
            self.assertTrue(self.device(text="饿了么").exists)
