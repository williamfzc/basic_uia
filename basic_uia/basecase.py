import unittest


class BaseTestCase(unittest.TestCase):
    def __init__(self, device, case_name, *args, **kwargs):
        self.device = device
        self.case_name = case_name
        super(BaseTestCase, self).__init__(*args, **kwargs)
