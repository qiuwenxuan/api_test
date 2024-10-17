import logging
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests


logger: Optional[logging.Logger] = logging.getLogger("main")


class RequestApi:
    session = requests.session()

    @classmethod
    def send_request(cls, res_type="json", **kwargs):
        # 记录请求信息
        logger.info(f"Request URL: {kwargs.get('method')}->{kwargs.get('url')}")
        logger.info(f"Request Body: {kwargs}")

        try:
            response = RequestApi.session.request(**kwargs)
            # 记录响应信息
            logger.info(f"Response Code: {response.status_code}")
            if res_type == "json":
                logger.info(f"Response Body: {response.json()}")
            elif res_type == "type":
                logger.info(f"Response Body: {response.text}")
            else:
                logger.exception(f"res_type param type error!")
                raise TypeError
            return response
        except Exception as e:
            logger.error(f"Request failed: {str(e)}")
            raise
