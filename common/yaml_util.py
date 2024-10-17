import sys
import os
from typing import Dict, Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import yaml

from conf.conf import YAML_PATH


class YamlUtil(object):

    # 读文件
    @classmethod
    def write_yaml(cls, data, file_path=YAML_PATH):
        with open(file_path, mode="a+", encoding="utf-8") as f:
            yaml.dump(data, stream=f, allow_unicode=True)
        # 获取data字典的key,data={"key":"value"}
        key = next(iter(data))
        return cls.read_yaml(key,file_path)

    # 写文件
    @classmethod
    def read_yaml(cls, key=None, file_path=YAML_PATH):
        with open(file_path, mode="r+", encoding="utf-8") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value if not key else value[key]

    # 清空文件
    @classmethod
    def clear_yaml(cls, file_path=YAML_PATH):
        with open(file_path, encoding="utf-8", mode="w") as f:
            f.truncate()


if __name__ == "__main__":
    content = YamlUtil.write_yaml({"name": "百里老师"}, YAML_PATH)
    print(type(content))
    print(content)
