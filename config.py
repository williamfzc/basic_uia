import os
import datetime
import random

# --- PROJECT CONF ---
PROJECT_PATH = os.path.dirname(__file__)
CASE_DIR_PATH = os.path.join(PROJECT_PATH, 'cases')
RESULT_DIR_PATH = os.path.join(PROJECT_PATH, 'result')
LOG_DIR_PATH = os.path.join(PROJECT_PATH, 'log')

# --- 每次测试都会改变 ---
CUR_TASK_NAME = datetime.datetime.now().strftime('%Y%m%d%H%M%S') \
                + str(random.randint(0, 9))
CUR_RESULT_FILE = os.path.join(RESULT_DIR_PATH, CUR_TASK_NAME+'.log')
CUR_LOG_FILE = os.path.join(LOG_DIR_PATH, CUR_TASK_NAME+'.log')

# --- 配置机器 ---
DEVICE_ID_LIST = [
    # '849a5c49',
    # '9b07c8f8',
    '192.168.0.152',
]
