import base64
import hashlib
import random

import yaml

from common.base_url import is_test_url
from common.files_path import extract_path, files_path


class DebugTalk:

    def read_extract_arg(self, key):
        with open(extract_path, encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    """提取多个值用下标取值"""
    def read_extract_args(self, key, index):
        with open(extract_path, encoding='utf-8', mode="r") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key][int(index)]

    """生成随机数"""
    def get_random_number(self):
        data = random.randint(0, 99999)
        return data

    """md5加密"""
    def md5_encode(self, args):
        #把变量变成 utf_8的格式
        args = str(args).encode("utf-8")
        #md5加密
        md5_value = hashlib.md5(args).hexdigest()
        return md5_value

    """base64加密"""
    def base64_encode(self, args):
        #把变量变成 utf_8的格式
        args = str(args).encode("utf-8")
        #base64加密
        base64_value = base64.b64encode(args).decode(encoding="utf-8")
        return base64_value

    """文件地址"""
    def get_model_path(self, file_name):
        path = files_path + file_name
        new_path = path.replace("\\", "/")
        return new_path

    def get_id(self):
        if is_test_url:
            return '123'
        else:
            return '456'