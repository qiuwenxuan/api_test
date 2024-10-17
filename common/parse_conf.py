import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf.conf import CONF_PATH
import configparser


class ParseConf:
    """conf.ini文件操作类"""

    def __init__(self, conf_path=None):
        self.conf = configparser.ConfigParser()
        if conf_path and os.path.exists(conf_path):
            self.conf.read(conf_path)
        self.conf_path = conf_path

    def get_value(self, section, option):
        try:
            return self.conf.get(section, option)
        except configparser.NoSectionError:
            print(f"Section '{section}' 不存在")
        except configparser.NoOptionError:
            print(f"Option '{option}' 不存在")

    def set_value(self, section, option, value):
        if not self.conf.has_section(section):
            self.conf.add_section(section)
        self.conf.set(section, option, value)
        # 保存配置文件到本地
        with open(self.conf_path, "w") as conf_ini:
            self.conf.write(conf_ini)


if __name__ == "__main__":
    parseConf = ParseConf(CONF_PATH)
    env = parseConf.get_value("service", "test")
    print(env)
    parseConf.set_value("headers", "access-token", "aaauISDHSAHFUOIADJLJ")
