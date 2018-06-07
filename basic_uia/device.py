import config as cf
from basic_uia import logger
from uiautomator import Device

DEVICE_INSTANCE_DICT = dict()


class DeviceItem(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self._device_instance = Device(device_id)
        logger.info('{} connected'.format(self.device_id))

    def __getattr__(self, item):
        return getattr(self._device_instance, item)

    def __call__(self, *args, **kwargs):
        return self._device_instance.__call__(*args, **kwargs)


def connect_all_device():
    for each_id in cf.DEVICE_ID_LIST:
        DEVICE_INSTANCE_DICT[each_id] = DeviceItem(each_id)
    logger.info('all connected.')
