import pytest,allure
from lib.org import org_framework_add, org_framework_edit, org_framework_delete, org_framework_list, org_framework_member_add,org_framework_member_edit,org_framework_member_list,org_framework_member_delete,org_framework_get_userinfo,group_getorgtree, \
    group_ref_get_org
from lib.org import prdt_divide_add,prdt_divide_update,prdt_divide_query,prdt_divide_delete,prdt_divide_export,prdt_divide_import,prdt_divide_downloadtemplate,prdt_prdtselect,prdt_productuser
from lib.org import group_config_add,group_config_edit,group_save_ref,group_edit_ref,group_delete,group_delete_ref,group_getorgtree,group_config_list,group_ref_get_user_query,group_ref_get_org
from lib.org import handover_touser_list,handover_fromuser_list,handover_fromuser_list2,handover_get_user_info,handover_createdoc,handover_get_prdtlist,handover_get_grouplist,handover_get_rolelist,handover_get_templist,\
    handover_get_prdt_alluser,handover_get_role_alluser,handover_get_temp_alluser,handover_submit,get_handover_detail,handover_add1,handover_isneedapproval,handover_add2,handover_cancel,handover_revoke,handover_get_task_01,handover_get_task_02
from lib.task_operate import task_approval_pass,task_approval_refuse,task_approval_list,task_handover_get_doc
from common.read_yml import get_timestamp

@allure.feature("组织架构")
class Test_org:
    @allure.story('新增组织-编辑组织-删除组织')
    def test_org(self,get_token_fixture):
        t=get_token_fixture

        print('步骤一：新增组织')
        r=org_framework_add(t,'DEPARTMENT')
        assert r.json()['code'] == '00000000'

        print('步骤二：查询组织列表')
        r1=org_framework_list(t)
        assert r1.json()['code']=='00000000'
        orglist = r1.json()['data']['rows']
        for item in orglist:
            try:
                if item['orgName'] == '自动化一级测试部门':
                    id = item['id']
                    orgname = ['orgName']
                    orgtype = item['orgType']
                    status = item['status']
                    publicemail = item['publicEmail']
                    onjobquantity = item['onJobQuantity']
                    parentnodecode = item['parentNodeCode']
                    treename = item['treeName']
                    treenames = item['treeNames']
                    treenode = item['treeNode']
                    treenodes = item['treeNodes']
                    updatets = item['updateTs']
                    updateuser = item['updateUser']
            except IndexError:
                print('没有查询到组织')

        print('步骤三：编辑组织')
        r2 = org_framework_edit(t,id,orgname,orgtype,status,publicemail,onjobquantity,parentnodecode,treename,treenames,treenode,treenodes,updatets,updateuser)
        print(r2.json())
        assert r2.json()['code'] == '00000000'

        print('步骤四：删除组织')
        r3 = org_framework_delete(t,id,orgname,orgtype,status,publicemail,onjobquantity,parentnodecode,treename,treenames,treenode,treenodes,updatets,updateuser)
        assert r3.json()['code'] == '00000000'

    @allure.story('新增用户-编辑用户-删除用户')
    def test_org_user(self, get_token_fixture):
        t = get_token_fixture

        print('步骤：获取可选用户列表')
        r = org_framework_get_userinfo(t)
        assert r.json()['code'] == '00000000'

        userlist = r.json()['data']
        for i in userlist:
            if i['userName'] == '致宇小智':
                userid = i['userId']
                username = i['userName']

        print('步骤：组织下新增用户(成员)')
        r1 = org_framework_member_add(t,"1j8pibs51ynmi",userid,'0')
        assert r1.json()['code'] == '00000000'

        print('步骤：查询当前组织下用户列表')
        r2 = org_framework_member_list(t,"1j8pibs51ynmi")
        assert r2.json()['code'] == '00000000'

        data = r2.json()['data']['rows']
        for i in data:
            print(i)
            if i['userId'] == userid:
                id = i['id']
                orgid = i['orgId']
                orgname = i['orgName']
                userid = i['userId']
                username = i['username']
                role = i['role']
                status = i['status']
                updatets = i['updateTs']
                updateuser = i['updateUser']
                userstatus = i['userStatus']
                startdate = i['startDate']
                enddate = i['endDate']

        print('步骤：组织下编辑用户')
        r3 = org_framework_member_edit(t,id,orgid,orgname,userid,username,role,status,startdate,enddate,updatets,updateuser,userstatus)
        assert r3.json()['code'] == '00000000'

        print('步骤：组织下删除用户')
        r4 = org_framework_member_delete(t,id,orgid,orgname,role,startdate,enddate,status,updatets,updateuser,userid,username,userstatus)
        assert r4.json()['code'] == '00000000'

@allure.feature("岗位设置")
class Test_group:
    @allure.story('新增岗位-编辑岗位-删除岗位')
    def test_group(self, get_token_fixture):
        t = get_token_fixture

        print('步骤一：查询orgtree,获取orgid')
        r=group_getorgtree(t)
        assert r.json()['code'] == '00000000'
        orglist=r.json()['data']
        for i in orglist:
            if i['orgName']=='测试一级部门勿删':
                orgid=i['id']

        print('步骤二：新增岗位')
        r1 = group_config_add(t,'01',orgid,'0','1','','1')
        assert r1.json()['code'] == '00000000'

        print('步骤：查询岗位列表')
        r2 = group_config_list(t)
        assert r2.json()['code'] == '00000000'
        grouplist1=r2.json()['data']['rows']
        for item in grouplist1:
            try:
                if item['userGroupName']=='自动化测试岗位':
                    groupid=item['userGroupId']
                    groupname = item['userGroupName']
                    grouptag = item['userGroupTag']
                    orgid = item['orgId']
                    orgname = item['orgName']
                    isproducttask = item['isProductTask']
                    ismusthanddown = item['isMustHandDown']
                    director = item['director']
                    crtts = item['crtTs']
                    crtuser = item['crtUser']
            except IndexError:
                print('没有查询到岗位')

        print('步骤：编辑岗位')
        r3 = group_config_edit(t,groupid,groupname,grouptag,orgid,orgname,isproducttask,ismusthanddown,director,crtts,crtuser)
        assert r3.json()['code'] == '00000000'

        print('步骤：查询岗位列表')
        r33 = group_config_list(t)
        assert r33.json()['code'] == '00000000'
        grouplist2 = r33.json()['data']['rows']
        for item in grouplist2:
            try:
                if item['userGroupName'] == '自动化测试岗位':
                    groupid = item['userGroupId']
                    groupname = item['userGroupName']
                    grouptag = item['userGroupTag']
                    orgid = item['orgId']
                    orgname = item['orgName']
                    isproducttask = item['isProductTask']
                    ismusthanddown = item['isMustHandDown']
                    director = item['director']
                    crtts = item['crtTs']
                    crtuser = item['crtUser']
            except IndexError:
                print('没有查询到岗位')

        print('步骤五：删除岗位')
        r4 = group_delete(t,crtts,crtuser,director,ismusthanddown,isproducttask,groupid,groupname,grouptag,orgid,orgname)
        assert r4.json()['code'] == '00000000'

    @allure.story('新增用户-编辑用户-删除用户')
    def test_group_user(self, get_token_fixture):
        t = get_token_fixture

        print('步骤一：查询岗位列表,选择一个岗位新增用户')
        r = group_config_list(t)
        assert r.json()['code'] == '00000000'
        grouplist=r.json()['data']['rows']
        for i in grouplist:
            if i['userGroupName']=='测试岗位勿删':
                groupid = i['userGroupId']
                groupname = i['userGroupName']
                orgid = i['orgId']
                orgname = i['orgName']

        print('步骤二：查询org列表下可选的用户：user')
        r1 = group_ref_get_org(t, orgid)
        assert r1.json()['code'] == '00000000'
        userid=r1.json()['data'][0]['userId']
        username = r1.json()['data'][0]['userName']

        print('步骤三：新增用户')
        r2 = group_save_ref(t,groupid,userid,'1')
        assert r2.json()['code'] == '00000000'

        print('步骤四：查询用户列表')
        r3 = group_ref_get_user_query(t,groupid)
        assert r3.json()['code'] == '00000000'
        userlist = r3.json()['data']['rows']
        for item in userlist:
            try:
                if item['userId'] == userid:
                    crtts = item['crtTs']
                    startdate = item['startDate']
                    enddate = item['endDate']
                    ismain = item['isMain']
                    orgname = item['orgName']
                    groupname = item['userGroupName']
                    grouprefid = item['userGroupRefId']
                    sequencenum = item['sequenceNum']
                    username = item['userName']
                    userid = item['userId']
                    userstatus = item['userStatus']
            except IndexError:
                print('没有查询到用户')

        print('步骤五：编辑用户')
        r4 = group_edit_ref(t,groupid,userid,ismain,startdate,enddate,crtts,orgname,orgid,groupname,grouprefid,username,sequencenum,userstatus)
        assert r4.json()['code'] == '00000000'

        print('步骤六：删除用户')
        r5 = group_delete_ref(t,userid,groupid,grouprefid)
        #assert r5.json()['code'] == '00000000'

@allure.feature("产品分工表")
class Test_prdt:
    @allure.story('新增产品分工-查询产品分工表-编辑产品分工-删除产品分工')
    def test_prdt(self, get_token_fixture):
        t = get_token_fixture

        print('步骤: 查询可选的产品列表,获取产品的prdtcode')
        r1 = prdt_prdtselect(t)
        assert r1.json()['code'] == '00000000'
        #prdtcode = r1.json()['data'][0]['productCode']
        #prdtname = r1.json()['data'][0]['productName']

        print('步骤: 查询可选的人员,获取主岗和备岗人员userid')
        r2 = prdt_productuser(t)
        assert r2.json()['code'] == '00000000'
        zhugangren=r2.json()['data'][0]['userId']
        beigangone=r2.json()['data'][1]['userId']

        print('步骤：新增产品分工表')
        r3=prdt_divide_add(t,"bai_test_product",zhugangren,beigangone)
        assert r3.json()['code'] == '00000000'

        print('步骤：查询产品分工表')
        r4 = prdt_divide_query(t)
        assert r4.json()['code'] == '00000000'
        prdtlist=r4.json()['data']['rows']
        for i in prdtlist:
            if i['productName']=='测试产品勿删':
                selectobjid = i['id']
                prdtcode=i['productCode']
                prdtname = i['productName']
                startdate = i['startDate']
                enddate = i['endDate']

        print('步骤：编辑产品分工表')
        r5 = prdt_divide_update(t,prdtcode,startdate,enddate,prdtname,selectobjid,zhugangren,beigangone)
        assert r5.json()['code'] == '00000000'

        print('步骤：删除产品分工表')
        r6 = prdt_divide_delete(t,selectobjid)
        assert r6.json()['code'] == '00000000'

    @allure.story('查询产品分工表-导出-下载模板-导入')
    def test_prdt2(self, get_token_fixture):
        t = get_token_fixture

        print('步骤：查询产品分工表')
        r1 = prdt_divide_query(t)
        assert r1.json()['code'] == '00000000'
        selectobjid = r1.json()['data']['rows'][0]['id']

        print('步骤：导出产品分工表')
        r2 = prdt_divide_export(t,selectobjid)
        assert r2.json()['code'] == '00000000'

        print('步骤：下载模板')
        r3 =prdt_divide_downloadtemplate(t)
        assert r3.json()['code'] == '00000000'

        print('步骤：导入')
        r4 = prdt_divide_import(t)
        assert r4.json()['code'] == '00000000'

'''
@allure.feature("交接管理")
class Test_handover:
    @allure.story('查询我的交接-查询交接给我的-新增交接-取消交接')
    def test_handover1(self, get_token_fixture):
        t = get_token_fixture

        print('步骤: 查询我的交接')
        r1 = handover_fromuser_list(t,'agnes')
        assert r1.json()['code'] == '00000000'

        print('步骤: 查询我被交接')
        r2 = handover_touser_list(t, 'agnes')
        assert r2.json()['code'] == '00000000'

        print('步骤: 获取objectid')
        r3 = handover_createdoc(t)
        assert r3.json()['status'] == True
        objectid = r3.json()['data']['objectId']

        print('步骤: 获取所有产品')
        r4 = handover_get_prdtlist(t,'agnes','agnes')
        assert r4.json()['code'] == '00000000'
        prdtlist = r4.json()['data']['rows']
        prdtcodelist = []
        if len(prdtlist)!=0:
            for i in prdtlist:
                prdtcodelist.append(i['productCode'])

        print('步骤: 获取所有产品的交接人')
        r41 = handover_get_prdt_alluser(t,'agnes','agnes')
        assert r41.json()['code'] == '00000000'
        prdtuserlist=r41.json()['data']
        prdtuserid=''
        prdtusername=''
        if len(prdtuserlist)!=0:
            prdtuserid=prdtuserlist[0]['userId']
            prdtusername = prdtuserlist[0]['userName']

        print('步骤: 获取所有岗位和岗位交接人')
        r5 = handover_get_grouplist(t,'agnes')
        assert r5.json()['code'] == '00000000'

        grouplist = r5.json()['data']
        groupidlist = []
        groupuserlist = []
        groupusernamelist=[]
        if len(grouplist)!=0:
            for i in grouplist:
                groupidlist.append(i['userGroupId'])
                groupuserlist.append(i['userList'])

            for i in groupuserlist:
                if i[0]['userName'] not in groupusernamelist:
                    groupusernamelist.append(i[0]['userName'])

        print('步骤: 获取所有角色')
        r6 = handover_get_rolelist(t,'agnes')
        assert r6.json()['code'] == '00000000'

        rolelist = r6.json()['data']
        roleidlist = []
        if len(rolelist)!=0:
            for i in rolelist:
                roleidlist.append(i['orgId'])

        print('步骤: 获取所有角色的交接人')
        r61 = handover_get_role_alluser(t,'agnes')
        assert r61.json()['code'] == '00000000'
        roleuserlist=r61.json()['data']
        roleuserid=''
        roleusername=''

        if len(roleuserlist)!=0:
            roleuserid=roleuserlist[0]['userId']
            roleusername = roleuserlist[0]['userName']

        print('步骤: 获取所有临时任务')
        r7 = handover_get_templist(t,'agnes','agnes')
        assert r7.json()['code'] == '00000000'

        templist = r7.json()['data']['rows']
        tempidlist = []
        if len(templist)!=0:
            for i in templist:
                if i['taskExecAuth'] == '1111':
                    tempidlist.append(i['pkId'])

        print('步骤: 获取所有临时任务的交接人')
        r71 = handover_get_temp_alluser(t,'agnes','agnes')
        assert r71.json()['code'] == '00000000'
        tempuserlist=r71.json()['data']
        tempuserid=''
        tempusername=''
        if len(tempuserlist)!=0:
            tempuserid=r71.json()['data'][0]['userId']
            tempusername = r71.json()['data'][0]['userName']

        print('步骤: 拼接交接明细数据')
        detail = get_handover_detail(prdtcodelist,prdtuserid,prdtusername,groupidlist,groupuserlist,groupusernamelist,roleidlist,roleuserid,roleusername,tempidlist,tempuserid,tempusername)

        print('步骤: 打开新增交接页面')
        r8 = handover_submit(t, 'agnes', 'agnes')
        assert r8.json()['code'] == '00000000'

        print('步骤: 新增交接')
        r9 = handover_add1(t,'agnes','agnes','agnes',objectid,detail)
        assert r9.json()['code'] == '00000000'

        id = r9.json()['data']

        print('步骤: 新增交接')
        r10 = handover_isneedapproval(t)
        assert r10.json()['code'] == '00000000'

        print('步骤: 新增交接')
        r11 = handover_add2(t,'agnes','agnes','agnes',objectid,id,detail)
        assert r11.json()['code'] == '00000000'

        print('步骤：取消交接')
        r12=handover_cancel(t,[id])
        assert r12.json()['code'] == '00000000'

    @allure.story('新增交接-任务中心查看交接详情-任务中心审核通过-撤销交接')
    def test_handover2(self, get_token_fixture):
        t = get_token_fixture

        print('步骤: 获取objectid')
        r3 = handover_createdoc(t)
        assert r3.json()['status'] == True
        objectid = r3.json()['data']['objectId']

        print('步骤: 获取所有产品')
        r4 = handover_get_prdtlist(t, 'agnes', 'agnes')
        assert r4.json()['code'] == '00000000'
        prdtlist = r4.json()['data']['rows']
        prdtcodelist = []
        if len(prdtlist) != 0:
            for i in prdtlist:
                prdtcodelist.append(i['productCode'])

        print('步骤: 获取所有产品的交接人')
        r41 = handover_get_prdt_alluser(t, 'agnes', 'agnes')
        assert r41.json()['code'] == '00000000'
        prdtuserlist = r41.json()['data']
        prdtuserid = ''
        prdtusername = ''
        if len(prdtuserlist) != 0:
            prdtuserid = prdtuserlist[0]['userId']
            prdtusername = prdtuserlist[0]['userName']

        print('步骤: 获取所有岗位和岗位交接人')
        r5 = handover_get_grouplist(t, 'agnes')
        assert r5.json()['code'] == '00000000'

        grouplist = r5.json()['data']
        groupidlist = []
        groupuserlist = []
        groupusernamelist = []
        if len(grouplist) != 0:
            for i in grouplist:
                groupidlist.append(i['userGroupId'])
                groupuserlist.append(i['userList'])

            for i in groupuserlist:
                if i[0]['userName'] not in groupusernamelist:
                    groupusernamelist.append(i[0]['userName'])

        print('步骤: 获取所有角色')
        r6 = handover_get_rolelist(t, 'agnes')
        assert r6.json()['code'] == '00000000'

        rolelist = r6.json()['data']
        roleidlist = []
        if len(rolelist) != 0:
            for i in rolelist:
                roleidlist.append(i['orgId'])

        print('步骤: 获取所有角色的交接人')
        r61 = handover_get_role_alluser(t, 'agnes')
        assert r61.json()['code'] == '00000000'
        roleuserlist = r61.json()['data']
        roleuserid = ''
        roleusername = ''

        if len(roleuserlist) != 0:
            roleuserid = roleuserlist[0]['userId']
            roleusername = roleuserlist[0]['userName']

        print('步骤: 获取所有临时任务')
        r7 = handover_get_templist(t, 'agnes', 'agnes')
        assert r7.json()['code'] == '00000000'

        templist = r7.json()['data']['rows']
        tempidlist = []
        if len(templist) != 0:
            for i in templist:
                if i['taskExecAuth'] == '1111':
                    tempidlist.append(i['pkId'])

        print('步骤: 获取所有临时任务的交接人')
        r71 = handover_get_temp_alluser(t, 'agnes', 'agnes')
        assert r71.json()['code'] == '00000000'
        tempuserlist = r71.json()['data']
        tempuserid = ''
        tempusername = ''
        if len(tempuserlist) != 0:
            tempuserid = r71.json()['data'][0]['userId']
            tempusername = r71.json()['data'][0]['userName']

        print('步骤: 拼接交接明细数据')
        detail = get_handover_detail(prdtcodelist, prdtuserid, prdtusername, groupidlist, groupuserlist,
                                     groupusernamelist, roleidlist, roleuserid, roleusername, tempidlist, tempuserid,
                                     tempusername)

        print('步骤: 打开新增交接页面')
        r8 = handover_submit(t, 'agnes', 'agnes')
        assert r8.json()['code'] == '00000000'

        print('步骤: 新增交接')
        r9 = handover_add1(t, 'agnes', 'agnes', 'agnes', objectid, detail)
        assert r9.json()['code'] == '00000000'

        id = r9.json()['data']

        print('步骤: 新增交接')
        r10 = handover_isneedapproval(t)
        assert r10.json()['code'] == '00000000'

        print('步骤: 新增交接')
        r11 = handover_add2(t, 'agnes', 'agnes', 'agnes', objectid, id, detail)
        assert r11.json()['code'] == '00000000'

        idd=''

        print('步骤：审批中心查询我的交接-获取数据')
        r12 = task_approval_list(t, '1')
        assert r12.json()['code'] == '00000000'
        list1=r12.json()['data']['rows']
        dict1={}
        for i in list1:
            if i['id']==idd:
                dict1=i

        applydata = dict1['applyData']
        applydate = dict1['applyDate']
        applyusername = dict1['applyUsername']
        approvalusername = dict1['approvalUsername']
        isagency = dict1['isAgency']
        reason = dict1['reason']
        status = dict1['status']
        summary = dict1['summary']
        type = dict1['type']
        urgenum = dict1['urgeNum']

        print('步骤：审批中心查看交接详情')
        r13 = task_handover_get_doc(t, objectid)
        print(r13.json())
        # assert r13.json()['code'] == '00000000'

        print('步骤：审批中心审核通过')
        r14 = task_approval_pass(t, applydata, applydate, applyusername, approvalusername, id, isagency, reason, status,
                                 summary, type, urgenum)
        assert r14.json()['code'] == '00000000'

        print('步骤：查询我的交接列表，获取相关参数')
        r15=handover_fromuser_list(t,'agnes')
        assert r15.json()['code'] == '00000000'
        list2 = r15.json()['data']['rows']
        dict2={}
        for i in list2:
            if i['id']== id:
               dict2=i

        applyuser = dict2['applyUser']
        approvalstatus = dict2['approvalStatus']
        approvaluser = dict2['approvalUser']
        begindate = dict2['beginDate']
        crtts = dict2['crtTs']
        detaillist = dict2['detailList']
        enddate = dict2['endDate']
        folderpath = dict2['folderPath']
        fromuser = dict2['fromUser']
        reason = dict2['reason']
        type = dict2['type']
        updatets = dict2['updateTs']

        print('步骤：获取未开始的任务列表')
        r16=handover_get_task_01(t,'agnes')
        assert r16.json()['code'] == '00000000'
        tasklist01 = r16.json()['data']['rows']

        print('步骤：获取执行中的任务列表')
        r17 = handover_get_task_02(t,'agnes')
        assert r17.json()['code'] == '00000000'
        tasklist02 = r17.json()['data']['rows']

        taskidlist=[]
        if len(tasklist01)!=0:
            for i in tasklist01:
                taskidlist.append(i['pkId'])
        if len(tasklist02)!=0:
            for i in tasklist02:
                taskidlist.append(i['pkId'])

        print('步骤：撤销交接')
        r18=handover_revoke(t,applyuser,approvalstatus,approvaluser,begindate,crtts,detaillist,enddate,folderpath,fromuser,id,reason,type,updatets,taskidlist,'agnes')
        assert r18.json()['code'] == '00000000'
'''

if __name__=='__main__':
    pytest.main(['../test_org.py','-s'])
