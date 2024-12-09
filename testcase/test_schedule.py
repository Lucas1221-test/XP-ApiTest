import pytest,allure
from lib.schedule import shedule_get_orgidlist,shedule_get_orglist,shedule_get_org_post,shedule_get_org_group,shedule_add,shedule_edit,shedule_get_list,shedule_preview,shedule_audit,shedule_delete
from lib.schedule import memo_listmonth,memo_getauditor,memo_getauditor_all,memo_get_roster_postlist,memo_get_roster_typelist,memo_get_roster_userlist,memo_checklist,memo_get_roster_isneedapproval,memo_add

@allure.feature("排班管理方案")
class Test_schedule:
    @allure.story('新增排班方案-编辑排班方案-预览-审核-删除')
    def test_schedule(self, get_token_fixture):
        global usergroupid
        t = get_token_fixture

        print('步骤：查询org列表')
        r =shedule_get_orglist(t,'agnes')
        assert r.json()['code'] == '00000000'
        orglist = []
        data1 = r.json()['data']
        for i in data1:
            orglist.append(i['orgId'])

        print('步骤：查询org列表2')
        r1 = shedule_get_orgidlist(t,orglist)
        assert r1.json()['code'] == '00000000'
        orgidlist = []
        data2 = r1.json()['data']
        print(data2)
        for i in data2:
            orgidlist.append(i['id'])
        print(orgidlist)

        print('步骤：查询org列表-获取岗位列表')
        r2 = shedule_get_org_post(t,orgidlist)
        assert r2.json()['code'] == '00000000'
        list = r2.json()['data']['rows']
        usergroupid=''
        for i in list:
            if i['userGroupName'] == '测试岗位00001':
                usergroupid = i['userGroupId']

        print('步骤：查询岗位数据')
        r3 =shedule_get_org_group(t,usergroupid)
        assert r3.json()['code'] == '00000000'
        grouplist=r3.json()['data']['rows']
        person1=r3.json()['data']['rows'][0]['userId']
        person2 = r3.json()['data']['rows'][1]['userId']

        startdate="2024-12-26"
        enddate = "2024-12-27"

        print('步骤：新增排班方案')
        r4 = shedule_add(t,startdate,enddate,usergroupid,grouplist,person1,person2,'ZB')
        assert r4.json()['code'] == '00000000'

        print('步骤：新增后，查询排班列表,获取排班相关参数')
        r5 = shedule_get_list(t)
        assert r5.json()['code'] == '00000000'

        id = r5.json()['data']['rows'][0]['id']
        enddate = r5.json()['data']['rows'][0]['endDate']
        flag = r5.json()['data']['rows'][0]['flag']
        planname = r5.json()['data']['rows'][0]['planName']
        planstatus = r5.json()['data']['rows'][0]['planStatus']
        postname = r5.json()['data']['rows'][0]['postName']
        startdate = r5.json()['data']['rows'][0]['startDate']
        status = r5.json()['data']['rows'][0]['status']
        updatets = r5.json()['data']['rows'][0]['updateTs']
        updateuser = r5.json()['data']['rows'][0]['updateUser']
        workday = r5.json()['data']['rows'][0]['workday']

        print('步骤：编辑排班方案')
        r6 = shedule_edit(t,usergroupid,grouplist,person1,person2,'ZB',enddate,flag,id,planname,startdate,status,updatets,updateuser)
        assert r6.json()['code'] == '00000000'

        print('步骤：编辑后，查询排班列表,获取排班相关参数')
        r7 = shedule_get_list(t)
        assert r7.json()['code'] == '00000000'

        id = r7.json()['data']['rows'][0]['id']
        enddate = r7.json()['data']['rows'][0]['endDate']
        flag = r7.json()['data']['rows'][0]['flag']
        planname = r7.json()['data']['rows'][0]['planName']
        planstatus = r7.json()['data']['rows'][0]['planStatus']
        postname = r7.json()['data']['rows'][0]['postName']
        startdate = r7.json()['data']['rows'][0]['startDate']
        status = r7.json()['data']['rows'][0]['status']
        updatets = r7.json()['data']['rows'][0]['updateTs']
        updateuser = r7.json()['data']['rows'][0]['updateUser']
        workday = r7.json()['data']['rows'][0]['workday']

        print('步骤：预览排班方案')
        r8 = shedule_preview(t,enddate,flag,id,planname,planstatus,postname,startdate,status,updatets,updateuser,workday)
        assert r8.json()['code'] == '00000000'

        print('步骤：审核排班方案')
        r8 = shedule_audit(t, usergroupid,grouplist,person1,person2,'ZB',enddate,flag,id,planname,startdate,status,updatets,updateuser)
        assert r8.json()['code'] == '00000000'

        print('步骤：审核后，查询排班列表,获取排班相关参数')
        r9 = shedule_get_list(t)
        assert r9.json()['code'] == '00000000'

        id = r9.json()['data']['rows'][0]['id']
        enddate = r9.json()['data']['rows'][0]['endDate']
        flag = r9.json()['data']['rows'][0]['flag']
        planname = r9.json()['data']['rows'][0]['planName']
        planstatus = r9.json()['data']['rows'][0]['planStatus']
        postname = r9.json()['data']['rows'][0]['postName']
        startdate = r9.json()['data']['rows'][0]['startDate']
        status = r9.json()['data']['rows'][0]['status']
        updatets = r9.json()['data']['rows'][0]['updateTs']
        updateuser = r9.json()['data']['rows'][0]['updateUser']
        workday = r9.json()['data']['rows'][0]['workday']

        #print('步骤：删除排班方案')
        #r10 =shedule_delete(t,enddate,flag,id,planname,planstatus,postname,startdate,status,updatets,updateuser,workday)
        #assert r10.json()['code'] == '00000000'

@allure.feature("排班日历")
class Test_memo:
    @allure.story('查询当日排班日历-临时调班')
    def test_memo(self, get_token_fixture):
        global dict
        t = get_token_fixture

        enddate = "2024-12-27"
        startdate = "2024-12-26"
        
        print('步骤：查询当日排班日历')
        r1 =memo_listmonth(t)
        assert r1.json()['code'] == '00000000'

        print('步骤：获取默认调班审批人')
        r2 =memo_getauditor(t,'qinyun')
        assert r2.json()['code'] == '00000000'
        auditor_userid = r2.json()['data']['userId']

        print('步骤：获取换出日期可选岗位')
        r3 = memo_get_roster_postlist(t,'qinyun',startdate)
        assert r3.json()['code'] == '00000000'
        postlist=r3.json()['data']
        postid=r3.json()['data'][0]['userGroupId']
        postname = r3.json()['data'][0]['userGroupName']

        print('步骤：获取全部班次')
        r4 = memo_get_roster_typelist(t,'qinyun',startdate,postid)
        assert r4.json()['code'] == '00000000'
        rostertypelist=r4.json()['data']
        rostertype=r4.json()['data'][0]['dictId']
        rostertypename=r4.json()['data'][0]['dictName']

        print('步骤：获取换回日期班次人员')
        r5 = memo_get_roster_userlist(t,'ZB',enddate,postid)
        assert r5.json()['code'] == '00000000'
        personlist=r5.json()['data']
        targetuserid=r5.json()['data'][0]['rosterNoticeUser']
        targetusername=r5.json()['data'][0]['userName']

        print('步骤：临时调班')
        r6 = memo_checklist(t,startdate,enddate,postid,rostertype,targetuserid,postlist,personlist,rostertypelist,'qinyun',auditor_userid)
        assert r6.json()['code'] == '00000000'

        print('步骤：')
        r7 = memo_get_roster_isneedapproval(t)
        assert r7.json()['code'] == '00000000'

        print('步骤：调班完成')
        r8 = memo_add(t, startdate, enddate, postid, rostertype, targetuserid, postlist, personlist,
                            rostertypelist, 'qinyun', auditor_userid,postname,rostertypename,targetusername)
        assert r8.json()['code'] == '00000000'


if __name__=='__main__':
    pytest.main(['../test_schedule.py','-s'])