import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests


class RequestUtil:
    session = requests.session()

    # 统计请求封装
    def send_request(self, **kwargs):
        return RequestUtil.session.request(**kwargs)
