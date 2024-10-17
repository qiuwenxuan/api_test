from typing import Optional
from object.yaml_loader import YamlLoader
from object.request_util import RequestApi


class CaseUtil:
    def __init__(self, casedata_path: str):
        # 加载测试数据
        self._casedata_loader = YamlLoader(casedata_path)

    def get_request(self, story):
        return self._casedata_loader.get_story_data(story).request

    def run_testcase(
        self, story, update_fields: Optional[dict] = None, res_type="json"
    ):
        request_data = self.get_request_data(story)
        if update_fields:
            for key, value in update_fields.items():
                request_data[key] = value
        return RequestApi.send_request(res_type, **request_data)
