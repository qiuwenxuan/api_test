from common.logger_manager import LoggerManager


class AssertHandler:
    """自定义断言处理类"""

    def __init__(self, logger=None):
        self.errors = []
        self.logger = logger if logger else LoggerManager().get_logger()

    def assert_equal(self, actual, expected, message=""):
        try:
            assert actual == expected, f"{message} | 预期: {expected}, 实际: {actual}"
            self.logger.info(f"断言成功: {message} | 预期: {expected}, 实际: {actual}")
        except AssertionError as e:
            self.logger.error(f"断言失败: {e}")
            self.errors.append(str(e))

    def assert_status_code(self, response, expected_code):
        self.assert_equal(response.status_code, expected_code, f"状态码不匹配")

    def assert_key_value(self, response, key, expected_value):
        actual_value = response.json().get(key)
        self.assert_equal(actual_value, expected_value, f"字段 '{key}' 值不匹配")

    def assert_key_exist_and_not_empty(self, response, key):
        try:
            res = response.json()
            keys = res.keys()
            assert key in keys, f"字段'{key}' 在响应体中不存在"
            assert res[key], f"字段'{key}' 在响应体中值为空"
            self.logger.info(f"字段 '{key}' 存在且非空")
        except AssertionError as e:
            self.logger.error(f"字段验证失败: {e}")
            self.errors.append(str(e))

    def assert_key_is_empty(self, response, key):
        try:
            res = response.json()
            assert not res[key], f"字段'{key}' 在响应体中值不为空"
        except AssertionError as e:
            self.logger.error(f"字段验证失败: {e}")
            self.errors.append(str(e))

    def check_errors(self):
        if self.errors:
            raise AssertionError("以下验证失败:\n" + "\n".join(self.errors))
