from basic_uia import device, logger, utils
from basic_uia.htmltestrunner import HTMLTestRunner
import config as cf
import unittest
import io


def run_all():
    runner_output = io.StringIO()
    runner_instance = HTMLTestRunner(
        stream=open(cf.CUR_RESULT_FILE, 'wb+')
    )

    case_dict = utils.CASE_MODULE_DICT
    device_dict = device.DEVICE_INSTANCE_DICT
    test_suite = unittest.TestSuite()
    case_list = list()
    for case_name, case_item in case_dict.items():
        for each_device_id, each_device in device_dict.items():
            logger.info(
                'start case [ {} ] on device: {}'.format(
                    case_name,
                    each_device_id,
                )
            )
            case_item_cls = case_item.TestCase(
                device=each_device,
                case_name=case_name,
                output_stream=runner_output,
            )
            case_list.append(case_item_cls)

    # start test!
    test_suite.addTests(case_list)
    result = runner_instance.run(test_suite)

    # result analysis
    logger.info('Total cases: ' + str(result.testsRun))
    logger.info('Fail cases: ' + str(len(result.failures)))

    runner_output.close()
    logger.info('test end')
