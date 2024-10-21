import logging
import os
import pytest

from common.case_util import CaseUtil
from common.log import log_init
from common.yaml_util import YamlUtil
from conf.conf import ROOT_DIR

# 定义logger对象
logger = logging.getLogger("main.weixin")
casedata_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data"
)
casedata_path = os.path.join(casedata_dir, "test_weixin_data.yaml")
extract_path = os.path.join(ROOT_DIR, "extract.yaml")

casedate_yaml = YamlUtil(casedata_path)
extract_yaml = YamlUtil(extract_path)

case_util = CaseUtil(casedate_yaml)


@pytest.fixture(scope="session", autouse=True)
def ini_log():
    log_init()


@pytest.fixture(scope="class", autouse=True)
def clean_yaml():
    logger.info("正在清理yaml文件...")
    extract_yaml.clean_data()
