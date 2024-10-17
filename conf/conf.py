import os

# 当前工作目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# conf.ini配置文件路径
CONF_PATH = os.path.join(ROOT_DIR, "conf", "conf.ini")

TEST_LOGIN_DATE = os.path.join(ROOT_DIR, "test_data", "test_login_data.yaml")

LOG_PATH = os.path.join(ROOT_DIR, "log", "log.txt")

YAML_PATH = os.path.join(ROOT_DIR, "extract.yaml")

if __name__ == "__main__":
    print(ROOT_DIR)
    print(CONF_PATH)
