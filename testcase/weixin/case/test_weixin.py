import os
import sys
from typing import Optional


sys.path.append(os.getcwd())
from object.casedata_loader import CaseDataLoader
from object.case_data import CaseData
from object.request_util import RequestApi
import re
import pytest
from common.yaml_util import YamlUtil as YU
from testcase.weixin.case.conftest import logger


# @pytest.fixture(scope="class")
# def api_request():
#     return RequestApi()


# @pytest.fixture(scope="class")
# def casedata_loader():
#     return CaseDataLoader(casedata_path)


class TestApi(object):
    _casedata_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data"
    )
    _casedata_path = os.path.join(_casedata_dir, "test_weixin_data.yaml")
    _casedate_loader = CaseDataLoader(_casedata_path)

    def get_requestDate(self, story):
        request_data = TestApi._casedate_loader.get_data(story).request
        return request_data

    def run_testcase(self, story, update_fields: Optional[dict] = {},res_type=None):
        request_data = self.get_requestDate(story)
        if update_fields:
            for key, value in update_fields.items():
                request_data[key] = value

        return RequestApi.send_request(res_type, **request_data)

    # 获取access_token鉴权码
    @pytest.mark.debug
    def test_get_token(self):
        res = self.run_testcase("get_token")
        assert len(res.json()["access_token"]) == 136 and res.status_code == 200
        YU.write_yaml({"access_token": res.json()["access_token"]})

    # 查询标签
    @pytest.mark.passed
    def test_select_flag(self):
        update_fields = {"params": {"access_token": YU.read_yaml(key="access_token")}}
        res = self.run_testcase("select_flag", update_fields)
        assert len(res.json()) != None and res.status_code == 200

    # 编辑标签
    @pytest.mark.passed
    def test_edit_flag(self):
        res = self.run_testcase("edit_flag")
        assert len(res.json()) != None and res.status_code == 200

    # 文件上传
    @pytest.mark.passed
    def test_file_upload(self):
        for key, value in self.get_requestDate("file_upload")["files"].items():
            update_fields = {
                "params": {"access_token": YU.read_yaml("access_token")},
                "files": {key: open(os.path.join(self._casedata_dir, value), "rb")},
            }
        res = self.run_testcase("file_upload", update_fields)
        assert res.status_code == 200 and res.json()["url"] != None

    # 访问phpwind首页
    @pytest.mark.passed
    def test_get_phpwind(self):
        res = self.run_testcase("get_phpwind")
        # 正则匹配csrf_token
        csrf_token = YU.write_yaml(
            {
                "csrf_token": re.search(
                    'name="csrf_token" value="(.*?)"', res.text
                ).group(1)
            }
        )
        assert len(csrf_token) == 16 and res.status_code == 200

    # 登录接口
    @pytest.mark.passed
    def test_login(self):
        update_fields = {"params": {"csrf_token": YU.read_yaml("csrf_token")}}
        res = self.run_testcase("login", update_fields, res_type="text")
        assert res.status_code == 200


if __name__ == "__main__":
    pytest.main()
