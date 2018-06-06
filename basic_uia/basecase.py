# TODO 看一下这里能不能重定向结果
import unittest
import basic_uia.logger as logger


class BaseTestCase(unittest.TestCase):
    def __init__(self, device, case_name, *args, **kwargs):
        self.device = device
        self.case_name = case_name
        super(BaseTestCase, self).__init__(*args, **kwargs)

    @logger.add_log
    def setUp(self):
        super(BaseTestCase, self).setUp()

    @logger.add_log
    def tearDown(self):
        super(BaseTestCase, self).tearDown()

    @logger.add_log
    def runTest(self):
        pass
