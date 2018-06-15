import basic_uia.runner as runner
import basic_uia.device as device
import basic_uia.utils as utils
import basic_uia.logger as logger
import config as cf
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', help="YOUR DEVICE ID")
parser.add_argument('-t', '--task', help="YOUR TASK NAME")


if __name__ == '__main__':
    # 处理外部参数
    outside_args = parser.parse_args()
    if outside_args.device:
        device_list = outside_args.device.split(',')
        cf.DEVICE_ID_LIST = device_list
    if outside_args.task:
        cf.CUR_TASK_NAME = outside_args.task
    cf.init_result_dir()
    logger.init_logger(cf.CUR_LOG_FILE)

    # 主流程
    device.connect_device()
    utils.load_all_cases()
    runner.run_all()
