import json
from typing import Optional
from urllib.parse import urljoin
import requests
from common.parse_conf import ParseConf
from conf.conf import CONF_PATH

url = None
headers = None
params = None

# 构造 Python 字典


class ApiKeys:
    def __init__(self, env="dev"):
        parseConf = ParseConf(CONF_PATH)
        self.env = parseConf.get_value("service", env)
        self.base_headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
        }

    def do_get(self, path=None, headers=None, params=None, **kwargs):
        url = urljoin(self.env, path)
        headers = self.base_headers.update(headers)

        return requests.get(url=url, headers=headers, params=params, **kwargs)

    def do_post(
        self,
        path=None,
        headers: Optional[dict] = None,
        params=None,
        jsonType=True,
        **kwargs
    ):
        url = urljoin(self.env, path)
        header = self.base_headers
        if headers:
            header.update(headers)

        if jsonType:
            return requests.post(url=url, headers=headers, json=params, **kwargs)
        else:
            return requests.post(url=url, headers=headers, data=params, **kwargs)
