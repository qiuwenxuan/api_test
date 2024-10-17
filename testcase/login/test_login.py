# import sys
# import os


# sys.path.append(os.getcwd())
# from common.parse_conf import ParseConf
# import unittest
# from conf.conf import CONF_PATH, TEST_LOGIN_DATE

# from ddt import ddt, file_data
# from api_keys.keys import ApiKeys


# @ddt
# class TestLogin(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.api = ApiKeys()
#         # cls.access_token = None

#     @file_data(TEST_LOGIN_DATE)
#     def test_login_001(self, **kwargs):
#         res = self.api.do_post(path=kwargs["path"], params=kwargs["data"])
#         # 模拟生成token
#         # res["access-token"] = "asdafsafafaf"
#         # self.access_token = res["access-token"]
#         ParseConf(CONF_PATH).set_value("headers", "access-token", res["access-token"])

#     @file_data(TEST_LOGIN_DATE)
#     def test_login_002(self, **kwargs):
#         # kwargs["headers"] = {"access-token": self.access_token}
#         kwargs["headers"] = {
#             "access-token": ParseConf(CONF_PATH).get_value("headers", "access-token")
#         }

#         res = self.api.do_post(path=kwargs["path"], params=kwargs["data"])


# if __name__ == "__main__":
#     unittest.main()
