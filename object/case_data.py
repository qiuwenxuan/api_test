from typing import Optional


class CaseData(object):
    """测试数据封装类，用于读取yaml文件内的数据"""

    def __init__(self, case_data: Optional[dict]):
        self.feature = case_data["feature"]
        self.story = case_data["story"]
        self.title = case_data["title"]
        self.vilidate = case_data["vilidate"]
        self.request = case_data["request"]

