
from config import HOST1
import allure
import requests
import random,time,datetime

#任务通知方案
@allure.step('step:新增通知方案-产品任务：1，岗位任务：2')
def task_notify_save(t,tasktype):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notify/save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "userGroupId": "",
          "planName": "自动化通知方案"+str(random.randint(100000,999999)),
          "taskType": tasktype,
          "jobBlon": "",
          "isDefault": '0',
          "userGroupName": "",
          "remark": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询通知方案，获取configid')
def task_get_notify(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notify/get"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #configid=r.json()['data'][0]['configId']

@allure.step('step:查询通知对象，获取fnid(notifyrule)')
def task_notify_get_config_fun(t):
    url=f"{HOST1}/api/agnes-ac/v1/config/fun/query/fun-by-apply-scence?applyScence=06"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #notifyrule=r.json()['data'][0]['fnId']

@allure.step('step:新增通知规则')
def task_notifyrule_save(t,configid,notifyrule):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notifyRule/save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "configId": configid,
            "notifyRule": notifyrule,
            "standard": "2",
            "conditionT": "2",
            "offsetT": "0",
            "unit": "1",
            "remark": "",
            "editable": True,
            "taskConfig": [
                {
                    "dictId": "1",
                    "dictName": "提前"
                },
                {
                    "dictId": "2",
                    "dictName": "延后"
                }
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:获取用户列表userid、username')
def task_notify_get_userlist(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/page/user/list?pageIndex=0&pageSize=500"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pageIndex": 0,
            "pageSize": 500
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #username=r.json()['data']['rows'][0]['userName']
    #userid = r.json()['data']['rows'][0]['userId']

@allure.step('step:查询通知规则,获取通知规则的pkid')
def task_get_notifyrule(t,configid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notifyRule/get"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "configId": configid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #pkid=r.json()['data'][0]['pkId']

@allure.step('step:新增通知方式-邮件')
def task_notifyrule_saveemail(t,pkid,userid,username):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notifyRule/saveEmailInfo"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pkId": pkid,
            "notifyContent": {
                "remindProp": [
                    {
                        "remindUser": [{"refType": "1", "memberId": userid, "memberDesc": username}],
                        "remindCc": "",
                        "remindBcc": "",
                        "remindTitle": {
                            "html": "<span key=\"taskInformation.taskName\" contenteditable=\"false\" class=\"tag\">任务信息.任务名称</span>",
                            "res": "${taskInformation.taskName}"
                        },
                        "remindContent": {
                            "html": "<p><span style=\"color: rgb(51, 135, 243);\"><span class=\"tag-blot\" data-code=\"taskInformation.taskName\" data-name=\"任务信息.任务名称\">﻿<span contenteditable=\"false\">${任务信息.任务名称}</span>﻿</span></span></p>",
                            "res": "<p><span style=\"color: rgb(51, 135, 243);\"><span>#{taskInformation.taskName}</span></span></p>"
                        },
                        "remindMode": "2",
                        "isSendAttach": "",
                        "sendAttachFile": "0",
                        "sendDataList": "0",
                        "remindUserList": [
                            {
                                "refType": "1",
                                "memberId": userid,
                                "memberDesc": username
                            }
                        ],
                        "remindCcList": [],
                        "remindBccList": [],
                        "fillFlag": True
                    }
                ]
            }
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:删除通知规则')
def task_notifyrule_delete(t,pkid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notifyRule/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pkId": pkid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:删除通知方案（pkid是通知方案的configid）')
def task_notify_delete(t,pkid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/notify/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pkId": pkid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#任务中心定义
@allure.step('step:新增一级分组（任务实例00）')
def task_theme_todo_save(t,type):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "parentThemeName": "",
          "themeName": "自动化一级分组"+str(random.randint(100000,999999)),
          "type":  type,   #分组类型：第一个："00",
          "status": "00",
          "taskDefTheme": "",
          "linkPageName": "",
          "linkPageId": "",
          "ownerGroup": "[]",
          "bizType": "",
          "operateType": "01",
          "summaryMethod": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询分组列表，获取分组的basepath,themepkid,themepkname')
def task_theme_todo_gettree(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/getTreeNew"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #themepkid=r.json()['data'][-1]['pkId']
    #themepkname=r.json()['data'][-1]['themeName']
    #basepath=r.json()['data'][-1]['basePath']
    #parentthemeid = r.json()['data'][-1]['parentThemeId']

@allure.step('step:查询任务主题列表,获取themeid')
def task_theme_todo_getthemeinfo(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/getThemeInfo"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "taskDefTheme": None
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #themeid=r.json()['data'][-1]['themeId']

@allure.step('step:查询任务列表,通过特定任务主题，获取关联任务的taskidlist')
def task_theme_todo_querytasklistforsave(t,themeid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/queryTaskListForSave"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "themeIdList": [
                themeid
            ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

    '''data=r.json()['data']
    taskidlist=[]
    for i in data:
        taskidlist.append(i['taskDefId'])'''

@allure.step('step:关联任务')
def task_theme_todo_savetasklink(t,themepkid,themepkname,themeid,taskidlist):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/saveTaskLink"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "themeId": themepkid,
          "themeName": themepkname,
          "themeIdList": [
              themeid
          ],
          "taskDefIdList": taskidlist,
          "preBizName": "",
          "bizName": "",
          "nodeName": "",
          "bizThemeName": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询关联任务列表,获取关联任务的pkidlist')
def task_theme_todo_querytasklist(t,themepkid,basepath):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/queryTaskLink"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pkId": themepkid,
            "taskDefTheme": "",
            "basePath": basepath,
            "q": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #list=r.json()['data']
    #pkidlist=[]
    #for i in list:
        #pkidlist.append(i['pkId'])

@allure.step('step:删除关联任务')
def task_theme_todo_deletetasklink(t,pkidlist):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/deleteTaskLink"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pkIdList": pkidlist
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:上移"01"/下移"02" 分组')
def task_theme_todo_movestep(t,themepkid,parentthemeid,movetype):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/moveOneStep"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pkId": themepkid,
          "parentThemeId": parentthemeid,
          "moveType": movetype
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:删除分组')
def task_theme_todo_delete(t,themepkid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/theme/todo/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "pkId": themepkid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#任务分配方案
@allure.step('step: 查询产品任务("1")的任务配置列表,获取tasklist')
def task_post_config_list(t,isproducttask):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/post/config/list-all"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "isProductTask": isproducttask,
            "status": "1"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #tasklist=r.json()['data']

@allure.step('step: 查询通知对象，获取fnid(customrule)')
def task_post_get_config_fun(t):
    url=f"{HOST1}/api/agnes-ac/v1/config/fun/query/fun-by-apply-scence?applyScence=05"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #customrule=r.json()['data'][0]['fnId']

@allure.step('step:新增任务分配方案:产品任务-"1"，岗位任务-"2"')
def task_info_save(t,tasktype,customrule,tasklist):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/info/save"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "planName": "自动化任务分配方案"+str(random.randint(100000,999999)),
            "taskType": tasktype,
            "personType": "0",
            "isDefault": "0",
            "editable": True,
            "taskConfig": {
                "jobRule": "",
                "schedualRule": "",
                "allocRule": "",
                "customRule": customrule,
                "taskList": tasklist,
                "scheduaList": [],
                "visibleDropdowns": {
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": True
                }
            }
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 查询任务分配方案列表，获取方案的pkid')
def task_info_get(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/info/get"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #pkid=r.json()['data'][0]['pkId']

@allure.step('step:删除分配方案')
def task_info_delete(t,pkid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/info/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pkId": pkid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

if __name__=='__main__':
    print()