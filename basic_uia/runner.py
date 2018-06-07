from basic_uia import device, logger, utils
import config as cf
import unittest
import io


def run_all():
    runner_output = io.StringIO()
    runner_instance = unittest.TextTestRunner(
        stream=open(cf.CUR_RESULT_FILE, 'w+')
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
    # todo: 暂时简陋版本
    report_template_content = open(cf.REPORT_TEMPLATE_FILE).read()
    with open(cf.CUR_REPORT_FILE, 'w+') as report_file:
        report_content = report_template_content.format(
            title_name=cf.CUR_TASK_NAME,
            total_case_count=result.testsRun,
            fail_case_count=len(result.failures)
        )
        report_file.write(report_content)

    runner_output.close()
    logger.info('test end')
