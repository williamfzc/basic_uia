import os
import datetime
import random

# --- PROJECT CONF ---
PROJECT_PATH = os.path.dirname(__file__)
CASE_DIR_PATH = os.path.join(PROJECT_PATH, 'cases')
RESULT_DIR_PATH = os.path.join(PROJECT_PATH, 'result')

# --- 每次测试都会改变 ---
CUR_TASK_NAME = datetime.datetime.now().strftime('%Y%m%d%H%M%S') \
                + str(random.randint(0, 9))
CUR_RESULT_DIR = os.path.join(RESULT_DIR_PATH, CUR_TASK_NAME)
CUR_RESULT_FILE = os.path.join(CUR_RESULT_DIR, CUR_TASK_NAME+'.txt')
# 系统日志
CUR_LOG_FILE = os.path.join(CUR_RESULT_DIR, CUR_TASK_NAME+'.log')

# --- 配置机器 ---
DEVICE_ID_LIST = [
    # '849a5c49',
    # '9b07c8f8',
    '192.168.0.152',
]

# --- 文件夹初始化 ---
if not os.path.exists(CUR_RESULT_DIR):
    os.makedirs(CUR_RESULT_DIR)
