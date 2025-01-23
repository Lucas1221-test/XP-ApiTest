import base64
import datetime
from datetime import datetime
import hashlib
import json
import random
import time
from io import StringIO
import string

import yaml

from common.base_url import is_test_url
from common.files_path import extract_path, files_path, token_path


class DebugTalk:
    """"""
    def read_extract_arg(self, key):
        if key != "token":
            with open(extract_path, encoding='utf-8') as f:
                value = yaml.load(stream=f, Loader=yaml.FullLoader)
                return value[key]
        else:
            with open(token_path, encoding='utf-8') as f:
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
        data = "自动化场景测试任务"+str(random.randint(100000,999999))
        return data

    "拼接单节点任务的casebody"
    def set_casebody(self,taskname,stepcode):
        casebody={"actions":[],"optionalStages":[],"stages":[{"defId":"","defName":"default","defType":"stage","optional":True,"edit":False,"defBody":{},"children":[{"stepName":taskname,"defType":"step","stepActType":"","stepId":"","edit":False,"stepFormInfo":{"caseStepDef":{"stepCode":stepcode,"stageName":"","stepName":taskname,"stepLevel":0,"encodingRule":"00008085","stepTag":[],"zrUserPzMethod":"0","zrUser":"","xzUserPzMethod":"0","xzUser":"","stepActOwner":"","stepCollaborateOwner":"","jrdb":"1","yxyq":"0","yxzb":"0","yxzf":"0","yxcxzx":"1","yxsggy":"1","dbzxazjdzs":"0","jdcxzx":"0","jdwxcxzx":"0","notifyRuleFlag":"0","startTimeFlag":"0","endTimeFlag":"0","notifyRule":"0","parmSetFlag":"0","stepRemark":"","baseDateType":"0","startTime":"00:00","startBaseDay":"","startDayType":"00","startCrossDayType":"0","startDay":"","endTime":"23:59","endBaseDay":"","endDayType":"00","endCrossDayType":"0","endDay":"0","isTodo":"0","isNotCrtJob":"0","allowManualConfirm":"1","isAllowExecAgain":"0","allowActionConfirm":"0","allowShowDetail":"0","allowFormAction":"0","allowEditEndTime":"0","paramsOutData":[],"warningMintues":"","stepExecMode":"FREQUENCY"},"failRuleTableData":{"judgeScript":""},"successRuleTableData":{"judgeScript":""},"activeRuleTableData":{"judgeScript":""},"timeoutRuleTableData":{"judgeScript":""},"exceptionRemind":[],"finishRemind":[],"timeoutRemind":[],"serviceResponseId":"","isRecordTimeoutError":"0","warningRemind":[]}}]}],"version":"0","stepCodeArr":{stepcode:stepcode}}
        return casebody

    "拼接快速新增单节点任务的casebody"
    def set_casebody_quick(self, stepcode):
        casebody = {"actions": [], "optionalStages": [], "stages": [
            {"defId": "", "defName": "default", "defType": "stage", "optional": True, "edit": False, "defBody": {},
             "children": [{"stepName": "default", "defType": "step", "stepActType": "", "stepId": "", "edit": False,
                           "stepFormInfo": {
                               "caseStepDef": {"stepCode": stepcode, "stageName": "", "stepName": "default",
                                               "stepLevel": 0, "encodingRule": "00008085", "stepTag": [],
                                               "zrUserPzMethod": "0", "zrUser": "", "xzUserPzMethod": "0", "xzUser": "",
                                               "stepActOwner": "", "stepCollaborateOwner": "", "jrdb": "1", "yxyq": "0",
                                               "yxzb": "0", "yxzf": "0", "yxcxzx": "1", "yxsggy": "1",
                                               "dbzxazjdzs": "0", "jdcxzx": "0", "jdwxcxzx": "0", "notifyRuleFlag": "0",
                                               "startTimeFlag": "0", "endTimeFlag": "0", "notifyRule": "0",
                                               "parmSetFlag": "0", "stepRemark": "", "baseDateType": "0",
                                               "startTime": "00:00", "startBaseDay": "", "startDayType": "00",
                                               "startCrossDayType": "0", "startDay": "", "endTime": "23:59",
                                               "endBaseDay": "", "endDayType": "00", "endCrossDayType": "0",
                                               "endDay": "0", "isTodo": "0", "isNotCrtJob": "0",
                                               "allowManualConfirm": "1", "isAllowExecAgain": "0",
                                               "allowActionConfirm": "0", "allowShowDetail": "0",
                                               "allowFormAction": "0", "allowEditEndTime": "0", "paramsOutData": [],
                                               "warningMintues": "", "stepExecMode": "FREQUENCY"},
                               "failRuleTableData": {"judgeScript": ""}, "successRuleTableData": {"judgeScript": ""},
                               "activeRuleTableData": {"judgeScript": ""}, "timeoutRuleTableData": {"judgeScript": ""},
                               "exceptionRemind": [], "finishRemind": [], "timeoutRemind": [], "serviceResponseId": "",
                               "isRecordTimeoutError": "0", "warningRemind": []}}]}], "version": "0",
                    "stepCodeArr": {stepcode: stepcode}}
        return casebody

    "拼接任务实例"
    def set_xcpmodel(self):
        list=[
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "1",
                "orderNum": 0,
                "tableField": "PK_ID",
                "field": "pkId",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "pkId",
                "isBizKey": "1",
                "isPk": "1",
                "ext": "{\"multiple\":\"0\"}",
                "fillRule": "ATOMIC_ID"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "CASE_ID",
                "field": "caseId",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "caseId"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "EXEC_DATE",
                "field": "execDate",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "执行日期"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "START_DATE",
                "field": "startDate",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "业务开始日期"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "END_DATE",
                "field": "endDate",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "业务结束日期"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "PLAN_START_TS",
                "field": "planStartTs",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "计划开始日期"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "PLAN_END_TS",
                "field": "planEndTs",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "计划结束日期"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "PRDT_CODE",
                "field": "prdtCode",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "产品代码"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "PRDT_NAME",
                "field": "prdtName",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "产品名称"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "FIELD1",
                "field": "field1",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "备用1"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "FIELD2",
                "field": "field2",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "备用2"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "FIELD3",
                "field": "field3",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "备用3"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "FIELD4",
                "field": "field4",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "备用4"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "FIELD5",
                "field": "field5",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "备用5"
            },
            {
                "fieldLength": 32,
                "fieldType": "text",
                "isRequire": "0",
                "orderNum": 1,
                "tableField": "FIELD6",
                "field": "field6",
                "fileDataType": "01",
                "linkId": "1",
                "component": "input-text",
                "formatType": "",
                "format": "",
                "fieldName": "备用6"
            }
        ]
        return list

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
        time = str(datetime.date.today())
        return time

    # yaml文件内容转换成json格式
    def yaml_to_json(self,yamlPath):
        with open(yamlPath, encoding="utf-8") as f:
            datas = yaml.load(f, Loader=yaml.FullLoader)  # 将文件的内容转换为字典形式
        jsonDatas = json.dumps(datas, indent=5)  # 将字典的内容转换为json格式的字符串
        return jsonDatas


if __name__=='__main__':
    print(DebugTalk().set_step_random_string(6))