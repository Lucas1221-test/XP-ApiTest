import base64
import datetime
import hashlib
import random
import time

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

    "生成随机任务主题名称"
    def get_random_task_theme(self):
        data =  "自动化任务主题"+str(random.randint(100000,999999))
        return data

    "生成随机任务名称"
    def get_random_task_name(self):
        data = "自动化测试任务"+str(random.randint(100000,999999))
        return data

    "生成随机临时任务名称"
    def get_random_temp_task_name(self):
        data = "自动化临时任务"+str(random.randint(100000,999999))
        return data

    "生成当日日期"
    def get_today(self,t):
        data = str(datetime.date.today())+t
        return data

    "拼接交接明细数据"
    def get_handover_detail(self,prdtcodelist, prdtuserid, prdtusername, groupidlist, groupuserlist, groupusernamelist,
                            roleidlist, roleuserid, roleusername, tempidlist, tempuserid, tempusername):
        detaillist = []
        if len(prdtcodelist) != 0:
            for i in prdtcodelist:
                detaillist.append(
                    {
                        "type": "prdt",
                        "bizId": i,
                        "toUser": prdtuserid,
                        "isAutoTrans": "1",
                        "planType": "1"
                    })
        if len(groupidlist) != 0:
            for i in range(len(groupidlist)):
                detaillist.append(
                    {
                        "type": "common",
                        "bizId": groupidlist[i],
                        "toUser": groupuserlist[i][0]['userId'],
                        "isAutoTrans": "1",
                        "planType": "1"
                    })
        if len(roleidlist) != 0:
            for i in roleidlist:
                detaillist.append(
                    {
                        "type": "role",
                        "bizId": i,
                        "toUser": roleuserid,
                        "isAutoTrans": "1",
                        "planType": "1"
                    })
        if len(tempidlist) != 0:
            for i in tempidlist:
                detaillist.append(
                    {
                        "type": "temp",
                        "bizId": i,
                        "toUser": tempuserid,
                        "isAutoTrans": "1",
                        "planType": "1"
                    })

        name = []
        if prdtusername != '' and prdtusername not in name:
            name.append(prdtusername)

        if len(groupusernamelist) != 0:
            for i in groupusernamelist:
                if i not in name:
                    name.append(i)

        if tempusername != '' and tempusername not in name:
            name.append(tempusername)

        if roleusername != '' and roleusername not in name:
            name.append(roleusername)

        handoveruser = ','.join(name)

        type = []
        if len(detaillist) != 0:
            for i in detaillist:
                if i['type'] == 'prdt' and '产品任务' not in type:
                    type.append("产品任务")
                if i['type'] == 'common' and '岗位任务' not in type:
                    type.append("岗位任务")
                if i['type'] == 'role' and '角色' not in type:
                    type.append("角色")
                if i['type'] == 'temp' and '临时任务' not in type:
                    type.append("临时任务")

        handovertype = ','.join(type)

        detail = {}
        detail['detaillist'] = detaillist
        detail['handoveruser'] = handoveruser
        detail['handovertype'] = handovertype
        return detail

    "获取当前日期和时间"
    # 获取当前时间y-m-d h:m:s
    def get_current_time(self):
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

    def get_id(self):
        if is_test_url:
            return '123'
        else:
            return '456'