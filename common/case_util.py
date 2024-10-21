import os
import sys


sys.path.append(os.getcwd())
from typing import Optional
from common.yaml_util import YamlUtil
from object.request_util import RequestApi


class CaseUtil:
    def __init__(self, casedata_yaml: YamlUtil):
        # 加载测试数据
        self._casedata_loader = casedata_yaml

    def run_testcase(
        self, story, update_fields: Optional[dict] = None, res_type="json"
    ):
        request_data = self._casedata_loader.get_request_data(story)
        if update_fields:
            for key, value in update_fields.items():
                request_data[key] = value
        return RequestApi.send_request(res_type, **request_data)


if __name__ == "__main__":

    case_util = CaseUtil(
        casedata_yaml=YamlUtil(
            r"C:\Users\v-williamqiu\Desktop\wx\workspace\api_test\testcase\weixin\data\test_weixin_data.yaml"
        )
    )
    res = case_util.run_testcase("get_token")
    print(res.json())
