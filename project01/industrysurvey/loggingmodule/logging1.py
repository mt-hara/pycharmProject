import logging.config
from loggingmodule.log_functions import test_func
fileopath = "C:\\workspace\\pycharmProject\\project01\\industrysurvey\\loggingmodule\\logging.conf"
logging.config.fileConfig(fileopath)

logger = logging.getLogger()
logger.info("info level log")
logger.debug("debug level log")

test_func()