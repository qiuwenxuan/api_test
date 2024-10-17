import sys
import os
from ruamel.yaml import YAML

sys.path.append(os.getcwd())
from object.case_data import CaseData


class CaseDataLoader(object):
    def __init__(self, file):
        if not os.path.exists(file):
            raise FileNotFoundError(f"File {file} does not exist.")

        self.file = file
        self.yaml = YAML()
        self.yaml.preserve_quotes = True  # 保持字符串的引号
        with open(file, mode="r", encoding="utf-8") as f:
            self._values = self.yaml.load(f)

    def get_data(self, story=None):
        if story:
            for value in self._values:
                if value["story"] == story:
                    self.value = value
                    return CaseData(value)
        else:
            return dict(self._values)

    def edit_data(self, story: str, data: dict):
        story_data = self.get_data(story)
        if not story_data:
            raise ValueError(f"No data found for story '{story}'")

        # 修改或添加数据
        for key, value in data.items():
            self.value["request"][key] = value

        # 将更新后的数据写回到 YAML 文件，同时保留格式
        with open(self.file, mode="w", encoding="utf-8") as f:
            self.yaml.dump(self._values, f)


if __name__ == "__main__":
    cl = CaseDataLoader(
        r"C:\Users\v-williamqiu\Desktop\wx\workspace\api_test\testcase\weixin\data\test_weixin_data.yaml"
    )
    value = cl.get_data("get_token")
    print(value)
    cl.edit_data("edit_flag", {"auto": "sb"})
