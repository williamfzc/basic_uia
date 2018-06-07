import os
import datetime
import random


# --- PROJECT CONF ---
PROJECT_PATH = os.path.dirname(__file__)
CASE_DIR_PATH = os.path.join(PROJECT_PATH, 'cases')
RESULT_DIR_PATH = os.path.join(PROJECT_PATH, 'result')
TEMPLATE_DIR_PATH = os.path.join(PROJECT_PATH, 'templates')

REPORT_TEMPLATE_FILE = os.path.join(TEMPLATE_DIR_PATH, 'report.html')

# --- 配置 ---
# 用例before、after、start执行前后停等时间
RELAX_TIME = 1
# 默认，本次任务结果文件夹
CUR_TASK_NAME = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 9))
# 本次任务的结果文件夹
CUR_RESULT_DIR = None
# unittest本身的测试输出
CUR_RESULT_FILE = None
# 系统日志
CUR_LOG_FILE = None
# 可阅读的测试报告
CUR_REPORT_FILE = None
# 错误截图文件夹
CUR_SCREEN_SHOT_DIR = None

# --- 配置机器 ---
# 通过参数传入也可
DEVICE_ID_LIST = ['849a5c49', ]


# --- 文件夹初始化 ---
# --- 每次测试都会改变 ---
def init_result_dir():
    global CUR_LOG_FILE, CUR_REPORT_FILE, CUR_RESULT_DIR, CUR_RESULT_FILE, CUR_SCREEN_SHOT_DIR
    CUR_RESULT_DIR = os.path.join(RESULT_DIR_PATH, CUR_TASK_NAME)
    CUR_RESULT_FILE = os.path.join(CUR_RESULT_DIR, 'unittest_output.txt')
    CUR_LOG_FILE = os.path.join(CUR_RESULT_DIR, 'framework.log')
    CUR_REPORT_FILE = os.path.join(CUR_RESULT_DIR, 'report.html')
    CUR_SCREEN_SHOT_DIR = os.path.join(CUR_RESULT_DIR, 'screen_shot')

    if not os.path.exists(CUR_SCREEN_SHOT_DIR):
        os.makedirs(CUR_SCREEN_SHOT_DIR)
