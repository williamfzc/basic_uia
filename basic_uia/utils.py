import config as cf
import os
import importlib
import basic_uia.logger as logger

CASE_MODULE_DICT = dict()


def load_all_cases():
    """ 加载所有cases文件夹下的用例 """
    case_module_dict = dict()
    case_dir_path = cf.CASE_DIR_PATH
    pure_case_dir_name = os.path.basename(case_dir_path)
    for each_file in os.listdir(case_dir_path):
        if each_file.endswith('.py') and not each_file.startswith('_'):
            case_module_name = os.path.splitext(each_file)[0]
            case_module_dict[case_module_name] = importlib.import_module(
                '{}.{}'.format(pure_case_dir_name, case_module_name)
            )
    global CASE_MODULE_DICT
    CASE_MODULE_DICT = case_module_dict
