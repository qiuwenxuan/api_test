import os
from time import sleep
from typing import List
from ruamel.yaml import YAML


class YamlLoader(object):
    """通用的 YAML 加载类，负责加载 YAML 文件中的数据"""

    def __init__(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")

        self.file_path: str = file_path
        self.yaml: YAML = YAML()
        self.yaml.preserve_quotes = True  # 保持字符串的引号
        self.datas = self._load_yaml()

    # 加载yaml文件数据
    def _load_yaml(self) -> List[dict]:
        with open(self.file_path, mode="r", encoding="utf-8") as f:
            # 转换为原生的 Python dict 类型
            datas = self.yaml.load(f) or []
            if isinstance(datas, dict):
                datas = [dict(datas)]
            return datas

    def get_data(self, key=None):
        if key:
            for d in self.datas:
                for k, v in d.items():
                    if k == key:
                        return v
        else:
            return self.datas

    def save_data(self, data: List[dict]) -> None:
        with open(self.file_path, mode="w", encoding="utf-8") as f:
            self.yaml.dump(data, f)

    def edit_data(self, new_data: dict) -> List[dict]:
        if self.datas:
            for data in self.datas:
                for key, value in new_data.items():
                    data[key] = value
        else:
            self.datas.append(new_data)
        self.save_data(self.datas)
        return self.datas

    def clean_data(self) -> None:
        self.save_data([])


if __name__ == "__main__":
    cl1 = YamlLoader(
        r"C:\Users\v-williamqiu\Desktop\wx\workspace\api_test\extract.yaml"
    )

    value = cl1.edit_data(
        {
            "access_token": "UK25WRgSnpSz6VZIJjeD1VbHbFD_ElgiWtQkI8geKbOIIyWv__EBf0oSXRiACAKPJ"
        }
    )
    sleep(2)
    value = cl1.edit_data({"access_token": "RiACAKPJ"})
    sleep(2)
    cl1.clean_data()
    print(value)
