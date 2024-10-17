from typing import Optional



class CaseData(object):
    def __init__(self, case_data: Optional[dict]):
        self.feature = case_data["feature"]
        self.story = case_data["story"]
        self.title = case_data["title"]
        self.vilidate = case_data["vilidate"]
        self.request = case_data["request"]

    # def get_requestdata(self):
    #     return RequestData(self.request)
