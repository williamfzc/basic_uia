import config as cf
import os
from basic_uia import logger
from .uiautomator import Device

DEVICE_INSTANCE_DICT = dict()


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
        self._device_instance = Device(device_id)
        logger.info('{} connected'.format(self.device_id))

    def __getattr__(self, item):
        return getattr(self._device_instance, item)

    def __call__(self, *args, **kwargs):
        return self._device_instance.__call__(*args, **kwargs)


def connect_all_device():
    """ 关联所有配置的设备 """
    for each_id in cf.DEVICE_ID_LIST:
        DEVICE_INSTANCE_DICT[each_id] = DeviceItem(each_id)
    logger.info('all connected.')
