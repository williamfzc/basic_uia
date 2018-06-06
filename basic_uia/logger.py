import logging
import functools
import config as cf


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    stream=open(cf.CUR_LOG_FILE, 'w+'),
    level=logging.DEBUG,
    format=LOG_FORMAT
)
info = logging.info


def add_log(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        info(func.__name__ + 'start ...')
        result = func(*args, **kwargs)
        info(func.__name__ + 'stop.')
        return result
    return deco
