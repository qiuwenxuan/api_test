from common.case_loader import CaseLoader
from common.request_handler import RequestHandler


class CaseExecutor(object):
    """负责执行测试用例，调用请求处理类并验证响应"""

    def __init__(
        self,
        case_loader: CaseLoader,
        request_handler: RequestHandler,
    ):
        self.case_loader = case_loader
        self.request_handler = request_handler

    def execute_testcase(self, story: str):
        case_request = self.case_loader.get_request_data(story)
        response = self.request_handler.send_request(**case_request)
        return response
