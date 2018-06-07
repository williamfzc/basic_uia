import logging
import functools

# alias of logging.info
info = None


def init_logger(logger_path):
    logger = logging.getLogger()
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel('INFO')

    file_handler = logging.FileHandler(logger_path)
    file_handler.setFormatter(log_format)
    file_handler.setLevel('INFO')

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    global info
    info = logging.info


def add_log(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        logging.info(func.__name__ + 'start ...')
        result = func(*args, **kwargs)
        logging.info(func.__name__ + 'stop.')
        return result
    return deco
