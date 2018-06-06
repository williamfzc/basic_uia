import logging
import config as cf


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    stream=open(cf.CUR_LOG_FILE, 'w+'),
    level=logging.DEBUG,
    format=LOG_FORMAT
)
info = logging.info
