import os

import config as cf
from basic_uia import logger
# from .uiautomator import Device
import uiautomator2 as u2

TEST_DEVICE = None


def confirm_device_connection(device_id):
    """ 确保设备已经正常连接上 """
    for line in os.popen('adb devices'):
        if device_id in line and 'device' in line:
            return True
    else:
        raise ConnectionError('device {} not found.'.format(device_id))


class DeviceItem(object):
    """ 设备类 """
    def __init__(self, device_id):
        self.device_id = device_id
        confirm_device_connection(device_id)
        self._device_instance = u2.connect(device_id)
        logger.info(self._device_instance.device_info)
        logger.info('{} connected'.format(device_id))

    def __getattr__(self, item):
        return getattr(self._device_instance, item)

    def __call__(self, *args, **kwargs):
        return self._device_instance.__call__(*args, **kwargs)


def connect_device():
    """ 关联所有配置的设备 """
    device_id = cf.DEVICE_ID_LIST[0]
    global TEST_DEVICE
    TEST_DEVICE = DeviceItem(device_id)
    logger.info('Device [ {} ] connected.'.format(device_id))
