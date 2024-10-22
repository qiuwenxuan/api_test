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

    def update_case_data(self, story: str, key: str, value: any) -> None:
        for case in self.cases:
            if case["story"] == story:
                if key in case:
                    case[key] = value
                    self.yaml_loader.save_data(self.cases)  # 假设你有一个保存数据的方法
                    return
                else:
                    raise KeyError(f"'{key}' not found in the case data.")


