import config as cf
import os
import importlib
import basic_uia.logger as logger

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
