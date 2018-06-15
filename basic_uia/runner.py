import unittest
import io

from basic_uia import device, logger, utils
from basic_uia.htmltestrunner import HTMLTestRunner
import config as cf


# TODO 需要有 运行部分用例 的功能
def run_all():
    """ 运行所有用例 """
    runner_output = io.StringIO()
    runner_instance = HTMLTestRunner(
        stream=open(cf.CUR_RESULT_FILE, 'wb+')
    )

    case_dict = utils.CASE_MODULE_DICT
    device_item = device.TEST_DEVICE
    test_suite = unittest.TestSuite()
    case_list = list()
    for case_name, case_item in case_dict.items():
        case_item_cls = case_item.TestCase(
            device=device_item,
            case_name=case_name,
            output_stream=runner_output,
            logout=logger,
        )
        case_list.append(case_item_cls)

    # start test!
    test_suite.addTests(case_list)
    result = runner_instance.run(test_suite)

    # result analysis
    total_case_num = result.testsRun
    fail_case_num = result.failure_count
    pass_case_num = result.success_count
    error_case_num = result.error_count

    logger.info('Total cases: {}'.format(total_case_num))
    logger.info('Pass cases: {}'.format(pass_case_num))
    logger.info('Fail cases: {}'.format(fail_case_num))
    logger.info('Error happened times: {}'.format(error_case_num))

    logger.info('To view details, please check {}.'.format(cf.CUR_RESULT_FILE))

    runner_output.close()
    device_item.service("uiautomator").stop()
    logger.info(' Test end '.center(cf.LENGTH_OF_SPLIT_LINE, '='))
