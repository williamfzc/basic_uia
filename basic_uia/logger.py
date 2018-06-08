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
    info('===== SYSTEM READY =====')


def add_log(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        logging.info('----- {} START -----'.format(func.__name__))
        try:
            result = func(*args, **kwargs)
        except BaseException as e:
            raise e
        finally:
            logging.info('----- {} STOP -----'.format(func.__name__))
        return result
    return deco
