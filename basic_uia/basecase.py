import unittest
import time
import functools
import sys
import os
import basic_uia.logger as logger
import config as cf


def func_relax(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        time.sleep(cf.RELAX_TIME)
        result = func(*args, **kwargs)
        time.sleep(cf.RELAX_TIME)
        return result
    return deco


class BaseTestCase(unittest.TestCase):
    def __init__(self, device, case_name, output_stream, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.device = device
        self.case_name = case_name

        # TODO: 测试过程中需要记录的东西可以写到这 暂时没想到可以干嘛 可能用来记录关键bug？
        self.output_stream = output_stream

    @func_relax
    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.before()

    @func_relax
    def tearDown(self):
        # TODO: 有待验证
        # 出错时触发截图
        if sys.exc_info()[0]:
            pic_name = '{}.png'.format(self._testMethodName)
            self.device.screenshot(os.path.join(cf.CUR_SCREEN_SHOT_DIR, pic_name))

        super(BaseTestCase, self).tearDown()
        self.after()

    @func_relax
    def runTest(self):
        self.start()

    @logger.add_log
    def before(self):
        pass

    @logger.add_log
    def after(self):
        pass

    @logger.add_log
    def start(self):
        pass
