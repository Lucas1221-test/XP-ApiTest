
from config import HOST1
import allure
import requests
import random,datetime
from common.read_yml import get_current_time,read_yml


#任务定制
@allure.step('step:新增任务主题')
def task_theme_save(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "themeName": "自动化任务主题"+str(random.randint(100000,999999)),
            "parentThemeId": "R0000001"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

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
    #caseid = r.json()['data']

@allure.step('step:填写任务名称,获取taskname,crtts,crtuser,updatets,updateuser,taskid,taskinitdays,taskstatus,casedefid,casetype,distype')
def task_pre_save(t,caseid,casetype,distype):
    url=f"{HOST1}/api/agnes-ac/v1/ac/mot/task/case/pre-save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "reTaskDef": {
                "caseKey": caseid,
                "taskName": "自动化测试任务"+str(random.randint(100000,999999)),
                "configDef": casetype,     #casetype:单节点任务-caseV3
                "disType": distype             #distype:岗位任务："2"
            },
            "isCheckCode": True
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    '''
    taskname = r1.json()['data']['reTaskDef']['taskName']
    taskid = r1.json()['data']['reTaskDef']['taskId']
    casedefid = r1.json()['data']['caseDefId']
    crtts = r1.json()['data']['reTaskDef']['crtTs']
    crtuser = r1.json()['data']['reTaskDef']['crtUser']
    updatets = r1.json()['data']['reTaskDef']['updateTs']
    updatetuser = r1.json()['data']['reTaskDef']['updateUser']
    distype = r1.json()['data']['reTaskDef']['disType']
    taskinitdays = r.json()['data']['reTaskDef']['taskInitDays']
    taskstatus = r.json()['data']['reTaskDef']['taskStatus']
    casetype = r.json()['data']['reTaskDef']['configDef']
'''

@allure.step('step:生成任务实例')
def task_save_xcpmodel(t,caseid,taskname):
    url=f"{HOST1}/api/agnes-ac/v2/ac/obj/def/save-xcp-model"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "xcpInfo": {
                "apiCode": "bb823a2b6ff58df9e5d90d6b593be22b",
                "body": {
                    "dsId": "default",
                    "datatype": caseid,
                    "datatypeName": taskname,
                    "fieldList": [
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
                    ],
                    "linkList": [],
                    "tableName": "AC_RU_CASE_MODEL_DEF"
                }
            }

    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询用户可见任务主题，获取themeid,themename,canfb,canht,cansc,canset,cansh,canty,canys')
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
    '''themeid=r.json()['data'][0]['pkId']
    themename=r.json()['data'][0]['themeName']
    canfb=r.json()['data'][0]['canFb']
    canht=r.json()['data'][0]['canHt']
    cansc=r.json()['data'][0]['canSc']
    canset=r.json()['data'][0]['canSet']
    cansh=r.json()['data'][0]['canSh']
    canty=r.json()['data'][0]['canTy']
    canys=r.json()['data'][0]['canYs']'''

@allure.step('step:单节点任务-获取当前任务下stepcode')
def task_get_single_step(t):
    url=f"{HOST1}/api/agnes-ac/v2/model/code/get-model-code?model=step"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    #stepcode=r.json()['data']

@allure.step('step: 查询频率列表，获取funcid')
def task_get_frequencyinfo(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/exec/getFrequencyInfo"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    #funcid=r.json()['data'][0]['fnId']

@allure.step('step:单节点任务-配置任务信息')
def task_add(t,distype,updateuser,taskname,crtts,crtuser,caseid,updatets,taskid,taskinitdays,taskstatus,casetype,themeid,casedefid,funcid,stepcode):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "reTaskDef": {
            "disType": distype,
            "updateUser": updateuser,
            "taskName": taskname,
            "crtTs": crtts,
            "crtUser": crtuser,
            "caseKey": caseid,
            "isDel": "0",
            "updateTs": updatets,
            "taskId": taskid,
            "taskInitDays": taskinitdays,
            "taskStatus": taskstatus,
            "configDef": casetype,
            "themeId": themeid,
            "themeName": "",
            "taskType": "common",
            "taskLevel": 1,
            "taskTitle": {
              "html": "<span key=\"taskInformation.taskName\" contenteditable=\"false\" class=\"tag\">任务信息.任务名称</span>",
              "res": "${taskInformation.taskName}"
            },
            "zrUserPzMethod": "1",
            "zrUser": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
            "xzUserPzMethod": "1",
            "xzUser": "[]",
            "isInvolvedPrdt": "0",
            "prdtRuleJson": "",
            "jrdb": "1",
            "yxyq": "1",
            "yxzb": "1",
            "yxzf": "1",
            "yxcxzx": "1",
            "yxsggy": "1",
            "applyType": "",
            "taskDesc": "",
            "caseDefId": casedefid,
            "execMode": "1",
            "funcId": funcid,
            "eventId": "",
            "workdayAreaCode": "CN",
            "planStartTs": "00:00:00",
            "planEndTs": "23:59:59",
            "actionParam": "[{\"paramName\":\"bizStartDate\",\"paramNameFormat\":\"业务开始日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"bizEndDate\",\"paramNameFormat\":\"业务结束日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planStartDate\",\"paramNameFormat\":\"执行开始日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizStartDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planEndDate\",\"paramNameFormat\":\"执行结束日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizEndDate\",\"paramShif\":0,\"paramDateType\":\"0\"}]",
            "remindPlanId": "",
            "addType": "regularAdd"
          },
          #"caseDefBody": "{\"actions\":[],\"optionalStages\":[],\"stages\":[{\"defId\":\"\",\"defName\":\"default\",\"defType\":\"stage\",\"optional\":true,\"edit\":false,\"defBody\":{},\"children\":[{\"stepName\":\"0-0-7\",\"defType\":\"step\",\"stepActType\":\"\",\"stepId\":\"\",\"edit\":false,\"stepFormInfo\":{\"caseStepDef\":{\"stepCode\":\"step-00001842\",\"stageName\":\"\",\"stepName\":\"0-0-7\",\"stepLevel\":0,\"encodingRule\":\"00008085\",\"stepTag\":[],\"zrUserPzMethod\":\"0\",\"zrUser\":\"\",\"xzUserPzMethod\":\"0\",\"xzUser\":\"\",\"stepActOwner\":\"\",\"stepCollaborateOwner\":\"\",\"jrdb\":\"1\",\"yxyq\":\"0\",\"yxzb\":\"0\",\"yxzf\":\"0\",\"yxcxzx\":\"1\",\"yxsggy\":\"1\",\"dbzxazjdzs\":\"0\",\"jdcxzx\":\"0\",\"jdwxcxzx\":\"0\",\"notifyRuleFlag\":\"0\",\"startTimeFlag\":\"0\",\"endTimeFlag\":\"0\",\"notifyRule\":\"0\",\"parmSetFlag\":\"0\",\"stepRemark\":\"\",\"baseDateType\":\"0\",\"startTime\":\"00:00\",\"startBaseDay\":\"\",\"startDayType\":\"00\",\"startCrossDayType\":\"0\",\"startDay\":\"\",\"endTime\":\"23:59\",\"endBaseDay\":\"\",\"endDayType\":\"00\",\"endCrossDayType\":\"0\",\"endDay\":\"0\",\"isTodo\":\"0\",\"isNotCrtJob\":\"0\",\"allowManualConfirm\":\"1\",\"isAllowExecAgain\":\"0\",\"allowActionConfirm\":\"0\",\"allowShowDetail\":\"0\",\"allowFormAction\":\"0\",\"allowEditEndTime\":\"0\",\"paramsOutData\":[],\"warningMintues\":\"\",\"stepExecMode\":\"FREQUENCY\"},\"failRuleTableData\":{\"judgeScript\":\"\"},\"successRuleTableData\":{\"judgeScript\":\"\"},\"activeRuleTableData\":{\"judgeScript\":\"\"},\"timeoutRuleTableData\":{\"judgeScript\":\"\"},\"exceptionRemind\":[],\"finishRemind\":[],\"timeoutRemind\":[],\"serviceResponseId\":\"\",\"isRecordTimeoutError\":\"0\",\"warningRemind\":[]}}]}],\"version\":\"0\",\"stepCodeArr\":{\"step-00001842\":\"step-00001842\"}}",
          "caseDefBody": {"actions":[],"optionalStages":[],"stages":[{"defId":"","defName":"default","defType":"stage","optional":True,"edit":False,"defBody":{},"children":[{"stepName":taskname,"defType":"step","stepActType":"","stepId":"","edit":False,"stepFormInfo":{"caseStepDef":{"stepCode":stepcode,"stageName":"","stepName":taskname,"stepLevel":0,"encodingRule":"00008085","stepTag":[],"zrUserPzMethod":"0","zrUser":"","xzUserPzMethod":"0","xzUser":"","stepActOwner":"","stepCollaborateOwner":"","jrdb":"1","yxyq":"0","yxzb":"0","yxzf":"0","yxcxzx":"1","yxsggy":"1","dbzxazjdzs":"0","jdcxzx":"0","jdwxcxzx":"0","notifyRuleFlag":"0","startTimeFlag":"0","endTimeFlag":"0","notifyRule":"0","parmSetFlag":"0","stepRemark":"","baseDateType":"0","startTime":"00:00","startBaseDay":"","startDayType":"00","startCrossDayType":"0","startDay":"","endTime":"23:59","endBaseDay":"","endDayType":"00","endCrossDayType":"0","endDay":"0","isTodo":"0","isNotCrtJob":"0","allowManualConfirm":"1","isAllowExecAgain":"0","allowActionConfirm":"0","allowShowDetail":"0","allowFormAction":"0","allowEditEndTime":"0","paramsOutData":[],"warningMintues":"","stepExecMode":"FREQUENCY"},"failRuleTableData":{"judgeScript":""},"successRuleTableData":{"judgeScript":""},"activeRuleTableData":{"judgeScript":""},"timeoutRuleTableData":{"judgeScript":""},"exceptionRemind":[],"finishRemind":[],"timeoutRemind":[],"serviceResponseId":"","isRecordTimeoutError":"0","warningRemind":[]}}]}],"version":"0","stepCodeArr":{stepcode:stepcode}},
          "caseDefId": casedefid,
          "isCheckCode": False,
          "taskDeploys": []
}

    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:查询某个积木类型下所有的积木块,获取blockcode,blocktype')
def task_get_block(t,blocktype): #blocktype:'01'
    url=f"{HOST1}/api/agnes-ac/v2/block/query"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "blockType": blocktype
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    #blockcode = r.json()['data'][0]['blockCode']
    #blocktype = r.json()['data'][0]['blockType']

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

@allure.step('step:获取场景任务下所有的step(获取stepid)')
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
    #stepid=r.json()['data'][0]['stepCode']

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

@allure.step('step: 查询任务的casebody')
def task_get_casebody(t,casedefid):
    url=f"{HOST1}/api/agnes-ac/v1/ac/case/def/case-body?caseDefId={casedefid}"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    #casebody=r.json()['data']['caseDefBody']

@allure.step('step:查询主题任务,获取相关参数crtts,crtuser,updatets,updateuser,taskinitdays')
def task_query_theme_task(t,themeid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/query?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "themeId": themeid,
            "taskName": '',
            "disTypes": [],
            "taskStatusArr": []
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #actionparam=r.json()['data']['rows'][0]['reTaskDef']['actionParam']
    #biztag = r.json()['data']['rows'][0]['reTaskDef']['bizTag']
    #crtts= r.json()['data']['rows'][0]['reTaskDef']['crtTs']
    #crtuser = r.json()['data']['rows'][0]['reTaskDef']['crtUser']
    #updatets= r.json()['data']['rows'][0]['reTaskDef']['updateTs']
    #updateuser = r.json()['data']['rows'][0]['reTaskDef']['updateUser']
    #tasktitle= r.json()['data']['rows'][0]['reTaskDef']['taskTitle']
    #zruser= r.json()['data']['rows'][0]['reTaskDef']['zrUser']

@allure.step('step:发布任务-新增任务发布')
def task_publish(t,canfb,canht,cansc,canset,cansh,canty,canys,casedefid,caseid,casetype,crtts,crtuser,distype,funcid,taskid,taskname,taskinitdays,themeid,themename,updatets,updateuser,casebody):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/info/task/publish"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "reTaskDef": {
          "actionParam": "[{\"paramName\":\"bizStartDate\",\"paramNameFormat\":\"业务开始日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"bizEndDate\",\"paramNameFormat\":\"业务结束日期\",\"paramType\":\"日期\",\"bizObj\":\"\",\"paramValue\":\"startDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planStartDate\",\"paramNameFormat\":\"执行开始日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizStartDate\",\"paramShif\":0,\"paramDateType\":\"0\"},{\"paramName\":\"planEndDate\",\"paramNameFormat\":\"执行结束日期\",\"paramType\":\"日期\",\"bizObj\":\"任务对象\",\"paramValue\":\"bizEndDate\",\"paramShif\":0,\"paramDateType\":\"0\"}]",
          "addType": "regularAdd",
          "applyType": "",
          "bizTag": "",
          "canFb": canfb,
          "canHt": canht,
          "canSc": cansc,
          "canSet": canset,
          "canSh": cansh,
          "canTy": canty,
          "canYs": canys,
          "caseDefId": casedefid,
          "caseKey": caseid,
          "configDef": casetype,
          "crtTs": crtts,
          "crtUser": crtuser,
          "disType": distype,
          "eventId": "",
          "execMode": "1",
          "funcId": funcid,
          "isCanEdit": "1",
          "isDel": "0",
          "isInvolvedPrdt": "0",
          "jrdb": "1",
          "planEndTs": "23:59:59",
          "planStartTs": "00:00:00",
          "prdtRuleJson": "",
          "remindPlanId": "",
          "taskDesc": "",
          "taskId": taskid,
          "taskInitDays": taskinitdays,
          "taskLevel": "1",
          "taskName": taskname,
          "taskStatus": "02",
          "taskTitle": "{\"res\":\"${taskInformation.taskName}\",\"html\":\"<span key=\\\"taskInformation.taskName\\\" contenteditable=\\\"false\\\" class=\\\"tag\\\">任务信息.任务名称</span>\"}",
          "taskType": "common",
          "themeId": themeid,
          "themeName": themename,
          "updateTs": updatets,
          "updateUser": updateuser,
          "versionId": 0,
          "workdayAreaCode": "CN",
          "xzUser": "[]",
          "xzUserPzMethod": "1",
          "yxcxzx": "1",
          "yxsggy": "1",
          "yxyq": "1",
          "yxzb": "1",
          "yxzf": "1",
          "zrUser": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
          "zrUserPzMethod": "1"
        },
        "caseDefId": casedefid,
        #"caseDefBody": "{\"actions\":[],\"optionalStages\":[],\"stages\":[{\"defId\":\"\",\"defName\":\"default\",\"defType\":\"stage\",\"optional\":true,\"edit\":false,\"defBody\":{},\"children\":[{\"stepName\":\"单节点任务0-0-0\",\"defType\":\"step\",\"stepActType\":\"\",\"stepId\":\"\",\"edit\":false,\"stepFormInfo\":{\"caseStepDef\":{\"stepCode\":\"step-00001825\",\"stageName\":\"\",\"stepName\":\"单节点任务0-0-0\",\"stepLevel\":0,\"encodingRule\":\"00008085\",\"stepTag\":[],\"zrUserPzMethod\":\"0\",\"zrUser\":\"\",\"xzUserPzMethod\":\"0\",\"xzUser\":\"\",\"stepActOwner\":\"\",\"stepCollaborateOwner\":\"\",\"jrdb\":\"1\",\"yxyq\":\"0\",\"yxzb\":\"0\",\"yxzf\":\"0\",\"yxcxzx\":\"1\",\"yxsggy\":\"1\",\"dbzxazjdzs\":\"0\",\"jdcxzx\":\"0\",\"jdwxcxzx\":\"0\",\"notifyRuleFlag\":\"0\",\"startTimeFlag\":\"0\",\"endTimeFlag\":\"0\",\"notifyRule\":\"0\",\"parmSetFlag\":\"0\",\"stepRemark\":\"\",\"baseDateType\":\"0\",\"startTime\":\"00:00\",\"startBaseDay\":\"\",\"startDayType\":\"00\",\"startCrossDayType\":\"0\",\"startDay\":\"\",\"endTime\":\"23:59\",\"endBaseDay\":\"\",\"endDayType\":\"00\",\"endCrossDayType\":\"0\",\"endDay\":\"0\",\"isTodo\":\"0\",\"isNotCrtJob\":\"0\",\"allowManualConfirm\":\"1\",\"isAllowExecAgain\":\"0\",\"allowActionConfirm\":\"0\",\"allowShowDetail\":\"0\",\"allowFormAction\":\"0\",\"allowEditEndTime\":\"0\",\"paramsOutData\":[],\"warningMintues\":\"\",\"stepExecMode\":\"FREQUENCY\"},\"failRuleTableData\":{\"judgeScript\":\"\"},\"successRuleTableData\":{\"judgeScript\":\"\"},\"activeRuleTableData\":{\"judgeScript\":\"\"},\"timeoutRuleTableData\":{\"judgeScript\":\"\"},\"exceptionRemind\":[],\"finishRemind\":[],\"timeoutRemind\":[],\"serviceResponseId\":\"\",\"isRecordTimeoutError\":\"0\",\"warningRemind\":[]}}]}],\"version\":\"0\",\"stepCodeArr\":{\"step-00001787\":\"step-00001787\",\"step-00001788\":\"step-00001788\",\"step-00001789\":\"step-00001789\",\"step-00001810\":\"step-00001810\",\"step-00001811\":\"step-00001811\",\"step-00001825\":\"step-00001825\"}}"
        "caseDefBody": casebody
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


#任务中心-操作
@allure.step('step:置顶')
def task_topping(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/Topping"
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
def task_cancelTopping(t,taskid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/cancelTopping"
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

@allure.step('step:查询仅待办下特定名称的任务，获取相关参数')
def task_query_fortaskname(t,taskname):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers={
        'cookie':'token='+t
    }
    payload={
          "showType": "00",
          "authQueryParam2": "1",
          "taskName": taskname,
          "taskStatus": "",
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
    '''
    attuser = r.json()['data']['rows'][0]['attUser']
    biztimefrom = r.json()['data']['rows'][0]['bizTimeFrom']
    biztimeto = r.json()['data']['rows'][0]['bizTimeTo']
    caseid = r.json()['data']['rows'][0]['caseId']
    crtts = r.json()['data']['rows'][0]['crtTs']
    crtuser = r.json()['data']['rows'][0]['crtUser']
    distype = r.json()['data']['rows'][0]['disType']
    exetime = r.json()['data']['rows'][0]['exeTime']
    executeuser = r.json()['data']['rows'][0]['executeUser']
    ispending = r.json()['data']['rows'][0]['isPending']
    pkid = r.json()['data']['rows'][0]['pkId']
    prdtinfo = r.json()['data']['rows'][0]['prdtInfo']
    process = r.json()['data']['rows'][0]['process']
    taskexecauth = r.json()['data']['rows'][0]['taskExecAuth']
    taskid = r.json()['data']['rows'][0]['taskId']
    pkid = r.json()['data']['rows'][0]['pkId']
    tasklevel = r.json()['data']['rows'][0]['taskLevel']
    taskname = r.json()['data']['rows'][0]['taskName']
    taskstatus = r.json()['data']['rows'][0]['taskStatus']
    tasktag = r.json()['data']['rows'][0]['taskTag']
    tasktimefrom = r.json()['data']['rows'][0]['taskTimeFrom']
    tasktimeto = r.json()['data']['rows'][0]['taskTimeTo']
    tasktype = r.json()['data']['rows'][0]['taskType']
    updatets = r.json()['data']['rows'][0]['updateTs']
    '''

@allure.step('step:完成任务')
def task_submit(t,attuser,biztimefrom,biztimeto,caseid,crtts,crtuser,distype,exetime,executeuser,ispending,pkid,\
        prdtinfo,process,taskexecauth,taskid,tasklevel,taskname,taskstatus,tasktag,tasktimefrom,tasktimeto,tasktype,updatets):
    url=f"{HOST1}/api/agnes-ac/v1/ac/task/manage/submit-tasks"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "taskList": [
                {
                    "attUser": attuser,
                    "bizTimeFrom": biztimefrom,
                    "bizTimeTo": biztimeto,
                    "caseId": caseid,
                    "crtTs": crtts,
                    "crtUser": crtuser,
                    "disType": distype,
                    "exeTime": exetime,
                    "executeUser": executeuser,
                    "isPending": ispending,
                    "pkId": pkid,
                    "prdtInfo": prdtinfo,
                    "process": process,
                    "taskExecAuth": taskexecauth,
                    "taskId": taskid,
                    "taskLevel": tasklevel,
                    "taskName": taskname,
                    "taskStatus": taskstatus,
                    "taskTag": tasktag,
                    "taskTimeFrom": tasktimefrom,
                    "taskTimeTo": tasktimeto,
                    "taskType": tasktype,
                    "updateTs": updatets,
                    "remark": ""
                }
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: ?')
def task_approval_type(t,type): # 转办：'4',延期：'1',作废：'2'
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/isNeedApproval"
    headers={
        'cookie':'token='+t
    }
    payload={
        "type": type
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:获取人员')
def task_get_memberlist(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/listMemberByOrgIdList?pageIndex=0&pageSize=500"
    headers={
        'cookie':'token='+t
    }
    payload={
         "orgIdList": []
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    approvaluser=r.json()['data']['rows'][0]['userId']
    memberid=r.json()['data']['rows'][1]['userId']
    membername=r.json()['data']['rows'][1]['username']

@allure.step('step:转办')
def task_approval_approval(t,approvaluser,memberid,membername,taskname,caseid,taskid,pkid,tasktimefrom,tasktimeto):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/batch/add"
    taskfrom=tasktimefrom[:-3]
    taskto=tasktimeto[:-3]

    headers = {
        'cookie': 'token=' + t
    }
    payload=[{
        "applyUser": "agnes",
        "type": "4",
        "reason": "转办",
        "approvalUser": approvaluser,
        "applyData": {
            "userName": "",
            #"zrUserInfo": "[{\"refType\":\"1\",\"memberId\":\"yong.chen\",\"memberDesc\":\"陈永\"}]",
            "ZrUserInfo": [{"refType": "1", "memberId": memberid, "memberDesc": membername}],
            "planEndTs": "",
            "approver": approvaluser,
            "remark": "转办",
            "taskName": taskname,
            "taskTime": taskfrom+" 至 "+taskto,
            "caseIds": [
                caseid
            ],
            "taskId": taskid,
            "pkId": pkid,
            "userId": "agnes",
            "rows": []
        },
        "summary": f"任务标题 : {taskname}\n任务日期 : {taskfrom} 至 {taskto}\n转办人 :{membername}"
    }
    ]
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:延期')
def task_approval_delay(t,approvaluser,taskname,caseid,tasktimefrom,tasktimeto):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/batch/add"
    taskfrom = tasktimefrom[:-3]
    taskto = tasktimeto[:-3]

    headers = {
        'cookie': 'token=' + t
    }
    payload=[{
                "applyUser":  "agnes",
                "type": "1",
                "reason": "延期",
                "approvalUser": approvaluser,
                "applyData": {
                    "tasks": {
                        "caseId": caseid,
                        "userName": "",
                        "zrUserInfo": "",
                        "planEndTs": "2025-12-30 00:00:00",
                        "approver": approvaluser,
                        "remark": "延期",
                        "taskName": "",
                        "taskTime": ""
                    }
                },
                "summary": f"任务标题 : {taskname}\n任务日期 : {taskfrom} 至 {taskto}\n延期时间 : 2025-12-30 00:00:00\n"
    }
        ]
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:作废')
def task_cancel(t,attuser,biztimefrom,biztimeto,caseid,crtts,crtuser,distype,exetime,executeuser,ispending,pkid,\
        prdtinfo,process,taskexecauth,taskid,tasklevel,taskname,taskstatus,tasktag,tasktimefrom,tasktimeto,tasktype,updatets):
    url=f"{HOST1}/api/agnes-ac/v1/ac/task/manage/cancel"
    taskfrom = tasktimefrom[:-3]
    taskto = tasktimeto[:-3]
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userName": "",
            "zrUserInfo": "",
            "planEndTs": "",
            "approver": "",
            "remark": "作废",
            "taskName": taskname,
            "taskTime": taskfrom+" 至 "+taskto,
            "taskId": taskid,
            "pkId": pkid,
            "caseId": caseid,
            "rows": [
                {
                    "attUser": attuser,
                    "bizTimeFrom": biztimefrom,
                    "bizTimeTo": biztimeto,
                    "caseId": caseid,
                    "crtTs": crtts,
                    "crtUser": crtuser,
                    "disType": distype,
                    "exeTime": exetime,
                    "executeUser": executeuser,
                    "isPending": ispending,
                    "pkId": pkid,
                    "prdtInfo": prdtinfo,
                    "process": process,
                    "taskExecAuth": taskexecauth,
                    "taskId": taskid,
                    "taskLevel": tasklevel,
                    "taskName": taskname,
                    "taskStatus": taskstatus,
                    "taskTag": tasktag,
                    "taskTimeFrom": tasktimefrom,
                    "taskTimeTo": tasktimeto,
                    "taskType": tasktype,
                    "updateTs": updatets
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
          "taskName": "自动化临时任务"+str(random.randint(100000,999999)),
          "bizTag": "",
          "bizTagName": "",
          "crtType": "1",
          "zrUserInfo": "[{\"refType\":\"1\",\"memberId\":\"agnes\",\"memberDesc\":\"致宇小智\"}]",
          "planStartTs": str(datetime.date.today())+' 00:00:00',
          "planEndTs": str(datetime.date.today())+' 23:59:00',
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

#任务中心-查询
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

@allure.step('step:仅待办01/仅转交02/仅协作03')
def task_query_task(t,taskcls):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/queryForTask"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "basePath": "R0000001",
          "startDate": str(datetime.date.today()),
          "endDate": str(datetime.date.today()),
          "taskCls": taskcls,
          "showType": "00"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#审批管理
@allure.step('step:查询我的审批："1"/我的发起："2"')
def task_approval_list(t,pagetype):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/list?pageIndex=0&pageSize=100"

    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "applyUserList": "agnes",
          "statusList": "0",
          "pageType": pagetype
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
'''
    list=r.json()['data']['rows']
    for i in list:
        if i['id']=="4f5f15a952a05796fc266b044db37bdf":
            applydata=i['applyData']
            applydate=i['applyDate']
            applyusername = i['applyUsername']
            approvalusername = i['approvalUsername']
            isagency = i['isAgency']
            reason = i['reason']
            status = i['status']
            summary = i['summary']
            type = i['type']
            urgenum = i['urgeNum']
'''

@allure.step('step: 通过')
def task_approval_pass(t,applydata,applydate,applyusername,approvalusername,id,isagency,reason,status,summary,type,urgenum):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/pass"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "applyData": applydata,
            "applyDate": applydate,
            "applyUsername": applyusername,
            "approvalUsername": approvalusername,
            "id": id,
            "isAgency": isagency,
            "reason": reason,
            "status": status,
            "summary": summary,
            "type": type,
            "urgeNum": urgenum
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 拒绝')
def task_approval_refuse(t,applydata,applydate,applyusername,approvalusername,id,isagency,reason,status,summary,type,urgenum):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/refuse"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "applyData": applydata,
            "applyDate": applydate,
            "applyUsername": applyusername,
            "approvalUsername": approvalusername,
            "id": id,
            "isAgency": isagency,
            "reason": reason,
            "status": status,
            "summary": summary,
            "type": type,
            "urgeNum": urgenum
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 催办')
def task_approval_urge(t,applydata,applydate,applyusername,approvalusername,id,isagency,reason,status,summary,type,urgenum):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/urge"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "applyData": applydata,
            "applyDate": applydate,
            "applyUsername": applyusername,
            "approvalUsername": approvalusername,
            "id": id,
            "isAgency": isagency,
            "reason": reason,
            "status": status,
            "summary": summary,
            "type": type,
            "urgeNum": urgenum
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 查看交接详情')
def task_handover_get_doc(t,objectid):
    url=f"{HOST1}/api/ecm-server/v1/ecm/doc/get/order-by-name?docId={objectid}"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#任务明细查询
@allure.step('step:查询我的任务1/中心任务2/全部任务3')
def task_query_6(t,authqueryparam,taskname):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "authQueryParam1": authqueryparam,
            "collaborator": "",
            "attUser": "",
            "executeUser": "",
            "belongPost": "",
            "taskStatus": "",
            "prdtCode": "",
            "taskName": taskname,
            "taskLevel": "",
            "taskTimeFrom": str(datetime.date.today()),
            "taskTimeTo": str(datetime.date.today()),
            "bizTimeFrom": "",
            "bizTimeTo": "",
            "residueTime": "",
            "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 查看任务详情,获取stepstatus,stepcode,stepexecid,jobid')
def task_get_breif(t,taskexecid):
    url = f"{HOST1}/api/agnes-ac/v1/ac/exec/process/theme-brief"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "taskExecId": taskexecid,
            "bizDate": str(datetime.date.today())
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    '''
        stepcode = r.json()['data']["caseSteps"][0]['stepCode']
        stepexecid = r.json()['data']["caseSteps"][0]['stepExecId']
        jobid = r.json()['data']["caseSteps"][0]['jobId']
        stepstatus = r.json()['data']["caseSteps"][0]['stepStatus']
    '''

@allure.step('step: 任务详情-查看执行记录')
def task_get_breif_execlog(t,stepexecid):
    url = f"{HOST1}/api/agnes-ac/v2/block/get/block-exec-log/by-step-code?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
          "pageIndex": 0,
          "pageSize": 100,
          "stepExecId": stepexecid,
          "q": ""
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step: 任务详情-重新执行')
def task_get_breif_exec(t,caseid,stepcode,taskid):
    url = f"{HOST1}/api/agnes-ac/v1/ac/service/task/exec"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
          "caseId": caseid,
          "stepCode": stepcode,
          "taskId": taskid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step: 任务详情-手工完成-更新状态')
def task_get_breif_confirm_update(t,stepstatus,jobid,stepcode,caseid,stepexecid):
    url = f"{HOST1}/api/agnes-ac/v1/ac/ru/step/update/status"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "stepStatus": stepstatus,
            "jobId": jobid,
            "stepCode": stepcode,
            "caseId": caseid,
            "stepExecId": stepexecid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step: 任务详情-手工完成')
def task_get_breif_confirm(t,stepstatus,jobid,stepcode,caseid,stepexecid,taskid):
    url = f"{HOST1}/api/agnes-ac/v1/ac/task/manage/confirm"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "stepInfo": {
                "stepStatus": stepstatus,
                "jobId": jobid,
                "stepCode": stepcode,
                "bizDate": str(datetime.date.today()),
                "execBizDate": str(datetime.date.today()),
                "caseId": caseid,
                "stepExecId": stepexecid
            },
            "inst": {
                "taskId": taskid
            },
            "paramListStr": "",
            "caseId": caseid,
            "stepExecId": stepexecid,
            "taskId": taskid
    }
    {
        "stepInfo": {
            "stepStatus": "06",
            "jobId": "",
            "stepCode": "step-00001712",
            "caseId": "20241125-0000000000268888",
            "stepExecId": "1j7hnevnsy17c"
        },
        "inst": {
            "taskId": "1j7hnew84mahk"
        },
        "paramListStr": "",
        "caseId": "20241125-0000000000268888",
        "stepExecId": "1j7hnevnsy17c",
        "taskId": "1j7hnew84mahk"
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step: 任务详情-查看明细')
def task_get_breif_carry_page(t,stepexecid):
    url = f"{HOST1}/api/agnes-app/v1/dc/file/deal/list/compare/carry-page"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "stepExecId": stepexecid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step: 任务详情-修改结束时间')
def task_get_breif_edit_planendtime(t,stepexecid):
    url = f"{HOST1}/api/agnes-ac/v1/ac/exec/process/edit/plan-end-time"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "stepExecId": stepexecid,
            "planEndTime":  str(datetime.date.today())+"23:59:00"
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step: 任务详情-作废')
def task_get_breif_step_cancel(t,stepexecid,taskid):
    url = f"{HOST1}/api/agnes-ac/v1/config/exe/task/step/cancel"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "stepExecId": stepexecid,
            "taskId": taskid
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

if __name__=='__main__':
    t=''
