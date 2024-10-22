import os

import pytest

from common.case_loader import CaseLoader
from common.logger_manager import LoggerManager
from common.request_handler import RequestHandler
from common.testcase_executor import CaseExecutor
from common.validation_handler import ValidationHandler
from common.yaml_util import YamlLoader
from conf.conf import ROOT_DIR

case_name = "TestWeixin"
logger = LoggerManager(case_name).get_logger()

extract_yaml = YamlLoader(os.path.join(ROOT_DIR, "extract.yaml"))
casedata_yaml = YamlLoader(
    os.path.join(ROOT_DIR, "testcase", "weixin", "data", "test_weixin_data.yaml")
)

case_loader = CaseLoader(casedata_yaml)
request_handler = RequestHandler(case_name)
validation_handler = ValidationHandler(case_name)
case_executor = CaseExecutor(case_loader, request_handler)


@pytest.fixture(scope="class", autouse=True)
def env_ini():
    extract_yaml.clean_data()

