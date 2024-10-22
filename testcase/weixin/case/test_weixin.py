import os
import sys


sys.path.append(os.getcwd())
from testcase.weixin.case.conftest import extract_yaml
from testcase.weixin.case.conftest import case_executor
from testcase.weixin.case.conftest import validation_handler
from testcase.weixin.case.conftest import case_loader
from testcase.weixin.case.conftest import logger
import pytest


class TestWeixin(object):

    # 获取access_token鉴权码
    @pytest.mark.debug
    @pytest.mark.parametrize("story", ["get_token"])
    def test_get_token(self, story):
        res = case_executor.execute_testcase(story)
        logger.info(res.json())
        validation_handler.validate_field_length(
            response=res, key="access_token", expected_length=136
        )
        extract_yaml.edit_data({"access_token": res.json()["access_token"]})

    # 查询标签
    @pytest.mark.debug
    @pytest.mark.parametrize("story", ["select_flag"])
    def test_select_flag(self, story):
        update_fields = {
            "params": {"access_token": extract_yaml.get_data(key="access_token")}
        }
        case_loader.update_request_data(story, update_fields)
        res = case_executor.execute_testcase(story)
        logger.info(res.json())
        validation_handler.validate_not_empty(response=res, key="tags")

    # 编辑标签
    @pytest.mark.debug
    @pytest.mark.parametrize("story", ["edit_flag"])
    def test_edit_flag(self, story):
        update_fields = {
            "params": {"access_token": extract_yaml.get_data(key="access_token")}
        }
        case_loader.update_request_data(story, update_fields)
        res = case_executor.execute_testcase(story)
        logger.info(res.json())
        assert len(res.json()) != None and res.status_code == 200

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
