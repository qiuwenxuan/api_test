import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging.handlers import TimedRotatingFileHandler
from common.parse_conf import ParseConf
from conf.conf import CONF_PATH, LOG_PATH

parseConf = ParseConf(CONF_PATH)
_log_level = parseConf.get_value("log", "log_level")
_log_format = parseConf.get_value("log", "log_format")
_log_file = LOG_PATH


def log_init():
    logger = logging.getLogger("main")
    logger.setLevel(level=_log_level)

    formatter = logging.Formatter(_log_format)

    handler = TimedRotatingFileHandler(
        filename=_log_file, when="D", interval=1, backupCount=7, encoding="utf-8"
    )
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)


if __name__ == "__main__":
    log_init()
    logger1 = logging.getLogger("main")
    logger2 = logging.getLogger("main.js")
    logger3 = logging.getLogger("main.bd")
    logger1.info("logger1 info ...")
    logger2.error("logger2 error ...")
    logger1.warning("logger1 warning ...")
    logger2.debug("logger2 debug ...")
    logger3.info("logger3 info ...")
    logger3.info("logger3 info ...")
