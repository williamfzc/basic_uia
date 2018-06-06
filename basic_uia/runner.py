from basic_uia import device, logger, utils
import config as cf
import unittest
import datetime
import os

runner_instance = unittest.TextTestRunner(
    stream=open(
        os.path.join(
            cf.RESULT_DIR_PATH,
            datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        ) + '.log',
        'w+',
    )
)


def run_all():
    case_dict = utils.CASE_MODULE_DICT
    device_dict = device.DEVICE_INSTANCE_DICT
    test_suite = unittest.TestSuite()
    case_list = list()
    for case_name, case_item in case_dict.items():
        for each_device_id, each_device in device_dict.items():
            logger.info(
                'start case {} on device: {}'.format(
                    case_name,
                    each_device_id,
                )
            )
            case_item_cls = case_item.TestCase(
                device=each_device,
                case_name=case_name
            )
            case_list.append(case_item_cls)

    # start test!
    test_suite.addTests(case_list)
    runner_instance.run(test_suite)
    logger.info('test end')
