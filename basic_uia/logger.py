import logging
import functools
import time

import config as cf

# alias of logging's methods
info = None
error = None


def init_logger(logger_path):
    """ 初始化日志模块 """
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
    )

    file_handler = logging.FileHandler(logger_path)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(logging.INFO)
    logging.getLogger('').addHandler(file_handler)

    global info, error
    info = logging.info
    error = logging.error
    info(' SYSTEM READY '.center(cf.LENGTH_OF_SPLIT_LINE, '='))


def add_log(func):
    """ 函数执行流程的日志装饰器 """
    @functools.wraps(func)
    def deco(*args, **kwargs):
        func_desc = func.__doc__
        logging.info('*** Start Function [{}] ***'.format(func_desc))
        start_time = time.time()
        result = func(*args, **kwargs)
        logging.info('--- Done in {} seconds ---'.format(str(round(time.time() - start_time, 2))))
        return result
    return deco
