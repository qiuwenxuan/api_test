import logging
from typing import Optional
import pytest

from common.log import log_init
from common.yaml_util import YamlUtil as YU
from conf.conf import YAML_PATH

# 定义logger对象
logger: Optional[logging.Logger] = logging.getLogger("main.weixin")


@pytest.fixture(scope="session", autouse=True)
def ini_log():
    log_init()


@pytest.fixture(scope="class", autouse=True)
def clean_yaml():
    logger.info("正在清理yaml文件...")
    YU.clear_yaml(YAML_PATH)
