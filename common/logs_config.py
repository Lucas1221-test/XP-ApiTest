import logging
import os
import time
from common.files_path import logs_path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

MAX_LOG_FILES = 10  # 最多保存的日志文件数量

# 整理已有的日志文件数量
existing_logs = [file for file in os.listdir(logs_path) if file.startswith("20")]
existing_logs.sort()

while len(existing_logs) >= MAX_LOG_FILES:
    oldest_log = existing_logs[0]
    os.remove(os.path.join(logs_path, oldest_log))
    existing_logs.pop(0)

# 生成带有时间戳的日志文件名，并创建FileHandler对象
current_time = time.strftime('%Y-%m%d %H-%M-%S')
file_name = f"{current_time}.log"
file_handler = logging.FileHandler(filename=os.path.join(logs_path, file_name), encoding="UTF-8")
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)