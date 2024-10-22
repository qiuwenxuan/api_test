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

    def __init__(self, logger=None):
        """初始化 ValidationHandler 并设置日志"""
        self.logger = logger if logger else LoggerManager().get_logger()
        self.errors = []  # 用于存储验证过程中发生的错误

    def validate_status_code(
        self, response: requests.Response, expected_code: int = 200
    ):
        """验证响应状态码"""
        try:
            actual_code = response.status_code
            assert (
                actual_code == expected_code
            ), f"状态码不匹配，实际: {actual_code}, 预期: {expected_code}"
            self.logger.debug(f"状态码验证成功: {expected_code}")
        except AssertionError as e:
            self.logger.error(f"状态码验证失败: {e}")
            self.errors.append(str(e))

    def validate_field_value(
        self, response: requests.Response, key: str, expected_value
    ):
        """验证响应中的字段值"""
        try:
            actual_value = response.json().get(key)
            assert (
                actual_value == expected_value
            ), f"'{key}' 期望值: {expected_value}，实际值: {actual_value}"
            self.logger.info(f"字段 '{key}' 值验证成功: {expected_value}")
        except AssertionError as e:
            self.logger.error(f"字段值验证失败: {e}")
            self.errors.append(str(e))

    def validate_field_length(
        self, response: requests.Response, key: str, expected_length: int
    ):
        """验证字段的长度"""
        try:
            actual_length = len(str(response.json().get(key)))
            assert (
                actual_length == expected_length
            ), f"'{key}' 长度不匹配，实际: {actual_length}, 预期: {expected_length}"
            self.logger.info(f"字段 '{key}' 长度验证成功: {expected_length}")
        except AssertionError as e:
            self.logger.error(f"字段长度验证失败: {e}")
            self.errors.append(str(e))

    def validate_not_empty(self, response: requests.Response, key: str):
        """验证字段不为空"""
        try:
            actual_value = response.json().get(key)
            assert actual_value, f"'{key}' 期望不为空，但实际为空"
            self.logger.info(f"字段 '{key}' 不为空验证成功")

        except AssertionError as e:
            self.logger.error(f"字段不为空验证失败: {e}")
            self.errors.append(str(e))

    def validate_empty(self, response: requests.Response, key: str):
        """验证字段为空"""
        try:
            actual_value = response.json().get(key)
            assert not actual_value, f"'{key}' 期望为空，但实际不为空"
            self.logger.info(f"字段 '{key}' 为空验证成功")
        except AssertionError as e:
            self.logger.error(f"字段为空验证失败: {e}")
            self.errors.append(str(e))

    def check_errors(self):
        """检查验证过程中是否有错误，并在测试结束时统一抛出"""
        if self.errors:
            raise AssertionError("以下验证失败:\n" + "\n".join(self.errors))
