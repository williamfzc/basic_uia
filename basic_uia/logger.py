import logging
import functools

# alias of logging.info
info = None


def init_logger(logger_path):
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
    )

    file_handler = logging.FileHandler(logger_path)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(logging.INFO)
    logging.getLogger('').addHandler(file_handler)

    global info
    info = logging.info


def add_log(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        logging.info(func.__name__ + ' start ...')
        result = func(*args, **kwargs)
        logging.info(func.__name__ + ' stop.')
        return result
    return deco
