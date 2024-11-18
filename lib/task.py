
from config import HOST1
import allure
import requests
import random,time

#获取当前时间
def get_current_time():
    # 获取当前时间的时间戳
    timestamp = time.time()
    # 将时间戳转换为本地时间
    local_time = time.localtime(timestamp)
    # 将本地时间转换为易读的字符串形式
    readable_time = time.asctime(local_time)
    # 格式化当前时间
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    return formatted_time

#任务定制
@allure.step('step:获取实例ID')
def task_get_model(t):
    url=f"{HOST1}/api/agnes-ac/v2/model/code/get-model-code?model=case"
    headers = {
        'cookie': 'token=' + t
    }
    payload={

    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:填写任务名称')
def task_pre_save(t,caseid):
    url=f"{HOST1}/api/agnes-ac/v1/ac/mot/task/case/pre-save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "reTaskDef": {
                "caseKey": caseid,
                "taskName": "自动化测试任务00"+str(random.randint(100000,999999)),
                "configDef": "caseV3",
                "disType": "2"
            },
            "isCheckCode": True
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:单节点-获取当前任务下step')
def task_get_single_step(t):
    url=f"{HOST1}/api/agnes-ac/v2/model/code/get-model-code?model=step"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:配置任务信息')
def task_add(t,taskname,caseid,taskid,casedefid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "reTaskDef": {
            "disType": "2",
            "updateUser": "agnes",
            "taskName": taskname,
            "crtTs": get_current_time(),
            "crtUser": "agnes",
            "caseKey": caseid,
            "isDel": "0",
            "updateTs": get_current_time(),
            "taskId": taskid,
            "taskInitDays": 0,
            "taskStatus": "01",
            "configDef": "caseV3",
            "themeId": "00000060",
            "themeName": "",
            "taskType": "common",
            "taskLevel": 1,
            "taskTitle": {
              "html": "<span key=\"taskInformation.taskName\" contenteditable=\"false\" class=\"tag\">任务信息.任务名称</span><span key=\"taskInformation.liablePer\" contenteditable=\"false\" class=\"tag\">任务信息.责任人</span>",
              "res": "${taskInformation.taskName}${taskInformation.liablePer}"
            },
            "zrUserPzMethod": "1",
            "zrUser": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
            "xzUserPzMethod": "1",
            "xzUser": "[]",
            "isInvolvedPrdt": "0",
            "prdtRuleJson": "",
            "jrdb": "1",
            "yxyq": "0",
            "yxzb": "0",
            "yxzf": "0",
            "yxcxzx": "1",
            "yxsggy": "1",
            "taskDesc": "",
            "caseDefId": casedefid,
            "execMode": "1",
            "funcId": "1ixea36dtwqvq_1",
            "eventId": "",
            "workdayAreaCode": "CN",
            "planStartTs": "00:00:00",
            "planEndTs": "23:59:59",
            "actionParam": "[{\"paramName\":\"bizStartDate\",\"paramNameFormat\":\"业务开始日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"bizEndDate\",\"paramNameFormat\":\"业务结束日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planStartDate\",\"paramNameFormat\":\"执行开始日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizStartDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planEndDate\",\"paramNameFormat\":\"执行结束日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizEndDate\",\"paramShif\":0,\"paramDateType\":\"0\"}]",
            "remindPlanId": "",
            "addType": "regularAdd"
          },
          "caseDefBody": "{\"actions\":[],\"optionalStages\":[],\"stages\":[{\"defId\":\"\",\"defName\":\"default\",\"defType\":\"stage\",\"optional\":true,\"edit\":false,\"defBody\":{},\"children\":[{\"stepName\":\"测试单节点任务01\",\"defType\":\"step\",\"stepActType\":\"\",\"stepId\":\"\",\"edit\":false,\"stepFormInfo\":{\"caseStepDef\":{\"stepCode\":\"step-00001248\",\"stageName\":\"\",\"stepName\":\"测试单节点任务01\",\"stepLevel\":0,\"encodingRule\":\"00008085\",\"stepTag\":[],\"zrUserPzMethod\":\"0\",\"zrUser\":\"\",\"xzUserPzMethod\":\"0\",\"xzUser\":\"\",\"stepActOwner\":\"\",\"stepCollaborateOwner\":\"\",\"jrdb\":\"1\",\"yxyq\":\"0\",\"yxzb\":\"0\",\"yxzf\":\"0\",\"yxcxzx\":\"1\",\"yxsggy\":\"1\",\"dbzxazjdzs\":\"0\",\"jdcxzx\":\"0\",\"jdwxcxzx\":\"0\",\"notifyRuleFlag\":\"0\",\"startTimeFlag\":\"0\",\"endTimeFlag\":\"0\",\"notifyRule\":\"0\",\"parmSetFlag\":\"0\",\"stepRemark\":\"\",\"baseDateType\":\"0\",\"startTime\":\"00:00\",\"startBaseDay\":\"\",\"startDayType\":\"00\",\"startCrossDayType\":\"0\",\"startDay\":\"\",\"endTime\":\"23:59\",\"endBaseDay\":\"\",\"endDayType\":\"00\",\"endCrossDayType\":\"0\",\"endDay\":\"0\",\"isTodo\":\"0\",\"isNotCrtJob\":\"0\",\"allowManualConfirm\":\"1\",\"isAllowExecAgain\":\"0\",\"allowActionConfirm\":\"0\",\"allowShowDetail\":\"0\",\"allowFormAction\":\"0\",\"allowEditEndTime\":\"0\",\"paramsOutData\":[],\"warningMintues\":\"\",\"stepExecMode\":\"FREQUENCY\"},\"failRuleTableData\":{\"judgeScript\":\"\"},\"successRuleTableData\":{\"judgeScript\":\"\"},\"activeRuleTableData\":{\"judgeScript\":\"\"},\"timeoutRuleTableData\":{\"judgeScript\":\"\"},\"exceptionRemind\":[],\"finishRemind\":[],\"timeoutRemind\":[],\"serviceResponseId\":\"\",\"isRecordTimeoutError\":\"0\",\"warningRemind\":[]}}]}],\"version\":\"0\",\"stepCodeArr\":{\"step-00001248\":\"step-00001248\"}}",
          "caseDefId": casedefid,
          "isCheckCode": False,
          "taskDeploys": []
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:新增积木')
def task_saveblock(t,stepid,caseid,blocktype,blockcode):
    url=f"{HOST1}/api/agnes-ac/v2/block/saveChildBlock"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "stepId": stepid,
          "caseKey": caseid,
          "childBlockType": blocktype,
          "childBlockCode": blockcode,
          "jgNum": "",
          "dw": "",
          "execMode": "0",
          "execStartTs": "00:00:00",
          "execEndTs": "23:59:00"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:编辑积木')
def task_editblock(t,stepid,caseid,blocktype,blockcode,blockindex,pkid):
    url=f"{HOST1}/api/agnes-ac/v2/block/saveChildBlock"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "stepId": stepid,
          "caseKey": caseid,
          "childBlockCode": blockcode,
          "childBlockIndex":blockindex ,
          "childBlockName": "",
          "childBlockType": blocktype,
          "dw": "",
          "execEndTs": "23:59:00",
          "execMode": "1",
          "execStartTs": "00:00:00",
          "jgNum": "",
          "pkId": pkid,
          "remark": "积木块编辑",
          "totalNum": "7",
          "updateTs": get_current_time(),
          "updateUser": "致宇小智"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:上下移动积木顺序')
def task_block_exchange(t,stepid):
    url=f"{HOST1}/api/agnes-ac/v2/block/exchange"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "stepId": stepid,
          "orderId": 2,
          "exchangeOrderId": 1
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:删除积木块')
def task_block_delete(t,pkid,stepid,blockindex):
    url=f"{HOST1}/api/agnes-ac/v2/block/deleteChildBlock"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pkId": pkid,
            "stepId": stepid,
            "childBlockIndex": blockindex
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:审核任务')
def task_check(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/check"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "taskDefs": [
                {
                    "taskId": taskid,
                    "taskStatus": "08"
                }
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:验收任务')
def task_acceptance(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/acceptance"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
  "taskDefs": [
        {
          "taskId": taskid,
          "taskStatus": "02"
        }
      ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:发布任务-新增任务发布')
def task_publish(t,casedefid,caseid,taskid,taskname,crtts):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/publish"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
                "reTaskDef": {
                    "actionParam": "[{\"paramName\":\"bizStartDate\",\"paramNameFormat\":\"业务开始日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"bizEndDate\",\"paramNameFormat\":\"业务结束日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planStartDate\",\"paramNameFormat\":\"执行开始日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizStartDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planEndDate\",\"paramNameFormat\":\"执行结束日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizEndDate\",\"paramShif\":0,\"paramDateType\":\"0\"}]",
                    "addType": "regularAdd",
                    "bizTag": "",
                    "canFb": "2",
                    "canHt": "2",
                    "canSc": "2",
                    "canSet": "2",
                    "canSh": "1",
                    "canTy": "2",
                    "canYs": "2",
                    "caseDefId": casedefid,
                    "caseKey": caseid,
                    "configDef": "caseV3",
                    "crtTs": crtts,
                    "crtUser": "agnes",
                    "disType": "2",
                    "eventId": "",
                    "execMode": "1",
                    "funcId": "1ixea36dtwqvq_1",
                    "isCanEdit": "2",
                    "isDel": "0",
                    "isInvolvedPrdt": "0",
                    "jrdb": "1",
                    "planEndTs": "23:59:59",
                    "planStartTs": "00:00:00",
                    "prdtRuleJson": "",
                    "remindPlanId": "",
                    "taskDesc": "",
                    "taskId": taskid,
                    "taskInitDays": 0,
                    "taskLevel": "1",
                    "taskName": taskname,
                    "taskStatus": "02",
                    "taskTitle": "{\"res\":\"${taskInformation.taskName}${taskInformation.liablePer}\",\"html\":\"<span key=\\\"taskInformation.taskName\\\" contenteditable=\\\"false\\\" class=\\\"tag\\\">任务信息.任务名称</span><span key=\\\"taskInformation.liablePer\\\" contenteditable=\\\"false\\\" class=\\\"tag\\\">任务信息.责任人</span>\"}",
                    "taskType": "common",
                    "themeId": "00000060",
                    "themeName": "上海银行指标监控",
                    "updateTs": get_current_time(),
                    "updateUser": "agnes",
                    "versionId": 0,
                    "workdayAreaCode": "CN",
                    "xzUser": "[]",
                    "xzUserPzMethod": "1",
                    "yxcxzx": "1",
                    "yxsggy": "1",
                    "yxyq": "0",
                    "yxzb": "0",
                    "yxzf": "0",
                    "zrUser": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
                    "zrUserPzMethod": "1"
                },
                "caseDefId": casedefid,
                "caseDefBody": "{\"actions\":[],\"optionalStages\":[],\"stages\":[{\"defId\":\"\",\"defName\":\"default\",\"defType\":\"stage\",\"optional\":true,\"edit\":false,\"defBody\":{},\"children\":[{\"stepName\":\"测试单节点任务01\",\"defType\":\"step\",\"stepActType\":\"\",\"stepId\":\"\",\"edit\":false,\"stepFormInfo\":{\"caseStepDef\":{\"stepCode\":\"step-00001248\",\"stageName\":\"\",\"stepName\":\"测试单节点任务01\",\"stepLevel\":0,\"encodingRule\":\"00008085\",\"stepTag\":[],\"zrUserPzMethod\":\"0\",\"zrUser\":\"\",\"xzUserPzMethod\":\"0\",\"xzUser\":\"\",\"stepActOwner\":\"\",\"stepCollaborateOwner\":\"\",\"jrdb\":\"1\",\"yxyq\":\"0\",\"yxzb\":\"0\",\"yxzf\":\"0\",\"yxcxzx\":\"1\",\"yxsggy\":\"1\",\"dbzxazjdzs\":\"0\",\"jdcxzx\":\"0\",\"jdwxcxzx\":\"0\",\"notifyRuleFlag\":\"0\",\"startTimeFlag\":\"0\",\"endTimeFlag\":\"0\",\"notifyRule\":\"0\",\"parmSetFlag\":\"0\",\"stepRemark\":\"\",\"baseDateType\":\"0\",\"startTime\":\"00:00\",\"startBaseDay\":\"\",\"startDayType\":\"00\",\"startCrossDayType\":\"0\",\"startDay\":\"\",\"endTime\":\"23:59\",\"endBaseDay\":\"\",\"endDayType\":\"00\",\"endCrossDayType\":\"0\",\"endDay\":\"0\",\"isTodo\":\"0\",\"isNotCrtJob\":\"0\",\"allowManualConfirm\":\"1\",\"isAllowExecAgain\":\"0\",\"allowActionConfirm\":\"0\",\"allowShowDetail\":\"0\",\"allowFormAction\":\"0\",\"allowEditEndTime\":\"0\",\"paramsOutData\":[],\"warningMintues\":\"\",\"stepExecMode\":\"FREQUENCY\"},\"failRuleTableData\":{\"judgeScript\":\"\"},\"successRuleTableData\":{\"judgeScript\":\"\"},\"activeRuleTableData\":{\"judgeScript\":\"\"},\"timeoutRuleTableData\":{\"judgeScript\":\"\"},\"exceptionRemind\":[],\"finishRemind\":[],\"timeoutRemind\":[],\"serviceResponseId\":\"\",\"isRecordTimeoutError\":\"0\",\"warningRemind\":[]}}]}],\"version\":\"0\",\"stepCodeArr\":{\"step-00001248\":\"step-00001248\"}}"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:发布任务-快速新增任务发布')
def task_publish_quick(t,casedefid,caseid,taskid,taskname,crtts):
    url=f"{HOST1}//api/agnes-ac/v1/mcc/theme/info/task/publish"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
                "reTaskDef": {
                    "actionParam": "",
                    "addType": "quickAdd",
                    "canFb": "1",
                    "canHt": "1",
                    "canSc": "1",
                    "canSet": "1",
                    "canSh": "1",
                    "canTy": "1",
                    "canYs": "1",
                    "caseDefId": casedefid,
                    "caseKey": caseid,
                    "configDef": "caseV3",
                    "crtTs": crtts,
                    "crtUser": "agnes",
                    "disType": "2",
                    "eventId": "",
                    "execMode": "1",
                    "funcId": "",
                    "isCanEdit": "1",
                    "isDel": "0",
                    "isInvolvedPrdt": "1",
                    "jrdb": "1",
                    "planEndTs": "23:59:59",
                    "planStartTs": "00:00:00",
                    "prdtRuleJson": "product_status-like-'%04%'",
                    "remindPlanId": "",
                    "taskAddParams": "{\"taskTitleFlag\":\"0\",\"zdgw\":\"\",\"zdpb\":\"1\",\"zdxzr\":\"\",\"jobRule\":\"\",\"schedualRule\":\"00\",\"cpfwType\":\"0\",\"quickFuncId\":\"\",\"ywDateFlag\":\"\",\"num\":\"\",\"tzCustom\":\"\",\"paramSetting\":\"100011\",\"paramCustom\":\"\",\"notificationPlan\":\"\"}",
                    "taskDesc": "",
                    "taskId": taskid,
                    "taskInitDays": 0,
                    "taskLevel": "1",
                    "taskName": taskname,
                    "taskStatus": "02",
                    "taskTitle": "{\"res\":\"${taskInformation.taskName}${productInformation.productAbbreviation}${productInformation.productCode}\",\"html\":\"default<span key=\\\"taskInformation.taskName\\\" contenteditable=\\\"false\\\" class=\\\"tag\\\">任务信息.任务名称</span><span key=\\\"productInformation.productName\\\" contenteditable=\\\"false\\\" class=\\\"tag\\\">产品信息.产品名称</span><span key=\\\"productInformation.productCode\\\" contenteditable=\\\"false\\\" class=\\\"tag\\\">产品信息.产品代码</span>\"}",
                    "taskType": "prdt",
                    "themeId": "00000063",
                    "themeName": "任务主题",
                    "updateTs": get_current_time(),
                    "updateUser": "agnes",
                    "versionId": 0,
                    "workdayAreaCode": "CN",
                    "xzUser": "",
                    "xzUserPzMethod": "",
                    "yxcxzx": "1",
                    "yxsggy": "1",
                    "yxyq": "0",
                    "yxzb": "0",
                    "yxzf": "0",
                    "zrUser": "{\"pkId\":\"cppb\",\"jobRule\":{\"editFlag\":\"\",\"value\":\"\"},\"schedualRule\":{\"editFlag\":\"\",\"value\":\"00\"},\"allocRule\":{\"editFlag\":\"\",\"value\":\"1\"},\"customRule\":{\"editFlag\":\"\",\"value\":\"\"}}",
                    "zrUserPzMethod": "2"
                },
                "caseDefId": casedefid,
                "caseDefBody": "{\"actions\":[],\"optionalStages\":[],\"stages\":[{\"defId\":\"\",\"defName\":\"default\",\"defType\":\"stage\",\"optional\":true,\"edit\":false,\"defBody\":{},\"children\":[{\"stepName\":\"default\",\"defType\":\"step\",\"stepActType\":\"\",\"stepId\":\"\",\"edit\":false,\"stepFormInfo\":{\"caseStepDef\":{\"stepCode\":\"step-00001412\",\"stageName\":\"\",\"stepName\":\"default\",\"stepLevel\":0,\"encodingRule\":\"00008085\",\"stepTag\":[],\"zrUserPzMethod\":\"0\",\"zrUser\":\"\",\"xzUserPzMethod\":\"0\",\"xzUser\":\"\",\"stepActOwner\":\"\",\"stepCollaborateOwner\":\"\",\"jrdb\":\"1\",\"yxyq\":\"0\",\"yxzb\":\"0\",\"yxzf\":\"0\",\"yxcxzx\":\"1\",\"yxsggy\":\"1\",\"dbzxazjdzs\":\"0\",\"jdcxzx\":\"0\",\"jdwxcxzx\":\"0\",\"notifyRuleFlag\":\"0\",\"startTimeFlag\":\"0\",\"endTimeFlag\":\"0\",\"notifyRule\":\"0\",\"parmSetFlag\":\"0\",\"stepRemark\":\"\",\"baseDateType\":\"0\",\"startTime\":\"00:00\",\"startBaseDay\":\"\",\"startDayType\":\"00\",\"startCrossDayType\":\"0\",\"startDay\":\"\",\"endTime\":\"23:59\",\"endBaseDay\":\"\",\"endDayType\":\"00\",\"endCrossDayType\":\"0\",\"endDay\":\"0\",\"isTodo\":\"0\",\"isNotCrtJob\":\"0\",\"allowManualConfirm\":\"1\",\"isAllowExecAgain\":\"0\",\"allowActionConfirm\":\"0\",\"allowShowDetail\":\"0\",\"allowFormAction\":\"0\",\"allowEditEndTime\":\"0\",\"paramsOutData\":[],\"warningMintues\":\"\",\"stepExecMode\":\"FREQUENCY\"},\"failRuleTableData\":{\"judgeScript\":\"\"},\"successRuleTableData\":{\"judgeScript\":\"\"},\"activeRuleTableData\":{\"judgeScript\":\"\"},\"timeoutRuleTableData\":{\"judgeScript\":\"\"},\"exceptionRemind\":[],\"finishRemind\":[],\"timeoutRemind\":[],\"serviceResponseId\":\"\",\"isRecordTimeoutError\":\"0\",\"warningRemind\":[]}}]}],\"version\":\"0\",\"stepCodeArr\":{\"step-00001412\":\"step-00001412\"}}"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:回退任务')
def task_back(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/back"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "taskDefs": [
                {
                    "taskId": taskid,
                    "taskStatus": "01"
                }
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:停用任务')
def task_stop(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/stop"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "taskDefs": [
            {
              "taskId": taskid
            }
          ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:删除任务')
def task_del(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/del"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "taskDefs": [
                {
                    "taskId": taskid,
                    "isDel": "1"
                }
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:快速新增')
def task_add_quick(t,caseid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "reTaskDef": {
            "caseKey": caseid,
            "taskName":"自动化测试-快速新增任务00"+str(random.randint(100000,999999)) ,
            "configDef": "caseV3",
            "disType": "2",
            "themeId": "00000063",
            "taskType": "prdt",
            "taskTitle": {
                "html": "default<span key=\"taskInformation.taskName\" contenteditable=\"false\" class=\"tag\">任务信息.任务名称</span><span key=\"productInformation.productName\" contenteditable=\"false\" class=\"tag\">产品信息.产品名称</span><span key=\"productInformation.productCode\" contenteditable=\"false\" class=\"tag\">产品信息.产品代码</span>",
                "res": "${taskInformation.taskName}${productInformation.productAbbreviation}${productInformation.productCode}"
            },
            "isInvolvedPrdt": "1",
            "zrUserPzMethod": "2",
            "zrUser": "{\"pkId\":\"cppb\",\"jobRule\":{\"editFlag\":\"\",\"value\":\"\"},\"schedualRule\":{\"editFlag\":\"\",\"value\":\"00\"},\"allocRule\":{\"editFlag\":\"\",\"value\":\"1\"},\"customRule\":{\"editFlag\":\"\",\"value\":\"\"}}",
            "xzUserPzMethod": "",
            "xzUser": "",
            "taskLevel": "1",
            "execMode": "1",
            "funcId": "",
            "eventId": "",
            "actionParam": "",
            "workdayAreaCode": "CN",
            "planStartTs": "00:00:00",
            "planEndTs": "23:59:59",
            "jrdb": "1",
            "yxyq": "0",
            "yxzb": "0",
            "yxzf": "0",
            "yxcxzx": "1",
            "yxsggy": "1",
            "taskDesc": "",
            "remindPlanId": "",
            "taskAddParams": "{\"taskTitleFlag\":\"0\",\"zdgw\":\"\",\"zdpb\":\"1\",\"zdxzr\":\"\",\"jobRule\":\"\",\"schedualRule\":\"00\",\"cpfwType\":\"0\",\"quickFuncId\":\"\",\"ywDateFlag\":\"\",\"num\":\"\",\"tzCustom\":\"\",\"paramSetting\":\"100011\",\"paramCustom\":\"\",\"notificationPlan\":\"\"}",
            "prdtRuleJson": "product_status-like-'%04%'",
            "addType": "quickAdd"
        },
        "caseDefBody": "{\"actions\":[],\"optionalStages\":[],\"stages\":[{\"defId\":\"\",\"defName\":\"default\",\"defType\":\"stage\",\"optional\":true,\"edit\":false,\"defBody\":{},\"children\":[{\"stepName\":\"default\",\"defType\":\"step\",\"stepActType\":\"\",\"stepId\":\"\",\"edit\":false,\"stepFormInfo\":{\"caseStepDef\":{\"stepCode\":\"step-00001412\",\"stageName\":\"\",\"stepName\":\"default\",\"stepLevel\":0,\"encodingRule\":\"00008085\",\"stepTag\":[],\"zrUserPzMethod\":\"0\",\"zrUser\":\"\",\"xzUserPzMethod\":\"0\",\"xzUser\":\"\",\"stepActOwner\":\"\",\"stepCollaborateOwner\":\"\",\"jrdb\":\"1\",\"yxyq\":\"0\",\"yxzb\":\"0\",\"yxzf\":\"0\",\"yxcxzx\":\"1\",\"yxsggy\":\"1\",\"dbzxazjdzs\":\"0\",\"jdcxzx\":\"0\",\"jdwxcxzx\":\"0\",\"notifyRuleFlag\":\"0\",\"startTimeFlag\":\"0\",\"endTimeFlag\":\"0\",\"notifyRule\":\"0\",\"parmSetFlag\":\"0\",\"stepRemark\":\"\",\"baseDateType\":\"0\",\"startTime\":\"00:00\",\"startBaseDay\":\"\",\"startDayType\":\"00\",\"startCrossDayType\":\"0\",\"startDay\":\"\",\"endTime\":\"23:59\",\"endBaseDay\":\"\",\"endDayType\":\"00\",\"endCrossDayType\":\"0\",\"endDay\":\"0\",\"isTodo\":\"0\",\"isNotCrtJob\":\"0\",\"allowManualConfirm\":\"1\",\"isAllowExecAgain\":\"0\",\"allowActionConfirm\":\"0\",\"allowShowDetail\":\"0\",\"allowFormAction\":\"0\",\"allowEditEndTime\":\"0\",\"paramsOutData\":[],\"warningMintues\":\"\",\"stepExecMode\":\"FREQUENCY\"},\"failRuleTableData\":{\"judgeScript\":\"\"},\"successRuleTableData\":{\"judgeScript\":\"\"},\"activeRuleTableData\":{\"judgeScript\":\"\"},\"timeoutRuleTableData\":{\"judgeScript\":\"\"},\"exceptionRemind\":[],\"finishRemind\":[],\"timeoutRemind\":[],\"serviceResponseId\":\"\",\"isRecordTimeoutError\":\"0\",\"warningRemind\":[]}}]}],\"version\":\"0\",\"stepCodeArr\":{\"step-00001412\":\"step-00001412\"}}",
        "isCheckCode": False,
        "taskDeploys": []
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

#查询
@allure.step('step:查询用户可见任务主题')
def task_query_theme(t,userid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/get"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "userId": userid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:查询主题任务')
def task_query_theme_task(t,themeid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/query?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "themeId": themeid,
            "taskName": '',
            "disTypes": [
                "0",
                "1",
                "2"
            ],
            "taskStatusArr": [
                "01",
                "02",
                "03",
                "08",
                "09"
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:获取快速新增任务的casedefid')
def task_query_theme_task_casedefid(t,themeid,taskname):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/query?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "themeId": themeid,
            "taskName": taskname,
            "disTypes": [],
            "taskStatusArr": []
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:获取某个任务下所有的step(获取stepid)')
def task_get_step(t,caseid):
    url=f"{HOST1}/api/agnes-ac/v2/block/get/has-block/step"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "caseKey": caseid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:获取某个积木类型下所有的积木块')
def task_get_block(t,blocktype):
    url=f"{HOST1}/api/agnes-ac/v2/block/query"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "blockType": blocktype
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:获取某个step下所有的积木块(获取积木块的pkid,blocktype,blockcode,blockindex)')
def task_get_step_block(t,stepid):
    url=f"{HOST1}/api/agnes-ac/v2/block/getBlockByStepCode?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "stepCode": stepid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

#任务中心
@allure.step('step:置顶')
def task_topping(host,t,taskid):
    url=f"{host}/api/agnes-ac/v1/mcc/task/pending/Topping"
    headers={
        'cookie':'token='+t
    }
    payload={
            "taskId": [
                taskid
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:取消置顶')
def task_cancelTopping(host,t,taskid):
    url=f"{host}/api/agnes-ac/v1/mcc/task/pending/cancelTopping"
    headers={
        'cookie':'token='+t
    }
    payload={
            "taskId": [
                taskid
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:完成任务')
def task_submit(t,caseid,taskid,taskname,crtts):
    url=f"{HOST1}/api/agnes-ac/v1/ac/task/manage/submit-tasks"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
      "taskList": [
        {
          "attUser": "致宇小智",
          "bizTimeFrom": "2024-11-07",
          "bizTimeTo": "2024-11-07",
          "caseId": caseid,
          "crtTs": crtts ,
          "crtUser": "autotask",
          "disType": "2",
          "exeTime": "2024-11-07",
          "executeUser": "autotask",
          "isPending": "1",
          "pkId": "1j5q5f4memmqe",
          "prdtInfo": "-_-",
          "process": 0,
          "taskExecAuth": "1000",
          "taskId": taskid,
          "taskLevel": "1",
          "taskName": taskname,
          "taskStatus": "02",
          "taskTag": "",
          "taskTimeFrom": "2024-11-07 00:00:00",
          "taskTimeTo": "2024-11-07 23:59:59",
          "taskType": "common",
          "updateTs": get_current_time(),
          "remark": "任务完成"
        }
      ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:转办')
def task_approval_add1(t):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/batch/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "applyUser": "agnes",
        "type": "4",
        "reason": "转办",
        "approvalUser": "agnes",
        "applyData": {
          "userName": "",
          "zrUserInfo": "[{\"refType\":\"1\",\"memberId\":\"admin\",\"memberDesc\":\"系统管理员\"}]",
          "planEndTs": "",
          "approver": "agnes",
          "remark": "转办",
          "taskName": "仅待办-临时任务1",
          "taskTime": "2024-11-14 00:00 至 2024-11-14 23:59",
          "caseIds": [
            "20241114-0000000000232535"
          ],
          "pkId": "1j6f0iaknewek",
          "userId": "agnes",
          "rows": []
        },
        "summary": "任务标题 : 仅待办-临时任务1\n任务日期 : 2024-11-14 00:00 至 2024-11-14 23:59\n转办人 :系统管理员"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:延期')
def task_approval_add2(t):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/batch/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "applyUser": "agnes",
            "type": "1",
            "reason": "延期",
            "approvalUser": "admin",
            "applyData": {
              "tasks": {
                "caseId": "20241114-0000000000232535",
                "userName": "",
                "zrUserInfo": "",
                "planEndTs": "2024-11-30 00:00:00",
                "approver": "admin",
                "remark": "延期",
                "taskName": "",
                "taskTime": ""
              }
            },
            "summary": "任务标题 : 仅待办-临时任务1\n任务日期 : 2024-11-14 00:00 至 2024-11-14 23:59\n延期时间 : 2024-11-30 00:00:00\n"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:作废')
def task_cancel(t):
    url=f"{HOST1}/api/agnes-ac/v1/ac/task/manage/cancel"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "userName": "",
          "zrUserInfo": "",
          "planEndTs": "",
          "approver": "",
          "remark": "作废",
          "taskName": "仅待办-临时任务1",
          "taskTime": "2024-11-14 00:00 至 2024-11-14 23:59",
          "taskId": "temp",
          "pkId": "1j6f0iaknewek",
          "caseId": "20241114-0000000000232535",
          "rows": [
            {
              "attUser": "致宇小智",
              "caseId": "20241114-0000000000232535",
              "crtTs": "2024-11-14 10:40:04",
              "crtUser": "agnes",
              "disType": "temp",
              "exeTime": "2024-11-14",
              "pkId": "1j6f0iaknewek",
              "process": 0,
              "taskExecAuth": "1111",
              "taskLevel": "1",
              "taskName": "仅待办-临时任务1",
              "taskStatus": "02",
              "taskTag": "",
              "taskTimeFrom": "2024-11-14 00:00:00",
              "taskTimeTo": "2024-11-14 23:59:00",
              "taskType": "temp"
            }
          ]
}
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:创建临时任务')
def task_addtemp_temptask(t):
    url=f"{HOST1}/api/agnes-ac/v1/config/exe/task/temp-task/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "taskName": "临时任务1",
            "bizTag": "",
            "bizTagName": "",
            "crtType": "1",
            "zrUserInfo": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
            "planStartTs": "2024-11-14 00:00:00",
            "planEndTs": "2024-11-14 23:59:00",
            "taskDesc": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:创建场景任务')
def task_addtemp_themetask(t):
    url=f"{HOST1}/api/agnes-ac/v1/config/exe/task/theme/temp-task/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "taskName": "场景任务1",
          "zrUserInfo": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
          "startDate": "2024-11-14",
          "endDate": "2024-11-14",
          "themeName": "测试指标",
          "taskId": "1j5ncnidnzlhy",
          "caseKey": "1j5ncnidnzlhy",
          "prdtCode": "",
          "prdtName": "",
          "varMap": {}
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#查询
@allure.step('step:查询今日必办')
def task_query_1(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "showType": "00",
        "authQueryParam2": "1",
        "taskName": "",
        "taskStatus": "01,02,03,04",
        "taskType": "",
        "basePath": "",
        "startDate": "",
        "endDate": "",
        "taskCls": "",
        "cardType": "",
        "residueTime": "",
        "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询超时任务')
def task_query_2(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "showType": "00",
        "authQueryParam2": "2",
        "taskName": "",
        "taskStatus": "04",
        "taskType": "",
        "basePath": "",
        "startDate": "",
        "endDate": "",
        "taskCls": "",
        "cardType": "",
        "residueTime": "",
        "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询今日异常')
def task_query_3(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "showType": "00",
        "authQueryParam2": "3",
        "taskName": "",
        "taskStatus": "03",
        "taskType": "",
        "basePath": "",
        "startDate": "",
        "endDate": "",
        "taskCls": "",
        "cardType": "",
        "residueTime": "",
        "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询可提前办')
def task_query_4(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "showType": "00",
        "authQueryParam2": "4",
        "taskName": "",
        "taskStatus": "02,03,04",
        "taskType": "",
        "basePath": "",
        "startDate": "",
        "endDate": "",
        "taskCls": "",
        "cardType": "",
        "residueTime": "",
        "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询我的发布')
def task_query_5(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "showType": "00",
        "authQueryParam2": "5",
        "taskName": "",
        "taskStatus": "01,02,03,04",
        "taskType": "",
        "basePath": "",
        "startDate": "",
        "endDate": "",
        "taskCls": "",
        "cardType": "",
        "residueTime": "",
        "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:仅待办')
def task_query_task1(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/queryForTask"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "basePath": "R0000001",
          "startDate": "2024-11-14",
          "endDate": "2024-11-14",
          "taskCls": "",
          "showType": "00"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:仅转交')
def task_query_task2(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/queryForTask"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "basePath": "R0000001",
            "startDate": "2024-11-14",
            "endDate": "2024-11-14",
            "taskCls": "02",
            "showType": "00"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r


if __name__=='__main__':
    print()
