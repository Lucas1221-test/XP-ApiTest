
from config import HOST1
import allure
import requests
import random,time
from datetime import datetime,timedelta
import datetime
from lib.login import login
from common.read_yml import get_current_time,read_yml

#组织管理
@allure.step('step:新增组织')
def org_framework_add(t,orgtype):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "id": "",
            "parentId": None,
            "orgName": "自动化一级测试部门",
            "orgType": orgtype,
            "status": "1",
            "publicEmail": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询组织列表，获取必要字段值:id,orgname,orgtype,parentnodecode,treename,treenames,treenode,treenodes')
def org_framework_list(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/list"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
'''
    orglist = r1.json()['data']['rows']
    for item in orglist:
        try:
            if item['orgName'] == '自动化一级测试部门':
                id = item['id']
                orgname = ['orgName']
                orgtype = item['orgType']
                status=item['status']
                publicemail=item['publicEmail']
                onjobquantity=item['onJobQuantity']
                parentnodecode = item['parentNodeCode']
                treename = item['treeName']
                treenames = item['treeNames']
                treenode = item['treeNode']
                treenodes = item['treeNodes']
                updatets=item['updateTs']
                updateuser=item['updateUser']
        except IndexError:
            print('没有查询到组织')
'''

@allure.step('step:编辑组织')
def org_framework_edit(t,id,orgname,orgtype, status,publicemail,onjobquantity,parentnodecode, treename, treenames, treenode, treenodes, updatets,updateuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/edit"
    headers = {
        'cookie': 'token=' + t
    }
    data={
          "id": id,
          "parentId": None,
          "orgName": orgname,
          "orgType": orgtype,
          "status": status,
          "publicEmail": publicemail,
          "onJobQuantity": onjobquantity,
          "parentNodeCode": parentnodecode,
          "treeName": treename,
          "treeNames": treenames,
          "treeNode": treenode,
          "treeNodes": treenodes,
          "updateTs": updatets,
          "updateUser": updateuser
    }
    r=requests.put(url=url,json=data,headers=headers)
    return r

@allure.step('step:删除组织')
def org_framework_delete(t,id,orgname,orgtype,status,publicemail,onjobquantity,parentnodecode,treename,treenames,treenode,treenodes,updatets,updateuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "id": id,
          "onJobQuantity": onjobquantity,
          "orgName": orgname,
          "orgType": orgtype,
          "parentNodeCode": parentnodecode,
          "publicEmail": publicemail,
          "status": status,
          "treeName": treename,
          "treeNames": treenames,
          "treeNode": treenode,
          "treeNodes": treenodes,
          "updateTs": updatets,
          "updateUser": updateuser
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#组织架构-用户设置
@allure.step('step:获取可选用户列表')
def org_framework_get_userinfo(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/tree/structure/get/user/info"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    userlist=r.json()['data']
    for i in userlist:
        if i['userName']=='bailuo':
            userid = i['userId']
            username = i['userName']
'''

@allure.step('step:组织下新增用户(当前用户所在组织：徐汇业务组"1j2z501o4e4k3"),role:"0"-成员，"1"-负责人')
def org_framework_member_add(t,orgid,userid,role):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/addMember"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "id": "",
          "orgId": orgid,
          "userId": userid,
          "role": role, #成员："0",负责人："1"
          "status": "1",
          "startDate": str(datetime.date.today()),
          "endDate": "9998-12-31"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询当前组织下用户列表')
def org_framework_member_list(t,orgid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/listMemberByOrgId?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "orgId": orgid,
          "selectAll": "0"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    data=r.json()['data']['rows']
    for i in data:
        if i['userId']==userid:
            id=i['id']
            orgid=i['orgId']
            orgname=i['orgName']
            userid=i['userId']
            username=i['username']
            role=i['role']
            status=i['status']
            updatets=i['updateTs']
            updateuser = i['updateUser']
            userstatus=i['userStatus']
            startdate=i['startDate']
            enddate=i['endDate']
            '''

@allure.step('step:组织下编辑用户(当前用户所在组织：徐汇业务组"1j2z501o4e4k3"),role:"0"-成员，"1"-负责人')
def org_framework_member_edit(t,id,orgid,orgname,userid,username,role,status,startdate,enddate,updatets,updateuser,userstatus):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/editMember"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "id": id,
            "orgId": orgid,
            "userId": userid,
            "role": role,
            "status": status,
            "startDate": startdate,
            "endDate": enddate,
            "orgName": orgname,
            "updateTs": updatets,
            "updateUser": updateuser,
            "userStatus": userstatus,
            "username": username
    }
    r=requests.put(url=url,json=payload,headers=headers)
    return r

@allure.step('step:组织下删除用户(当前用户所在组织：徐汇业务组"1j2z501o4e4k3"),role:"0"-成员，"1"-负责人')
def org_framework_member_delete(t,id,orgid,orgname,role,startdate,enddate,status,updatets,updateuser,userid,username,userstatus):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/deleteMember"
    headers = {
        'cookie': 'token=' + t
    }
    payload=[
        {
                "endDate": enddate,
                "id": id,
                "orgId": orgid,
                "orgName": orgname,
                "role": role,
                "startDate": startdate,
                "status": status,
                "updateTs": updatets,
                "updateUser": updateuser,
                "userId": userid,
                "userStatus": userstatus,
                "username": username
    }
    ]
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#岗位设置-岗位设置
@allure.step('step:查询org列表,获取orgid')
def group_getorgtree(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/getOrgTree"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
'''
    orglist = r.json()['data']
    for i in orglist:
        if i['orgName'] == '测试一级部门勿删':
            orgid = i['id']
'''

@allure.step('step:查询org的用户列表,获取directorid')
def group_getorg_member(t,orgid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/listMemberByOrgId?pageSize=5"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "orgId": orgid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #memberlist=r.json()['data']['rows']

@allure.step('step:新增岗位')
def group_config_add(t,grouptag,orgid,isproducttask,ismusthanddown,director,status):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/post/config/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userGroupId": "",
            "userGroupName": '自动化测试岗位',
            "userGroupTag": grouptag, #岗位标签第一个："01"
            "orgId": orgid,
            "isProductTask": isproducttask, #是否是产品任务：否"0",是"1"
            "isMustHandDown": ismusthanddown, #是否必须交接：是"1",否"0"
            "director": director, #负责人id
            "status": status #状态：正常"1"，停用"0"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询岗位列表，获取岗位必要字段：groupid,groupname,grouptag,orgid,orgname')
def group_config_list(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/post/config/list?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "pageIndex": 0,
            "pageSize": 100
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
'''
    grouplist = r.json()['data']['rows']
    for item in grouplist:
        try:
            if item['usergroupname'] == '自动化测试岗位':
                groupid = item['userGroupId']
                groupname = item['userGroupName']
                grouptag = item['userGroupTag']
                orgid = item['orgId']
                orgname = item['orgName']
                isproducttask=item['isProductTask']
                ismusthanddown=item['isMustHandDown']
                director=item['director']
                crtts=item['crtTs']
                crtuser=item['crtUser']

        except IndexError:
            print('没有查询到岗位')
'''

@allure.step('step:编辑岗位')
def group_config_edit(t,groupid,groupname,grouptag,orgid,orgname,isproducttask,ismusthanddown,director,crtts,crtuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/post/config/edit"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userGroupId": groupid,
            "userGroupName": groupname,
            "userGroupTag": grouptag,
            "orgId": orgid,
            "isProductTask": isproducttask,
            "isMustHandDown": ismusthanddown,
            "director": director,
            "status": "1",
            "crtTs": crtts,
            "crtUser": crtuser,
            "orgName": orgname
    }
    r=requests.put(url=url,json=payload,headers=headers)
    return r

@allure.step('step:删除岗位')
def group_delete(t,crtts,crtuser,director,ismusthanddown,isproducttask,groupid,groupname,grouptag,orgid,orgname):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "crtTs": crtts,
            "crtUser": crtuser,
            "director": director,
            "isMustHandDown": ismusthanddown,
            "isProductTask": isproducttask,
            "orgId": orgid,
            "orgName": orgname,
            "userGroupId": groupid,
            "userGroupName": groupname,
            "userGroupTag": grouptag
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#岗位设置-用户管理

@allure.step('step:查询某个org下，可选的用户：userid,username')
def group_ref_get_org(t,orgid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/get/center/user/by/org"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "orgId": orgid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:添加用户（主岗）')
def group_save_ref(t,groupid,userid,ismain):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/save/ref"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "id": "",
          "userGroupId": groupid,
          "userId": userid,
          "userIds": [
            userid
          ],
          "isMain": ismain, #是否是主岗：是"1"
          "startDate": str(datetime.date.today()),
          "endDate": "9998-12-31"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询用户列表')
def group_ref_get_user_query(t,groupid):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/query?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "selectAll": "0",
          "userGroupId": groupid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

'''
    userlist = r.json()['data']['rows']
    for item in userlist:
        try:
            if item['userid'] == userid:
                crtts=item['crtTs']
                startdate=item['startDate']
                enddate=item['endDate']
                ismain=item['isMain']
                orgname=item['orgName']
                groupname = item['userGroupName']
                grouprefid = item['userGroupRefId']
                sequencenum = item['sequenceNum']
                username=item['userName']
                userid = item['userId']
                userstatus=item['userStatus']
        except IndexError:
            print('没有查询到用户')

'''

@allure.step('step:编辑用户（主岗）')
def group_edit_ref(t,groupid,userid,ismain,startdate,enddate,crtts,orgname,orgid,groupname,grouprefid,username,sequencenum,userstatus):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/edit/ref"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "id": "",
          "userGroupId": groupid,
          "userId": userid,
          "userIds": [],
          "isMain": ismain,
          "startDate": startdate,
          "endDate": enddate,
          "crtTs": crtts,
          "orgName": orgname,
          "sequenceNum": sequencenum,
          "userGroupName": groupname,
          "userGroupRefId": grouprefid,
          "userName": username,
          "userStatus": userstatus,
          "orgId": orgid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:删除用户')
def group_delete_ref(t,userid,usergroupid,usergrouprefid):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/delete/ref"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userGroupRefId": usergrouprefid,
            "userId": userid,
            "userGroupId": usergroupid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

#产品分工表
@allure.step('step:查询可选的产品列表,获取产品的prdtcode')
def prdt_prdtselect(t):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/prdtSelect"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #prdtcode=r.json()['data'][0]['productCode']

@allure.step('step:查询可选的人员,获取主岗和备岗人员userid')
def prdt_productuser(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/getProductUser"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #zhugangren=r.json()['data'][0]['userId']
    #beigangone=r.json()['data'][1]['userId']

@allure.step('step:新增产品分工')
def prdt_divide_add(t,prdtcode,zhugangren,beigangone):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "startDate": str(datetime.date.today()),
          "endDate": "9998-12-31",
          "prdtCode": prdtcode,
          "zhugangren": zhugangren,
          "beigangone": beigangone,
          "beigangtwo": "",
          "beigangthr": "",
          "id": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询产品分工列表-获取必要字段值：prdtcode,prdtname,selectobjid,zhugangren,beigangone')
def prdt_divide_query(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/queryPage?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "allParam": False,
            "productName": [],
            "zhugangren": [],
            "beigangren": [],
            "divideWork": [],
            "productStatus": [],
            "productType": [],
            "custodianBank": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
'''
    prdtlist = r.json()['data']['rows']
    for i in prdtlist:
        if i['productName'] == '测试产品勿删':
            selectobjid = i['id']
            prdtcode = i['productCode']
            prdtname = i['productName']
            startdate=i['startDate']
            enddate=i['endDate']
'''
@allure.step('step:编辑产品分工')
def prdt_divide_update(t,prdtcode,startdate,enddate,prdtname,selectobjid,zhugangren,beigangone):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/update"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "startDate": startdate,
          "endDate": enddate,
          "prdtCode": prdtname+"-"+prdtcode,
          "zhugangren": zhugangren,
          "beigangone": beigangone,
          "beigangthr": "",
          "id": "",
          "selectObjId": selectobjid
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:删除产品分工')
def prdt_divide_delete(t,selectobjid):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/delete"
    headers = {
        'cookie': 'token=' + t
    }
    payload=[
            selectobjid
    ]
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:下载导入模板')
def prdt_divide_downloadtemplate(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/dowmloadTemplate"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:导出')
def prdt_divide_export(t,pkid):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/exportDivide"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pkIds": [
            pkid
          ]
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:导入')
def prdt_divide_import(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/importDivide"
    file_path = '../data/产品分工表导入文件.xlsx'
    headers = {
        'cookie': 'token=' + t
    }
    data={
        "selectedDate": str(datetime.date.today()),
    }
    files= {'file': open(file_path, "rb")}
    r= requests.post(url=url,data=data,headers=headers,files=files)
    return r

#交接管理
@allure.step('step:查询我被交接')
def handover_touser_list(t,touser):
    url=f"{HOST1}/api/agnes-app/v1/dop/handover/list?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "fromUser": "",
          "toUser": touser, #"agnes"
          "approvalStatus": "",
          "startDateBegin": "",
          "startDateEnd": "",
          "endDateBegin": "",
          "endDateEnd": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询我的交接')
def handover_fromuser_list(t,fromuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/handover/list?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "fromUser": fromuser, #"agnes"
          "toUser": "",
          "approvalStatus": "",
          "startDateBegin": "",
          "startDateEnd": "",
          "endDateBegin": "",
          "endDateEnd": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:获取可选的审批人')
def handover_get_user_info(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/tree/structure/get/user/info"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userId": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #userlist=r.json()['data']

@allure.step('step: 获取objectid')
def handover_createdoc(t):
    url=f"{HOST1}/api/ecm-server/ecm/doc/createDocAndGetDocId?folderTag=2"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #objectid=r.json()['data']['objectId']

@allure.step('step: 获取所有产品')
def handover_get_prdtlist(t,userid,zhugangren):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/queryPage?pageIndex=0&pageSize=1000"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "isProductTask": "1",
          "handoverFlag": "1",
          "beginDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "userId": userid,  #"agnes"
          "zhugangren": zhugangren  #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    prdtlist=r.json()['data']['rows']
    prdtcodelist=[]
    for i in prdtlist:
        prdtcodelist.append(i['productCode'])
        '''

@allure.step('step: 获取所有岗位和岗位下可选的交接人')
def handover_get_grouplist(t,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/user/group/list-by-user-id"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "isMustHandDown": "1",
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "userId": userid   #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    grouplist=r.json()['data']
    groupidlist=[]
    userlist=[]
    for i in grouplist:
        groupidlist.append(i['userGroupId'])
        useridlist.append(i['userList'])
        
    usernamelist=[]
    for i in userlist:
       usernamelist.append(i[0]['userName'])
    '''

@allure.step('step: 获取所有角色')
def handover_get_rolelist(t,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/listAllOrgByUserId"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "role": "1",
          "handoverFlag": "1",
          "userId": userid,  #"agnes"
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    rolelist=r.json()['data']
    roleidlist=[]
    for i in rolelist:
        roleidlist.append(i['orgId'])
'''

@allure.step('step: 获取所有临时任务')
def handover_get_templist(t,attuser,userid):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSize=1000"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "role": "1",
          "taskStatus": "01",
          "taskType": "temp",
          "handoverFlag": "1",
          "taskTimeFrom": str(datetime.date.today()),
          "taskTimeTo": str(datetime.date.today()),
          "attUser": attuser,  #"agnes"
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "userId": userid  #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    templist=r.json()['data']['rows']
    tempidlist=[]
    for i in templist:
        if i['taskExecAuth']=='1111':
            tempidlist.append(i['pkId'])
        '''

@allure.step('step: 获取产品的交接人')
def handover_get_prdt_alluser(t,userid,zhugangren):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/getAllUserByUserId?handoverFlag=%221%22"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "isProductTask": "1",
          "handoverFlag": "1",
          "beginDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "userId": userid,   #"agnes"
          "zhugangren": zhugangren,   #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    prdtuserlist=r.json()['data']
    if len(prdtuserlist)!=0:
        prdtuserid = prdtuserlist[0]['userId']
        prdtusername = prdtuserlist[0]['userName']
    '''

@allure.step('step: 获取角色的交接人')
def handover_get_role_alluser(t,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/getAllUserByUserId?handoverFlag=%221%22"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "role": "1",
          "handoverFlag": "1",
          "userId": userid, #"agnes"
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    roleuserlist = r.json()['data']
    if len(roleuserlist) != 0:
        roleuserid = roleuserlist[0]['userId']
        roleusername = roleuserlist[0]['userName']
'''

@allure.step('step: 获取临时任务的交接人')
def handover_get_temp_alluser(t,attuser,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/getAllUserByUserId?handoverFlag=%221%22"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "role": "1",
          "taskStatus": "01",
          "taskType": "temp",
          "handoverFlag": "1",
          "taskTimeFrom": str(datetime.date.today()),
          "taskTimeTo": str(datetime.date.today()),
          "attUser": attuser,  #"agnes",
          "startDate": str(datetime.date.today())+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "userId": userid  #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    tempuserlist=r.json()['data']
    if len(tempuserlist)!=0:
        tempuserid = tempuserlist[0]['userId']
        tempusername = tempuserlist[0]['userName']
'''

@allure.step('step: 获取当前用户可选人员')
def handover_get_userlist(t):
    url=f"{HOST1}/api/agnes-app/v1/dop/ru/org/framework/getAllUserByUserId?handoverFlag=0"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
            "userId": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #userlist=r.json()['data']

@allure.step('step: 打开新增交接页面')
def handover_submit(t,userid,zhugangren):
    url=f"{HOST1}/api/agnes-app/v1/dop/prdt-divide-work/list/by/handover"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "isProductTask": "1",
          "handoverFlag": "1",
          "beginDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "startDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "userId":  userid, #"agnes",
          "zhugangren": zhugangren  #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 拼接交接明细数据')
def get_handover_detail(prdtcodelist,prdtuserid,prdtusername,groupidlist,groupuserlist,groupusernamelist,roleidlist,roleuserid,roleusername,tempidlist,tempuserid,tempusername):
    detaillist=[]
    if len(prdtcodelist)!=0:
        for i in prdtcodelist:
            detaillist.append(
                {
                    "type": "prdt",
                    "bizId": i,
                    "toUser": prdtuserid,
                    "isAutoTrans": "1",
                    "planType": "1"
                })
    if len(groupidlist)!=0:
     for i in range(len(groupidlist)):
        detaillist.append(
            {
                "type": "common",
                "bizId": groupidlist[i],
                "toUser": groupuserlist[i][0]['userId'],
                "isAutoTrans": "1",
                "planType": "1"
            })
    if len(roleidlist)!=0:
     for i in roleidlist:
        detaillist.append(
            {
                "type": "role",
                "bizId": i,
                "toUser": roleuserid,
                "isAutoTrans": "1",
                "planType": "1"
            })
    if len(tempidlist)!=0:
     for i in tempidlist:
        detaillist.append(
            {
                "type": "temp",
                "bizId": i,
                "toUser": tempuserid,
                "isAutoTrans": "1",
                "planType": "1"
            })

    name=[]
    if prdtusername!='' and prdtusername not in name:
        name.append(prdtusername)

    if len(groupusernamelist)!=0:
        for i in groupusernamelist:
            if i not in name:
                name.append(i)

    if tempusername!='' and tempusername not in name:
        name.append(tempusername)

    if roleusername!='' and roleusername not in name:
        name.append(roleusername)

    handoveruser=','.join(name)

    type=[]
    if len(detaillist)!=0:
        for i in detaillist:
            if i['type']=='prdt' and '产品任务' not in type:
                type.append("产品任务")
            if i['type']=='common' and '岗位任务' not in type:
                type.append("岗位任务")
            if i['type'] == 'role' and '角色' not in type:
                type.append("角色")
            if i['type']=='temp' and '临时任务' not in type:
                type.append("临时任务")

    handovertype = ','.join(type)

    detail={}
    detail['detaillist']=detaillist
    detail['handoveruser']=handoveruser
    detail['handovertype']=handovertype
    return detail

@allure.step('step: 新增交接1')
def handover_add1(t,approvaluser,applyuser,fromuser,objectid,detail):
    url=f"{HOST1}/api/agnes-app/v1/dop/handover/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "approvalUser": approvaluser,  #"agnes",
          "applyUser": applyuser,  #"agnes",
          "fromUser": fromuser,  #"agnes",
          "auditUserName": "",
          "isAgency": "0",
          "reason": "1",
          "beginDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
          "endDate": str(datetime.date.today())+"T15:59:59.999Z",
          "folderPath": objectid,
          "detailList": detail['detaillist']
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #id=r.json()['data']

@allure.step('step: 提交')
def handover_isneedapproval(t):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/isNeedApproval"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "type": 3
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step: 新增交接2')
def handover_add2(t,approvaluser,applyuser,fromuser,objectid,id,detail):
    url=f"{HOST1}/api/agnes-app/v1/mcc/approval/add"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "isAgency": "0",
          "applyData": {
            "approvalUser": approvaluser,  #"agnes",
            "applyUser": applyuser,  #"agnes",
            "fromUser": fromuser,  #"agnes",
            "auditUserName": "",
            "isAgency": "0",
            "reason": "1",
            "beginDate": str(datetime.date.today()-datetime.timedelta(days=1))+"T16:00:00.000Z",
            "endDate": str(datetime.date.today())+"T15:59:59.999Z",
            "folderPath": objectid,
            "detailList": detail['detaillist'],
            "id": id
          },
          "type": "3",
          "reason": "1",
          "applyUser": applyuser,  #"agnes",
          "approvalUser": approvaluser,  #"agnes",
          "summary": "开始时间: "+str(datetime.date.today())+" 00:00:00"+" \n结束时间: "+str(datetime.date.today())+" 23:59:59"+"\n交出人: 致宇小智, 交接人: "+detail['handoveruser']+"\n交接任务类型: "+detail['handovertype']
          #"summary": "开始时间: 2024-12-05 00:00:00 \n结束时间: 2024-12-05 23:59:59\n交出人: 致宇小智, 交接人: 财务001,it管理员,双洪波,autotask\n交接任务类型: 产品任务,岗位任务,临时任务,角色"
}
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:查询我的交接列表，获取相关参数')
def handover_fromuser_list2(t,fromuser):
    url=f"{HOST1}/api/agnes-app/v1/dop/handover/list?pageIndex=0&pageSize=100"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "fromUser": fromuser, #"agnes"
          "toUser": "",
          "approvalStatus": "",
          "startDateBegin": "",
          "startDateEnd": "",
          "endDateBegin": "",
          "endDateEnd": ""
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    '''
    datalist=r.json()['data']['rows']
    for i in datalist:
        if i['id']='':
            applyuser=i['applyUser']
            approvalstatus = i['approvalStatus']
            approvaluser = i['approvalUser']
            begindate = i['beginDate']
            crtts = i['crtTs']
            detaillist = i['detailList']
            enddate = i['endDate']
            folderpath = i['folderPath']
            fromuser=i['fromUser']
            reason= i['reason']
            type= i['type']
            updatets= i['updateTs']
'''

@allure.step('step:获取未开始的任务列表')
def handover_get_task_01(t,changeuser):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSiz"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "taskStatus": "01",
          "changeUser": changeuser,  #"agnes",
          "taskTimeFrom": str(datetime.date.today()-datetime.timedelta(days=1)),
          "taskTimeTo": str(datetime.date.today())
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #tasklist01=r.json()['data']['rows']

@allure.step('step:获取执行中的任务列表')
def handover_get_task_02(t,changeuser):
    url=f"{HOST1}/api/agnes-ac/v1/mcc/task/pending/queryPengding?pageIndex=0&pageSiz"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
          "pageIndex": 0,
          "pageSize": 100,
          "taskStatus": "02",
          "changeUser": changeuser,   #"agnes",
          "taskTimeFrom": str(datetime.date.today()-datetime.timedelta(days=1)),
          "taskTimeTo": str(datetime.date.today())
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r
    #tasklist02 = r.json()['data']['rows']

@allure.step('step:撤销交接')
def handover_revoke(t,applyuser,approvalstatus,approvaluser,begindate,crtts,detaillist,enddate,folderpath,fromuser,id,reason,type,updatets,taskidlist,userid):
    url=f"{HOST1}/api/agnes-app/v1/dop/handover/revoke"
    headers = {
        'cookie': 'token=' + t
    }
    payload={
        "applyUser": applyuser,
        "approvalStatus": approvalstatus,
        "approvalUser": approvaluser,
        "beginDate": begindate,
        "crtTs": crtts,
        "detailList": detaillist,
        "endDate": enddate,
        "folderPath": folderpath,
        "fromUser": fromuser,
        "id": id,
        "reason": reason,
        "type": type,
        "updateTs": updatets,
        "revokeDate": get_current_time(),
        "taskIdList": taskidlist,
        "remark": "撤销人: "+approvaluser+"; 撤销时间: "+get_current_time(),
        "userId": userid  #"agnes"
    }
    r=requests.post(url=url,headers=headers,json=payload)
    return r

@allure.step('step:取消交接')
def handover_cancel(t,idlist):
    url=f"{HOST1}/api/agnes-app/v1/dop/handover/batch/cancel"
    headers = {
        'cookie': 'token=' + t
    }
    payload=idlist
    r=requests.post(url=url,headers=headers,json=payload)
    return r

if __name__=='__main__':
    t = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IkFHTkVTIiwiY3J0VHMiOjE3MzI3OTk0NTcsInVzZXJJZCI6ImFnbmVzIn0.MFwRafhpdz2nKu1jU5Qw1WK5103u5YV_z3-mqn67hp0'
    r1=prdt_divide_import(t)
    print(r1.text)
