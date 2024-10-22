from datetime import datetime
import os
import sys

sys.path.append(os.getcwd())
import logging

from logging.handlers import TimedRotatingFileHandler

from conf.conf import ROOT_DIR


class LoggerManager:
    """通用的日志管理类，负责配置和获取日志记录器"""

    def __init__(
        self,
        log_name: str = "LoggerManager",
        log_level: int = logging.INFO,
        log_dir: str = "logs",
    ) -> None:
        """
        初始化 LoggerManager 类

        @param log_name: str 日志文件的名称
        @param log_level: int 日志级别 (默认 logging.INFO)
        @param log_dir: str 日志文件存储目录 (默认 'logs')
        """
        self.log_dir = os.path.join(ROOT_DIR, log_dir)
        self.log_name = log_name
        self.log_level = log_level
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """
        配置日志记录器
        @return: logging.Logger 配置完成的日志记录器
        """
        # 确保日志目录存在
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # 创建日志记录器
        logger = logging.getLogger(self.log_name)
        logger.setLevel(self.log_level)

        # 获取当前日期，并将日期添加到日志文件名中
        current_date = datetime.now().strftime("%Y-%m-%d")

        # 创建日志文件路径
        log_file = os.path.join(self.log_dir, f"{current_date}.log")

        # 创建处理器
        file_handler = TimedRotatingFileHandler(
            log_file, when="midnight", interval=1, backupCount=7, encoding="utf-8"
        )
        file_handler.suffix = "%Y-%m-%d"
        file_handler.setLevel(self.log_level)

        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)

        # 创建格式化器并添加到处理器
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器到日志记录器
        if not logger.hasHandlers():
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

    def get_logger(self) -> logging.Logger:
        """
        获取日志记录器的接口
        @return: logging.Logger 日志记录器
        """
        return self.logger


# 使用示例
if __name__ == "__main__":
    log_manager = LoggerManager(log_name="test_logger", log_level=logging.DEBUG)
    logger = log_manager.get_logger()

    logger.info("This is an info log message.")
    logger.debug("This is a debug log message.")
    logger.warning("This is an warning log message.")
    logger.error("This is an error log message.")
    logger.critical("This is an critical log message.")
