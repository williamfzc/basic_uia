"""
本例为 测试用例 对应的脚本文件
新开发的测试用例可以此为蓝本
"""
import time
from basic_uia.basecase import BaseTestCase


class TestCase(BaseTestCase):
    def before(self):
        """
        前置操作，在用例真正逻辑进行之前的环境配置可以写在这里
        例如，在测试前需要先解锁，或进入到某个页面
        """
        pass

    def after(self):
        # 这里可以添加一些后置操作，环境清理的操作
        # 如果不用 可以不要这个函数
        # 当然before也是可以不要的
        pass
    
    def start(self):
        # 输出log，用于分析
        self.log.info('LOG FROM ' + self.case_name)

        # 调用 uiautomator 的API
        # 详情可以参见 https://github.com/xiaocong/uiautomator 中的文档
        # 这里是一个唤醒操作与滑动操作的例子
        self.device.wakeup.abc()
        self.device.swipe(500, 1000, 500, 0, steps=10)

        # 调用adb命令，下面这一句即：
        # adb -s YOUR_DEVICE_ID shell am start -n ......
        # 推荐使用该方式而不是os或subprocess强行调用
        self.adb('shell am start -n com.nearme.instant.platform/a.a.a.bdf')

        # 耗时操作直接使用time模块进行停等
        time.sleep(1)
        self.device.press('home')
        time.sleep(1)

        # 调用公用API，见 basic_uia/api.py
        # 例如
        # self.api.clean_recent()

        # 调用额外的API，配置在extend_api.py中
        # 调用方法同原生API
        self.api.screen_off_and_on()

        # 下面是一个组合起来的例子
        # 启动快捷入口
        self.device.swipe(500, 400, 500, 1000, steps=10)
        time.sleep(2)

        # 使用unittest原生的assert来判定测试结果
        # 详情可见python unittest模块
        self.assertTrue(self.device(text="搜索").exists)

        self.device(text="搜索").set_text("饿了么")
        self.device.press.back()
        time.sleep(2)
        self.assertTrue(self.device(text="秒开").exists)
        self.device(text="秒开").click()
        time.sleep(2)
        self.assertTrue(self.device(text="饿了么").exists)
