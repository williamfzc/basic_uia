import os

import config as cf
from basic_uia import logger
import uiautomator2 as u2

TEST_DEVICE = None


def confirm_device_connection(device_id):
    """ 确保设备已经正常连接上 """
    for line in os.popen('adb devices'):
        if device_id in line and 'device' in line:
            return True
    else:
        raise ConnectionError('device {} not found.'.format(device_id))


def get_device(device_id):
    """ 获取设备对象 """
    confirm_device_connection(device_id)
    device_instance = u2.connect(device_id)
    logger.info(device_instance.device_info)
    logger.info('{} connected'.format(device_id))
    return device_instance


def connect_device():
    """ 关联所有配置的设备 """
    device_id = cf.DEVICE_ID_LIST[0]
    global TEST_DEVICE
    TEST_DEVICE = get_device(device_id)
    logger.info('Device [ {} ] connected.'.format(device_id))
