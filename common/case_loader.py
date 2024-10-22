import os
import sys

sys.path.append(os.getcwd())
from object.case_data import CaseData


from common.yaml_util import YamlLoader


class CaseLoader(object):
    """用于加载并解析测试用例"""

    def __init__(self, yaml_loader: YamlLoader):
        self.yaml_loader = yaml_loader
        self.cases = self.yaml_loader.get_data()

    def get_case(self, story: str) -> CaseData:
        for case in self.cases:
            if case["story"] == story:
                return CaseData(case)
        raise ValueError(f"No case found for '{story}'.")

    def get_request_data(self, story: str):
        case_data = self.get_case(story)
        return case_data.request

    def get_validation(self, story):
        case_data = self.get_case(story)
        return case_data.vilidate

    def update_request_data(self, story: str, data: dict) -> None:
        request_data = self.get_request_data(story)
        for key, value in data.items():
            for k, v in request_data.items():
                if key == k:
                    request_data[k] = value
        self.yaml_loader.save_data(self.cases)
        return self.get_request_data(story)


if __name__ == "__main__":
    cl = CaseLoader(
        YamlLoader(
            r"C:\Users\v-williamqiu\Desktop\wx\workspace\api_test\testcase\weixin\data\test_weixin_data.yaml"
        )
    )
    print(cl.get_case("get_token"))
    print(cl.get_request_data("get_token"))
    print(cl.get_validation("get_token"))
    print(cl.update_request_data("get_token", {"json": 100}))
