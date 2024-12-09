import pytest,allure
from lib.task_operate import task_add, task_get_model, task_pre_save, task_get_single_step, task_query_theme, \
    task_get_frequencyinfo, task_get_block, task_saveblock, task_get_step_block, task_get_casebody, task_check, \
    task_acceptance, task_publish, task_submit, task_query_theme_task, task_back, task_save_xcpmodel, task_stop, \
    task_query_fortaskname, task_approval_type, task_get_memberlist, task_approval_delay, task_approval_list, \
    task_approval_urge, task_approval_pass, task_approval_approval, task_approval_refuse, task_cancel
from lib.task_operate import task_get_step,task_block_delete,task_del,task_addtemp_temptask

@allure.feature("任务配置")
class Test_config:

    #@pytest.mark.repeat(10000)
    @allure.story('新增单节点岗位任务-绑定积木-审核-验收-发布-完成')
    def test_task_1(self, get_token_fixture):
        t = get_token_fixture
        print('步骤：获取实例id')
        r = task_get_model(t)
        caseid = r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤：填写任务名称')
        r1 = task_pre_save(t, caseid, 'caseV3', '2')
        assert r1.json()['code'] == '00000000'
        taskname = r1.json()['data']['reTaskDef']['taskName']
        taskid = r1.json()['data']['reTaskDef']['taskId']
        casedefid = r1.json()['data']['caseDefId']
        crtts = r1.json()['data']['reTaskDef']['crtTs']
        crtuser = r1.json()['data']['reTaskDef']['crtUser']
        updatets = r1.json()['data']['reTaskDef']['updateTs']
        updatetuser = r1.json()['data']['reTaskDef']['updateUser']
        distype = r1.json()['data']['reTaskDef']['disType']
        taskinitdays = r1.json()['data']['reTaskDef']['taskInitDays']
        taskstatus = r1.json()['data']['reTaskDef']['taskStatus']
        casetype = r1.json()['data']['reTaskDef']['configDef']

        print('步骤: 生成任务实例')
        r2 = task_save_xcpmodel(t, caseid, taskname)
        assert r2.json()['code'] == '00000000'

        print('步骤：获取当前case下的stepcode')
        r3 = task_get_single_step(t)
        assert r3.json()['code'] == '00000000'
        stepcode = r3.json()['data']

        print('步骤：查询用户可见任务主题，获取themeid')
        r4 = task_query_theme(t, "agnes")
        assert r4.json()['code'] == '00000000'
        themeid = r4.json()['data'][0]['pkId']
        themename = r4.json()['data'][0]['themeName']
        canfb = r4.json()['data'][0]['canFb']
        canht = r4.json()['data'][0]['canHt']
        cansc = r4.json()['data'][0]['canSc']
        canset = r4.json()['data'][0]['canSet']
        cansh = r4.json()['data'][0]['canSh']
        canty = r4.json()['data'][0]['canTy']
        canys = r4.json()['data'][0]['canYs']

        print('步骤：查询频率列表，获取funcid')
        r5 = task_get_frequencyinfo(t)
        assert r5.json()['code'] == '00000000'
        funcid = r5.json()['data'][0]['fnId']

        print('步骤：任务配置')
        r6 = task_add(t, distype, updatetuser, taskname, crtts, crtuser, caseid, updatets, taskid, taskinitdays,
                      taskstatus, casetype, themeid, casedefid, funcid, stepcode)
        assert r6.json()['code'] == '00000000'

        print('步骤七：获取第一个积木类型下所有的积木块')
        r7 = task_get_block(t, '02')
        assert r7.json()['code'] == '00000000'
        blockcode = r7.json()['data'][0]['blockCode']
        blocktype = r7.json()['data'][0]['blockType']

        print('步骤八：新增积木')
        r8 = task_saveblock(t, stepcode, caseid, blocktype, blockcode)
        assert r8.json()['code'] == '00000000'

        print('步骤：审核任务')
        r9 = task_check(t, taskid)
        assert r9.json()['code'] == '00000000'

        print('步骤：验收任务')
        r10 = task_acceptance(t, taskid)
        assert r10.json()['code'] == '00000000'

        print('步骤：查询任务的casebody')
        r11 = task_get_casebody(t, casedefid)
        assert r11.json()['code'] == '00000000'
        casebody = r11.json()['data']['caseDefBody']

        print('步骤：查询任务主题下的任务列表，获取相关参数')
        r12 = task_query_theme_task(t, themeid)
        assert r12.json()['code'] == '00000000'

        # actionparam=r12.json()['data']['rows'][0]['reTaskDef']['actionParam']
        # biztag = r12.json()['data']['rows'][0]['reTaskDef']['bizTag']
        crtts = r12.json()['data']['rows'][0]['reTaskDef']['crtTs']
        crtuser = r12.json()['data']['rows'][0]['reTaskDef']['crtUser']
        updatets = r12.json()['data']['rows'][0]['reTaskDef']['updateTs']
        updateuser = r12.json()['data']['rows'][0]['reTaskDef']['updateUser']
        # tasktitle= r.json()['data']['rows'][0]['reTaskDef']['taskTitle']
        # zruser= r.json()['data']['rows'][0]['reTaskDef']['zrUser']

        print('步骤：发布任务')
        r13 = task_publish(t, canfb, canht, cansc, canset, cansh, canty, canys, casedefid, caseid, casetype, crtts,
                           crtuser, distype, funcid, taskid, taskname, taskinitdays, themeid, themename, updatets,
                           updateuser, casebody)
        assert r13.json()['code'] == '00000000'

'''
    #@pytest.mark.repeat(20010)
    @allure.story('新增临时单节点任务-延期')
    def test_task_1(self, get_token_fixture):
        t = get_token_fixture

        #print('步骤：临时任务')
        #r = task_addtemp_temptask(t)
        #assert r.json()['code'] == '00000000'

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        r14 = task_query_fortaskname(t, "temp001")
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        #biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        #biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        #executeuser = r14.json()['data']['rows'][0]['executeUser']
        #ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        #prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        #taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        #updatets = r14.json()['data']['rows'][0]['updateTs']

        print('步骤：')
        r15 = task_approval_type(t, '1')
        assert r15.json()['code'] == '00000000'

        print('步骤：获取人员')
        r16 = task_get_memberlist(t)
        assert r16.json()['code'] == '00000000'
        approvaluser = r16.json()['data']['rows'][0]['userId']
        memberid = r16.json()['data']['rows'][1]['userId']
        membername = r16.json()['data']['rows'][1]['username']

        print('步骤：延期任务')
        r17 = task_approval_delay(t, 'agnes', taskname, caseid, tasktimefrom, tasktimeto)
        assert r17.json()['code'] == '00000000'

        print('步骤：审批中心查询我的审批-获取数据')
        r18 = task_approval_list(t, '1')
        assert r18.json()['code'] == '00000000'

        list = r18.json()['data']['rows']
        dict = {}
        for i in list:
            if i['id'] == "d7ea19bab9152e15d12584128f856e3e":
                dict = i

        print(dict)
        applydata = dict['applyData']
        applydate = dict['applyDate']
        applyusername = dict['applyUsername']
        approvalusername = dict['approvalUsername']
        isagency = dict['isAgency']
        reason = dict['reason']
        status = dict['status']
        summary = dict['summary']
        type = dict['type']
        urgenum = dict['urgeNum']

        print("步骤：催办任务")
        r19 = task_approval_urge(t, applydata, applydate, applyusername, approvalusername, "d7ea19bab9152e15d12584128f856e3e", isagency, reason,
                                 status, summary, type, urgenum)
        assert r19.json()['code'] == '00000000'

        print('步骤：审批中心审核通过')
        r20 = task_approval_pass(t, applydata, applydate, applyusername, approvalusername, "d7ea19bab9152e15d12584128f856e3e", isagency, reason,
                                 status,
                                 summary, type, urgenum)
        assert r20.json()['code'] == '00000000'

    @allure.story('新增临时单节点任务-转办')
    def test_task_1(self, get_token_fixture):
        t = get_token_fixture

        #print('步骤：临时任务')
        #r = task_addtemp_temptask(t)
        #assert r.json()['code'] == '00000000'

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        r14 = task_query_fortaskname(t, "temp002")
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        #biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        #biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        #executeuser = r14.json()['data']['rows'][0]['executeUser']
        #ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        #prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        #taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        #updatets = r14.json()['data']['rows'][0]['updateTs']

        print('步骤：')
        r15 = task_approval_type(t, '1')
        assert r15.json()['code'] == '00000000'

        print('步骤：获取人员')
        r16 = task_get_memberlist(t)
        assert r16.json()['code'] == '00000000'
        approvaluser = r16.json()['data']['rows'][0]['userId']
        memberid = r16.json()['data']['rows'][1]['userId']
        membername = r16.json()['data']['rows'][1]['username']

        print('步骤：转办任务')
        r17 = task_approval_approval(t, approvaluser, memberid, membername, taskname, caseid, '', pkid,
                                     tasktimefrom, tasktimeto)
        assert r17.json()['code'] == '00000000'

        print('步骤：审批中心查询我的审批-获取数据')
        r18 = task_approval_list(t, '1')
        assert r18.json()['code'] == '00000000'

        list = r18.json()['data']['rows']
        dict = {}
        for i in list:
            if i['id'] == "a24f0464b4bda7030cef07834c7f0f93":
                dict = i

        print(dict)
        applydata = dict['applyData']
        applydate = dict['applyDate']
        applyusername = dict['applyUsername']
        approvalusername = dict['approvalUsername']
        isagency = dict['isAgency']
        reason = dict['reason']
        status = dict['status']
        summary = dict['summary']
        type = dict['type']
        urgenum = dict['urgeNum']

        print("步骤：催办任务")
        r19 = task_approval_urge(t, applydata, applydate, applyusername, approvalusername, "a24f0464b4bda7030cef07834c7f0f93", isagency, reason,
                                 status, summary, type, urgenum)
        assert r19.json()['code'] == '00000000'

        print('步骤：审批中心审核拒绝')
        r20 = task_approval_refuse(t, applydata, applydate, applyusername, approvalusername, "a24f0464b4bda7030cef07834c7f0f93", isagency, reason,
                                   status,summary, type, urgenum)
        assert r20.json()['code'] == '00000000'

    @allure.story('新增临时单节点任务-完成')
    def test_task_1(self, get_token_fixture):
        t = get_token_fixture

        #print('步骤：临时任务')
        #r = task_addtemp_temptask(t)
        #assert r.json()['code'] == '00000000'

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        r14 = task_query_fortaskname(t, "temp002")
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        #biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        #biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        #executeuser = r14.json()['data']['rows'][0]['executeUser']
        #ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        #prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        #taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        #updatets = r14.json()['data']['rows'][0]['updateTs']

        print('步骤：完成任务')
        r15 = task_submit(t, attuser, '','', caseid, crtts, crtuser, distype, exetime, '',
                         '', pkid, '', process, taskexecauth, '', tasklevel, taskname, taskstatus,
                          tasktag, tasktimefrom, tasktimeto, tasktype,'')
        assert r15.json()['code'] == '00000000'

    @allure.story('新增临时单节点任务-作废')
    def test_task_1(self, get_token_fixture):
        t = get_token_fixture

        # print('步骤：临时任务')
        # r = task_addtemp_temptask(t)
        # assert r.json()['code'] == '00000000'

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        r14 = task_query_fortaskname(t, "temp005")
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        # biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        # biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        # executeuser = r14.json()['data']['rows'][0]['executeUser']
        # ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        # prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        # taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        # updatets = r14.json()['data']['rows'][0]['updateTs']

        print('步骤：')
        r15 = task_approval_type(t, '2')
        assert r15.json()['code'] == '00000000'

        print('步骤：作废任务')
        r16 = task_cancel(t, attuser, '', '', caseid, crtts, crtuser, distype, exetime,'',
                          '', pkid, '', process, taskexecauth, "temp", tasklevel, taskname, taskstatus,
                          tasktag, tasktimefrom, tasktimeto, tasktype, '')
        assert r16.json()['code'] == '00000000'
'''

if __name__=='__main__':
    pytest.main(['../test_test.py','-s'])
