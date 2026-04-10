import base64
import datetime
from datetime import datetime, timedelta
import hashlib
import json
import random
import time
from io import StringIO
import string

import yaml

from common.files_path import extract_path, files_path, token_path
from gmssl import sm2

class DebugTalk:
    """"""

    def read_extract_arg(self, key):
        # 判断 key 是否以 "token" 或 "global_" 开头
        if key.startswith("token") or key.startswith("global_"):
            path = token_path
        else:
            path = extract_path

        with open(path, encoding='utf-8') as f:
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

    "获取当前日期和时间"
    # 获取当前时间y-m-d h:m:s
    def get_current_time_bai(self):
        # 获取当前时间的时间戳
        timestamp = time.time()
        # 将时间戳转换为本地时间
        local_time = time.localtime(timestamp)
        # 将本地时间转换为易读的字符串形式
        readable_time = time.asctime(local_time)
        # 格式化当前时间
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
        return formatted_time

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

    """获取当前时间"""
    def get_current_time(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d+%H:%M:%S")
        return formatted_time


    """获取当前时间  年-月-日"""
    def get_current_time1(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d")
        return formatted_time

    """获取当前时间"""
    def get_current_time2(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time

    """获取下一天"""
    def get_next_date(self):
        current_time = datetime.now()

        # 格式化为 "年-月-日"
        current_date = current_time.strftime("%Y-%m-%d")

        # 加 1 天
        next_day = current_time + timedelta(days=1)
        next_date = next_day.strftime("%Y-%m-%d")
        return next_date


    # yaml文件内容转换成json格式
    def yaml_to_json(self,yamlPath):
        with open(yamlPath, encoding="utf-8") as f:
            datas = yaml.load(f, Loader=yaml.FullLoader)  # 将文件的内容转换为字典形式
        jsonDatas = json.dumps(datas, indent=5)  # 将字典的内容转换为json格式的字符串
        return jsonDatas

    "登录密码sm2加密"
    def set_sm2(self):
        params = {
            "userId": "agnes",
            "password": "000000",   #Agnes1324!
            "captcha": "",
            "captchaId": ""
        }
        public_key = '04abb2e4ea5937b038a066d7eee4a2583abf8b195e30e822046d6125a464413667214ad59d4099b5baf31f5b478e69aff110d4486645afb92babfb2cecb7ffd4e6'

        if public_key:
            # 假设 params['password'] 是字符串格式
            password = params.get('password')
            if password:
                sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=None)
                encrypted_password = sm2_crypt.encrypt(password.encode())
                # 在加密后的密码前加上 '04'
                params['password'] = '04' + encrypted_password.hex()

        return params



if __name__=='__main__':
    a=DebugTalk().get_model_path('账户登记-开户材料.pdf')
    print(a)
