import unittest
import time
import functools
import sys
import os

import basic_uia.logger as logger
import config as cf
from basic_uia.api import CustomAPI


def func_relax(func):
    """ 用于给函数前后加延时 """
    @functools.wraps(func)
    def deco(*args, **kwargs):
        time.sleep(cf.RELAX_TIME)
        result = func(*args, **kwargs)
        time.sleep(cf.RELAX_TIME)
        return result
    return deco


class BaseTestCase(unittest.TestCase):
    """ 测试用例基类 """
    def __init__(self, device, case_name, output_stream, logout, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.device = device
        self.case_name = case_name
        self.adb = self.device.server.adb.cmd
        self.log = logout
        self.api = CustomAPI(self.device, self.adb, self.log)

        # TODO: 测试过程中需要记录的东西可以写到这 暂时没想到可以干嘛 可能用来记录关键bug？
        # TODO: 测试记录？记录下失败前执行到什么位置
        self.output_stream = output_stream

    @func_relax
    def setUp(self):
        """ before() """
        super(BaseTestCase, self).setUp()
        self.log.info(
            ' CURRENT CASE: [ {} ] '.format(self.case_name)
                .center(cf.LENGTH_OF_SPLIT_LINE, '-'))
        self.before()

    @func_relax
    def tearDown(self):
        """ after() """

        # TODO: 出错时触发截图 使用htmltestrunner之后这个不能用了
        # if sys.exc_info()[1]:
        #     self.log.error('error happened: {}'.format(sys.exc_info()))
        #     pic_name = '{}_{}.png'.format(self.case_name, self._testMethodName)
        #     self.device.screenshot(os.path.join(cf.CUR_SCREEN_SHOT_DIR, pic_name))

        super(BaseTestCase, self).tearDown()
        self.after()

        # RESET
        self.device.press.home()
        self.api.clean_recent()

    @func_relax
    def runTest(self):
        """ start() """
        self.start()

    def before(self):
        pass

    def after(self):
        pass

    def start(self):
        pass
