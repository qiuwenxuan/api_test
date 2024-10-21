import os
import sys
from typing import Optional


sys.path.append(os.getcwd())
from common.case_util import CaseUtil
from conf.conf import ROOT_DIR
from common.yaml_util import YamlUtil
from object.request_util import RequestApi
from testcase.weixin.case.conftest import extract_yaml
from testcase.weixin.case.conftest import case_util
import re
import pytest


class TestApi(object):

    # 获取access_token鉴权码
    @pytest.mark.debug
    def test_get_token(self):
        res = case_util.run_testcase("get_token")
        assert len(res.json()["access_token"]) == 136 and res.status_code == 200
        extract_yaml.edit_data({"access_token": res.json()["access_token"]})

    # # 查询标签
    # @pytest.mark.passed
    # def test_select_flag(self):
    #     update_fields = {"params": {"access_token": YU.get_data(key="access_token")}}
    #     res = self.run_testcase("select_flag", update_fields)
    #     assert len(res.json()) != None and res.status_code == 200

    # # 编辑标签
    # @pytest.mark.passed
    # def test_edit_flag(self):
    #     res = self.run_testcase("edit_flag")
    #     assert len(res.json()) != None and res.status_code == 200

    # # 文件上传
    # @pytest.mark.passed
    # def test_file_upload(self):
    #     for key, value in self.get_requestDate("file_upload")["files"].items():
    #         update_fields = {
    #             "params": {"access_token": YU.get_data("access_token")},
    #             "files": {key: open(os.path.join(self._casedata_dir, value), "rb")},
    #         }
    #     res = self.run_testcase("file_upload", update_fields)
    #     assert res.status_code == 200 and res.json()["url"] != None

    # # 访问phpwind首页
    # @pytest.mark.passed
    # def test_get_phpwind(self):
    #     res = self.run_testcase("get_phpwind", res_type="text")
    #     # 正则匹配csrf_token
    #     csrf_token = YU.edit_data(
    #         {
    #             "csrf_token": re.search(
    #                 'name="csrf_token" value="(.*?)"', res.text
    #             ).group(1)
    #         }
    #     )
    #     assert len(csrf_token) == 16 and res.status_code == 200

    # # 登录接口
    # @pytest.mark.passed
    # def test_login(self):
    #     update_fields = {"params": {"csrf_token": YU.get_data("csrf_token")}}
    #     res = self.run_testcase("login", update_fields)
    #     assert res.status_code == 200


if __name__ == "__main__":
    pytest.main()
