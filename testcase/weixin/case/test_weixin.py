import os
import sys


sys.path.append(os.getcwd())
from object.casedata_loader import CaseDataLoader
from object.case_data import CaseData
from object.request_util import RequestUtil
import re
import pytest
from common.yaml_util import YamlUtil as YU
from testcase.weixin.case.conftest import logger

current_path = os.path.abspath(__file__)
casedata_dir = os.path.join(os.path.dirname(os.path.dirname(current_path)), "data")
casedata_path = os.path.join(casedata_dir, "test_weixin_data.yaml")


class TestApi(object):

    request = RequestUtil()
    casedata_loader = CaseDataLoader(casedata_path)

    # 获取access_token鉴权码
    @pytest.mark.passed
    @pytest.mark.parametrize("case_data", [casedata_loader.get_data("get_token")])
    def test_get_token(self, case_data: CaseData):
        requestDate = case_data.request
        res = self.request.send_request(**requestDate)
        YU.write_yaml({"access_token": res.json()["access_token"]})

        logger.info(res.json())
        assert len(res.json()["access_token"]) == 136 and res.status_code == 200

    # 查询标签
    @pytest.mark.passed
    @pytest.mark.parametrize("case_data", [casedata_loader.get_data("select_flag")])
    def test_select_flag(self, case_data: CaseData):
        requestData = case_data.request
        requestData["params"] = {"access_token": YU.read_yaml(key="access_token")}
        res = self.request.send_request(**requestData)

        logger.info(f"res:{res.json()}")
        assert len(res.json()) != None and res.status_code == 200

    # 编辑标签
    @pytest.mark.passed
    @pytest.mark.parametrize(
        "case_data",
        [casedata_loader.get_data("edit_flag")],  # 通过story读取对应的测试用例数据
    )
    def test_edit_flag(self, case_data: CaseData):
        requestDate = case_data.request
        res = self.request.send_request(**requestDate)

        logger.info(f"res:{res.json()}")
        assert len(res.json()) != None and res.status_code == 200

    # 编辑标签
    @pytest.mark.passed
    @pytest.mark.parametrize(
        "case_data",
        [casedata_loader.get_data("file_upload")],  # 通过story读取对应的测试用例数据
    )
    def test_file_upload(self, case_data: CaseData):
        requestDate = case_data.request
        for key, value in requestDate["files"].items():
            requestDate["files"][key] = open(
                os.path.join(casedata_dir, value), "rb"
            )  # 以rb二进制格式读取上传文件
        requestDate["params"] = {"access_token": YU.read_yaml("access_token")}
        res = self.request.send_request(**requestDate)

        logger.info(f"res:{res.json()}")
        assert res.status_code == 200 and res.json()["url"] != None

    @pytest.mark.passed
    @pytest.mark.parametrize("case_data", [casedata_loader.get_data("get_phpwind")])
    # 访问phpwind首页
    def test_get_phpwind(self, case_data: CaseData):
        requestDate = case_data.request
        res = self.request.send_request(**requestDate)
        # 正则匹配csrf_token
        csrf_token = YU.write_yaml(
            {
                "csrf_token": re.search(
                    'name="csrf_token" value="(.*?)"', res.text
                ).group(1)
            }
        )

        logger.debug(f"res:{res.text}")
        assert len(csrf_token) == 16 and res.status_code == 200

    # 登录接口
    @pytest.mark.passed
    @pytest.mark.parametrize(
        "case_data",
        [casedata_loader.get_data("login")],  # 通过story读取对应的测试用例数据
    )
    def test_login(self, case_data: CaseData):
        requestDate = case_data.request
        requestDate["data"] = {"csrf_token": YU.read_yaml("csrf_token")}
        res = self.request.send_request(**requestDate)

        logger.info(res.json())
        assert res.status_code == 200


if __name__ == "__main__":
    pytest.main()
