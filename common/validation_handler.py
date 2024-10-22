import os
import sys

sys.path.append(os.getcwd())
import requests
from common.logger_manager import LoggerManager
from common.request_handler import RequestHandler


import requests
from common.logger_manager import LoggerManager
from common.request_handler import RequestHandler


class ValidationHandler:
    """负责验证 HTTP 响应"""

    def __init__(self, logger_name: str = "ValidationHandler"):
        """初始化 ValidationHandler 并设置日志"""
        self.logger = LoggerManager(log_name=logger_name).get_logger()
        self.errors = []  # 用于存储验证过程中发生的错误

    def validate(
        self,
        response: requests.Response,
        key: str = None,
        expected_value=None,
        expected_code: int = 200,
        expected_length: int = None,
        check_empty: bool = False,
        check_not_empty: bool = False,
    ):
        """
        通用验证方法，可以验证状态码、字段长度、字段值、是否为空等。
        - response: 需要验证的 HTTP 响应
        - key: 需要验证的字段名
        - expected_value: 预期的字段值
        - expected_code: 预期的状态码
        - expected_length: 预期的字段长度
        - check_empty: 是否检查字段为空
        - check_not_empty: 是否检查字段不为空
        """
        try:
            # 验证状态码
            if expected_code is not None:
                actual_code = response.status_code
                assert (
                    actual_code == expected_code
                ), f"状态码不匹配，实际: {actual_code}, 预期: {expected_code}"
                self.logger.debug(f"状态码验证成功: {expected_code}")

            # 验证字段值
            if key and expected_value is not None:
                actual_value = response.json().get(key)
                assert (
                    actual_value == expected_value
                ), f"'{key}' 期望值: {expected_value}，实际值: {actual_value}"
                self.logger.info(f"字段 '{key}' 值验证成功: {expected_value}")

            # 验证字段长度
            if key and expected_length is not None:
                actual_length = len(str(response.json().get(key)))
                assert (
                    actual_length == expected_length
                ), f"'{key}' 长度不匹配，实际: {actual_length}, 预期: {expected_length}"
                self.logger.info(f"字段 '{key}' 长度验证成功: {expected_length}")

            # 验证字段不为空
            if check_not_empty and key:
                actual_value = response.json().get(key)
                assert actual_value, f"'{key}' 期望不为空，但实际为空"
                self.logger.info(f"字段 '{key}' 不为空验证成功")

            # 验证字段为空
            if check_empty and key:
                actual_value = response.json().get(key)
                assert not actual_value, f"'{key}' 期望为空，但实际不为空"
                self.logger.info(f"字段 '{key}' 为空验证成功")

        except AssertionError as e:
            self.logger.error(f"验证失败: {e}")
            self.errors.append(str(e))

    def check_errors(self):
        """检查验证过程中是否有错误，并在测试结束时统一抛出"""
        if self.errors:
            raise AssertionError("以下验证失败:\n" + "\n".join(self.errors))


if __name__ == "__main__":
    params = {
        "grant_type": "client_credential",
        "appid": "wx8a9de038e93f77ab",
        "secret": "8326fc915928dee3165720c910effb86",
    }
    res = RequestHandler().send_request(
        url="https://api.weixin.qq.com/cgi-bin/token", method="get", params=params
    )

    # 实例化 ValidationHandler 并调用实例方法
    validator = ValidationHandler("test").validate(
        response=res, key="access_token", expected_length=136
    )
