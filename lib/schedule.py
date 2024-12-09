import allure
import requests
from datetime import datetime,timedelta
import datetime
from common.read_yml import get_current_time,read_yml
from config import HOST1

#排班管理方案
@allure.step('step:查询org列表')
def shedule_get_orglist(t,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/listAllOrgByUserId"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "userId":userid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

    '''orglist=[]
    data=r.json()['data']
    for i in data:
        orglist.append(i['orgId'])'''

@allure.step('step:查询org列表')
def shedule_get_orgidlist(t,orglist):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/selectParentOrgByType"
    headers = {
        'cookie': 'token=' + t
    }
    payload=orglist
    r=requests.post(url=url,headers=headers,json=payload)
    return r

    '''orgidlist=[]
       data=r.json()['data']
       for i in data:
           orgidlist.append(i['id'])'''

@allure.step('step:查询org列表-获取岗位列表')
def shedule_get_org_post(t,orgidlist):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/post/config/center/post/get"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "orgIdList": orgidlist,
            "status": "1"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
'''
    list=r.json()['data']['rows']
    for i in list:
        if i['postName']=='':
            usergroupid=i['userGroupId']
'''

@allure.step('step:查询岗位数据,获取岗位可选人员')
def shedule_get_org_group(t,usergroupid):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/query?pageSize=1000"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userGroupId": usergroupid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #grouplist1=r.json()['data']['rows']
    #grouplist2 = grouplist1.append({"userId": "ROTATE","userName": "轮值"})
    #person1=r.json()['data']['rows'][0]['userId']
    #person2 = r.json()['data']['rows'][1]['userId']

@allure.step('step:新增/复制排班方案')
def shedule_add(t,startdate,enddate,usergroupid,grouplist,person1,person2,schedule):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "id": "",
          "planName": "自动化排班方案05",
          "cycleDays": "",
          "startDate": startdate,
          "endDate": enddate,
          "detailList": [
            {
              "disabled": True,
              "postId": usergroupid,
              "perList": [{"userId": "ROTATE","userName": "轮值"}]+grouplist,
              "smallPerList": grouplist,
              "workDay": "1",
                "columns": [
                    {
                        "value": "user",
                        "name": "人员"
                    },
                    {
                        "value": "user",
                        "name": "人员"
                    }
                ],
                "cycleInfoRes": [
                    {
                        "person": [
                            1,
                            1
                        ],
                        "schedule": ""
                    },
                    {
                        "person": [],
                        "schedule": ""
                    },
                    {
                        "person": [
                            [
                                person1
                            ],
                            [
                                person2
                            ]
                        ],
                        "schedule": schedule  #"ZB"
                    }
                ],
                "childColumns": [],
                "childCycleInfoRes": [
                    {
                        "person": [],
                        "schedule": ""
                    },
                    {
                        "person": [],
                        "schedule": ""
                    }
                ]
            }
          ],
          "flag": "1"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:新增后，查询排班列表,获取排班相关参数')
def shedule_get_list(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/list?pageIndex=0&pageSize=100&planName="
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "planName": "",
          "orgIdList": None,
          "postId": None,
          "status": None
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    '''
    id=r.json()['data']['rows'][0]['id']
    enddate = r.json()['data']['rows'][0]['endDate']
    flag= r.json()['data']['rows'][0]['flag']
    planname= r.json()['data']['rows'][0]['planName']
    planstatus= r.json()['data']['rows'][0]['planStatus']
    postname= r.json()['data']['rows'][0]['postName']
    startdate = r.json()['data']['rows'][0]['startDate']
    status = r.json()['data']['rows'][0]['status']
    updatets = r.json()['data']['rows'][0]['updateTs']
    updateuser = r.json()['data']['rows'][0]['updateUser']
    workday = r.json()['data']['rows'][0]['workday']
'''

@allure.step('step:编辑排班方案')
def shedule_edit(t,usergroupid,grouplist,person1,person2,schedule,enddate,flag,id,planname,startdate,status,updatets,updateuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/edit"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "detailList": [
                {
                    "postId": usergroupid,
                    "workDay": "1",
                    "columns": [
                        {
                            "name": "人员",
                            "value": "user"
                        },
                        {
                            "name": "人员",
                            "value": "user"
                        }
                    ],
                    "childColumns": [],
                    "cycleInfoRes": [
                        {
                            "person": [
                                1,
                                1
                            ]
                        },
                        {
                            "person": [
                                "a",
                                "b"
                            ]
                        },
                        {
                            "schedule": schedule,  # "ZB",
                            "person": [
                                [
                                    person1
                                ],
                                [
                                    person2
                                ]
                            ]
                        }
                    ],
                    "childCycleInfoRes": [
                        {
                            "person": [],
                            "schedule": ""
                        },
                        {
                            "person": [],
                            "schedule": ""
                        }
                    ],
                    "smallPerList": grouplist,
                    "perList": [{"userId": "ROTATE","userName": "轮值"}]+grouplist,
                }
            ],
            "id": id,
            "planName": planname,
            "startDate": startdate,
            "endDate": enddate,
            "status": status,
            "updateTs": updatets,
            "updateUser": updateuser,
            "flag": flag
    }

    r=requests.put(url=url,json=payload,headers=headers)
    return r

@allure.step('step:编辑后，查询排班列表,获取排班相关参数')
def shedule_get_list(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/list?pageIndex=0&pageSize=100&planName="
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "planName": "",
          "orgIdList": None,
          "postId": None,
          "status": None
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    '''
    id=r.json()['data']['rows'][0]['id']
    enddate = r.json()['data']['rows'][0]['endDate']
    flag= r.json()['data']['rows'][0]['flag']
    planname= r.json()['data']['rows'][0]['planName']
    planstatus= r.json()['data']['rows'][0]['planStatus']
    postname= r.json()['data']['rows'][0]['postName']
    startdate = r.json()['data']['rows'][0]['startDate']
    status = r.json()['data']['rows'][0]['status']
    updatets = r.json()['data']['rows'][0]['updateTs']
    updateuser = r.json()['data']['rows'][0]['updateUser']
    workday = r.json()['data']['rows'][0]['workday']
'''

@allure.step('step:预览排班方案')
def shedule_preview(t,enddate,flag,id,planname,planstatus,postname,startdate,status,updatets,updateuser,workday):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/preview"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "endDate": enddate,
          "flag": flag,
          "id": id,
          "planName": planname,
          "planStatus": planstatus,
          "postName": postname,
          "startDate": startdate,
          "status": status,
          "updateTs": updatets,
          "updateUser": updateuser,
          "workday": workday
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:审核排班方案')
def shedule_audit(t,usergroupid,grouplist,person1,person2,schedule,enddate,flag,id,planname,startdate,status,updatets,updateuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/audit"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "detailList": [
                {
                    "postId": usergroupid,
                    "workDay": "1",
                    "columns": [
                        {
                            "name": "人员",
                            "value": "user"
                        },
                        {
                            "name": "人员",
                            "value": "user"
                        }
                    ],
                    "childColumns": [],
                    "cycleInfoRes": [
                        {
                            "person": [
                                1,
                                1
                            ]
                        },
                        {
                            "person": [
                                "a",
                                "b"
                            ]
                        },
                        {
                            "schedule": schedule,  #"ZB",
                            "person": [
                                [
                                    person1
                                ],
                                [
                                    person2
                                ]
                            ]
                        }
                    ],
                    "childCycleInfoRes": [
                        {
                            "person": [],
                            "schedule": ""
                        },
                        {
                            "person": [],
                            "schedule": ""
                        }
                    ],
                    "smallPerList": grouplist,
                    "perList": [{"userId": "ROTATE","userName": "轮值"}]+grouplist,
                }
            ],
            "id": id,
            "planName": planname,
            "startDate": startdate,
            "endDate": enddate,
            "status": status,
            "updateTs": updatets,
            "updateUser": updateuser,
            "flag": flag
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

@allure.step('step:审核之后，再次查询排班列表,获取排班最新的相关参数')
def shedule_get_list(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/list?pageIndex=0&pageSize=100&planName="
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "planName": "",
          "orgIdList": None,
          "postId": None,
          "status": None
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r
    '''
    id=r.json()['data']['rows'][0]['id']
    enddate = r.json()['data']['rows'][0]['endDate']
    flag= r.json()['data']['rows'][0]['flag']
    planname= r.json()['data']['rows'][0]['planName']
    planstatus= r.json()['data']['rows'][0]['planStatus']
    postname= r.json()['data']['rows'][0]['postName']
    startdate = r.json()['data']['rows'][0]['startDate']
    status = r.json()['data']['rows'][0]['status']
    updatets = r.json()['data']['rows'][0]['updateTs']
    updateuser = r.json()['data']['rows'][0]['updateUser']
    workday = r.json()['data']['rows'][0]['workday']
'''

@allure.step('step:删除排班方案')
def shedule_delete(t,enddate,flag,id,planname,planstatus,postname,startdate,status,updatets,updateuser,workday):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "endDate": enddate,
            "flag": flag,
            "id": id,
            "planName": planname,
            "planStatus": planstatus,
            "postName": postname,
            "startDate": startdate,
            "status": status,
            "updateTs": updatets,
            "updateUser": updateuser,
            "workday": workday
    }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

#排班日历: 组织-岗位-排班-调班
@allure.step('step:查询当日排班日历')
def memo_listmonth(t):
    url=f"{HOST1}/api/agnes-app/v2/dop/memo/listMonthDetail"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "postId": "",
          "rosterType": "",
          "rosterNoticeUser": "",
          "rosterDate": str(datetime.date.today())
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:获取默认调班审批人')
def memo_getauditor(t,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/getAuditor"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
         "userId": userid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #auditor_userid=r.json()['data']['userId']

@allure.step('step:获取调班可选审批人')
def memo_getauditor_all(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/tree/structure/get/user/info"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #auditor_userid=r.json()['data'][0]['userId']

@allure.step('step:获取换出日期可选岗位')
def memo_get_roster_postlist(t,roster_userid,rosterdate1):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/getRosterPostList"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "rosterNoticeUser": roster_userid,
            "rosterDate": rosterdate1
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #postlist=r.json()['data']
    #postid=r.json()['data'][0]['userGroupId']
    #postname = r.json()['data'][0]['userGroupName']

@allure.step('step:获取全部班次')
def memo_get_roster_typelist(t,rosteruserid,rosterdate1,postid):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/getRosterTypeList"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "rosterNoticeUser": rosteruserid,
          "rosterDate": rosterdate1,
          "postId": postid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #rostertypelist=r.json()['data']
    #rostertype=r.json()['data'][0]['dictId']
    #rostertypename=r.json()['data'][0]['dictName']

@allure.step('step:获取换回日期班次人员')
def memo_get_roster_userlist(t,rostertype,rosterenddate,postid):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/getRosterUserList"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "rosterDate": rosterenddate,
          "rosterType": rostertype,
          "postId": postid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #personlist=r.json()['data']
    #targetuserid=r.json()['data'][0]['rosterNoticeUser']
    #targetusername=r.json()['data'][0]['userName']

@allure.step('step:临时调班')
def memo_checklist(t,sourcedate,targetdate,postid,rostertype,targetuserid,postlist,personlist,rostertypelist,sourceuserid,audit_userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/schedule-plan/checkList"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
                "sourceDate": sourcedate,
                "pickerOptions": {},
                "endPickerOptions": {},
                "targetDate": targetdate,
                "postId": postid,
                "rosterType": rostertype,  #早班："ZB"
                "targetUser": targetuserid,
                "rosterTypeDisabled": False,
                "postList": postlist,
                "personList": personlist,
                "rosterTypeDict": rostertypelist,
                "sourceUser": sourceuserid,
                "auditUser": audit_userid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: ')
def memo_get_roster_isneedapproval(t):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/isNeedApproval"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "type": 5
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:调班完成')
def memo_add(t,sourcedate, targetdate, postid, rostertype, targetuserid, postlist, personlist, rostertypelist,
                   sourceuserid, audit_userid,postname,rostertypename,targetusername):
    url = f"{HOST1}/api/agnes-app/v1/mcc/approval/batch/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload = {
            "applyData": [
              {
                "sourceDate": sourcedate,
                "pickerOptions": {},
                "endPickerOptions": {},
                "targetDate": targetdate,
                "postId": postid,
                "rosterType": rostertype,
                "targetUser": targetuserid,
                "rosterTypeDisabled": False,
                "postList": postlist,
                "personList": personlist,
                "rosterTypeDict": rostertypelist,
                "sourceUser": sourceuserid,
                "auditUser": audit_userid
              }
            ],
            "type": "5",
            "applyUser": sourceuserid,
            "approvalUser": audit_userid,
            "summary": "岗位: "+postname+", 班次: "+rostertypename+"\n申请人: 覃云, 调出日期: "+sourcedate+"\n对调人: "+targetusername+", 调入日期: "+targetdate
            }
    r = requests.post(url=url, headers=headers, json=payload)
    return r

if __name__=='__main__':
   print()