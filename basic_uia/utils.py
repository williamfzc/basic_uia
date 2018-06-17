import os
import importlib
import unittest
import io

from basic_uia import device, logger, utils
from basic_uia.htmltestrunner import HTMLTestRunner
import config as cf

CASE_MODULE_DICT = dict()


def load_all_cases():
    """
    加载所有cases文件夹下的用例
    如果有配置文件 则按照配置文件加载
    """
    case_module_dict = dict()
    case_dir_path = cf.CASE_DIR_PATH
    case_config_file_path = cf.CASE_CONFIG_FILE
    pure_case_dir_name = os.path.basename(case_dir_path)
    pure_case_config_name = cf.CASE_CONFIG_FILE_NAME

    # 有配置文件
    if pure_case_config_name in os.listdir(case_dir_path):
        with open(case_config_file_path) as config_file:
            line = config_file.readline().strip()
            if line and line.endswith('.py'):
                case_module_name = os.path.splitext(line)[0]
                try:
                    case_module_dict[case_module_name] = importlib.import_module(
                        '{}.{}'.format(pure_case_dir_name, case_module_name)
                    )
                except ImportError as e:
                    logger.error(e)
    # 没配置文件
    else:
        for each_file in os.listdir(case_dir_path):
            if each_file.endswith('.py') and not each_file.startswith('_'):
                case_module_name = os.path.splitext(each_file)[0]
                case_module_dict[case_module_name] = importlib.import_module(
                    '{}.{}'.format(pure_case_dir_name, case_module_name)
                )
    global CASE_MODULE_DICT
    CASE_MODULE_DICT = case_module_dict
    logger.info('Cases Count: ' + str(len(CASE_MODULE_DICT.keys())))


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
