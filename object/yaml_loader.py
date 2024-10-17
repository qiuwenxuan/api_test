import sys
import os
from time import sleep
from ruamel.yaml import YAML


class YamlLoader(object):
    """加载操作yaml测试数据文件类"""

    def __init__(self, file: str) -> None:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File {file} does not exist.")

        self.file: str = file
        self.yaml: YAML = YAML()
        self.yaml.preserve_quotes = True  # 保持字符串的引号
        with open(file, mode="r", encoding="utf-8") as f:
            self._values: list[dict] = self.yaml.load(f) or []  # 确保至少是一个空列表

    def get_story_data(self, story: str) -> dict:
        if story:
            for value in self._values:
                if value["story"] == story:
                    return value
        raise ValueError(f"No story found for '{story}' in {self.file}")

    def get_request_data(self, story: str) -> dict:
        return self.get_story_data(story)["request"]

    def edit_request_data(self, story: str, data: dict) -> dict:
        request_data = self.get_request_data(story)

        # 修改或添加数据
        for key, value in data.items():
            request_data[key] = value

        # 将更新后的数据写回到 YAML 文件，同时保留格式
        with open(self.file, mode="w", encoding="utf-8") as f:
            self.yaml.dump(self._values, f)

        return self.get_story_data(story)

    def edit_data(self, data: dict) -> dict:
        if not data:
            raise ValueError("Data dictionary is empty.")

        with open(self.file, mode="a+", encoding="utf-8") as f:
            self.yaml.dump(data, stream=f)

        # 获取data字典的key,data={"key":"value"}
        key = next(iter(data))
        return self.get_data(key)

    # 写文件
    def get_data(self, key: str = None) -> dict:
        return (
            self._values
            if not key
            else next(
                (value for value in self._values if value.get("story") == key), {}
            )
        )

    # 清空文件
    def clean_data(self) -> None:
        with open(self.file, encoding="utf-8", mode="w") as f:
            f.write("")


if __name__ == "__main__":
    cl1 = YamlLoader(
        r"C:\Users\v-williamqiu\Desktop\wx\workspace\api_test\testcase\weixin\data\test_weixin_data.yaml"
    )
    value1 = cl1.get_story_data("get_token")
    value2 = cl1.get_request_data("edit_flag")
    value3 = cl1.edit_request_data("edit_flag", {"auth": "sb"})
    sleep(1)
    value3 = cl1.edit_request_data("edit_flag", {"auth": ""})
    print(value1)
    print(value2)
    print(value3)

    cl2 = YamlLoader(
        r"C:\Users\v-williamqiu\Desktop\wx\workspace\api_test\extract.yaml"
    )
    value4 = cl2.edit_data(
        {
            "access_token": "85_QjE-u3a1eOhTpp2a86O36iLBPGFOElMHQhg3w4C6PxY2CFCVjCkGonEACxFot_xYslYUUK25WRgSnpSz6VZIJjeD1VbHbFD_ElgiWtQkI8geKbOIIyWv__EBf0oSXRiACAKPJ"
        }
    )
    value5 = cl2.get_data("access_token")
    sleep(1)
    cl2.clean_data()
