import os
import datetime
import random


# --- PROJECT CONF ---
PROJECT_PATH = os.path.dirname(__file__)
CASE_DIR_PATH = os.path.join(PROJECT_PATH, 'cases')
RESULT_DIR_PATH = os.path.join(PROJECT_PATH, 'result')
TEMPLATE_DIR_PATH = os.path.join(PROJECT_PATH, 'templates')

# 自定义的外部API
EXTEND_API_FILE_NAME = 'extend_api.py'
EXTEND_API_FILE = os.path.join(PROJECT_PATH, EXTEND_API_FILE_NAME)

# 用例配置文件
CASE_CONFIG_FILE_NAME = 'case_config.txt'
CASE_CONFIG_FILE = os.path.join(CASE_DIR_PATH, CASE_CONFIG_FILE_NAME)

# --- 配置 ---
# 用例before、after、start执行前后停等时间
RELAX_TIME = 1
# 执行用例时分割线的长度
LENGTH_OF_SPLIT_LINE = 60
# 默认，本次任务结果文件夹
CUR_TASK_NAME = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 9))
# 本次任务的结果文件夹
CUR_RESULT_DIR = None
# runner的输出（html）
CUR_RESULT_FILE = None
# 系统日志
CUR_LOG_FILE = None
# 错误截图文件夹
CUR_SCREEN_SHOT_DIR = None

# --- 配置机器 ---
# 通过参数传入也可
DEVICE_ID_LIST = ['R8AQCYIBKB496DOZ', ]


# --- 文件夹初始化 ---
# --- 每次测试都会改变 ---
def init_result_dir():
    global CUR_LOG_FILE, CUR_RESULT_DIR, CUR_RESULT_FILE, CUR_SCREEN_SHOT_DIR
    CUR_RESULT_DIR = os.path.join(RESULT_DIR_PATH, CUR_TASK_NAME)
    CUR_RESULT_FILE = os.path.join(CUR_RESULT_DIR, 'result.html')
    CUR_LOG_FILE = os.path.join(CUR_RESULT_DIR, 'framework.log')
    CUR_SCREEN_SHOT_DIR = os.path.join(CUR_RESULT_DIR, 'screen_shot')

    if not os.path.exists(CUR_SCREEN_SHOT_DIR):
        os.makedirs(CUR_SCREEN_SHOT_DIR)
