import os

# 当前工作目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# conf.ini配置文件路径
CONF_PATH = os.path.join(ROOT_DIR, "conf", "conf.ini")


TEST_WEIXIN_DATA = os.path.join(
    ROOT_DIR, "testcase", "weixin", "data", "test_weixin_data.yaml"
)
EXTRACT_PATH = os.path.join(ROOT_DIR, "extract.yaml")

if __name__ == "__main__":
    print(ROOT_DIR)
    print(CONF_PATH)
