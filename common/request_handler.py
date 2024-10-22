import sys
import os

sys.path.append(os.getcwd())
from common.logger_manager import LoggerManager

import logging
import requests


class RequestHandler:
    """统一请求封装类"""

    def __init__(self, logger=None):
        self.logger = logger if logger else LoggerManager().get_logger()
        self.session = requests.session()

    def send_request(self, **kwargs):
        # 记录请求信息
        self.logger.info(
            f'Sending {kwargs["method"].upper()} request to {kwargs["url"]}'
        )
        try:
            response = self.session.request(**kwargs)
            # 记录响应信息
            self.logger.info(f"Response Code: {response.status_code}")
            return response
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise


if __name__ == "__main__":
    params = {
        "grant_type": "client_credential",
        "appid": "wx8a9de038e93f77ab",
        "secret": "8326fc915928dee3165720c910effb86",
    }
    res = RequestHandler().send_request(
        url="https://api.weixin.qq.com/cgi-bin/token", method="get", params=params
    )
    print(res.json())
