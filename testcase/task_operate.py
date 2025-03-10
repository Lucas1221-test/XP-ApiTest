import time

import pytest,allure
from lib.task_operate import task_get_model, task_pre_save, task_add, task_saveblock, task_check, task_acceptance, \
    task_publish, task_submit, task_stop, task_del, \
    task_get_step, task_get_step_block, task_block_delete, task_block_exchange, task_get_block, task_get_single_step, \
    task_query_theme, task_get_frequencyinfo, task_back, task_cancel
from lib.task_operate import task_topping,task_cancelTopping,task_query_fortaskname,task_submit,task_approval_type,task_get_memberlist,task_approval_approval,task_approval_delay,task_query_1,task_query_2,task_query_3,task_query_4,task_query_5,task_query_task
from lib.task_operate import task_query_6,task_get_breif,task_get_breif_execlog,task_get_breif_exec,task_get_breif_confirm,task_get_breif_confirm_update,task_get_breif_edit_planendtime
from lib.task_operate import task_approval_list,task_approval_pass,task_approval_refuse,task_approval_urge,task_handover_get_doc
from lib.task_operate import task_save_xcpmodel,task_get_casebody,task_query_theme_task
import json

@allure.feature("任务定制")
class Test_task_create:
    @allure.story('新增单节点岗位任务-绑定积木-审核-验收-发布')
    #@pytest.mark.repeat(10000)
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
        r7 = task_get_block(t, '01')
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

    @allure.story('新增单节点岗位任务-绑定积木-上下移动积木顺序-删除积木-删除任务')
    def test_task_2(self, get_token_fixture):
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

        print('步骤：获取第一个积木类型下所有的积木块')
        r7 = task_get_block(t, '01')
        assert r7.json()['code'] == '00000000'
        blockcode1 = r7.json()['data'][0]['blockCode']
        blocktype1 = r7.json()['data'][0]['blockType']
        blockcode2 = r7.json()['data'][1]['blockCode']
        blocktype2 = r7.json()['data'][0]['blockType']

        print('步骤：新增积木')
        r8 = task_saveblock(t, stepcode, caseid, blocktype1, blockcode1)
        assert r8.json()['code'] == '00000000'

        print('步骤：新增积木')
        r81 = task_saveblock(t, stepcode, caseid, blocktype2, blockcode2)
        assert r81.json()['code'] == '00000000'

        print('步骤：获取场景任务下所有的step(获取stepid)')
        r9 = task_get_step(t, caseid)
        assert r9.json()['code'] == '00000000'
        stepid = r9.json()['data'][0]['stepCode']

        print('步骤：获取当前step下所有的block')
        r10 = task_get_step_block(t, stepid)
        assert r10.json()['code'] == '00000000'
        blockindex = r10.json()['data']['rows'][0]['childBlockIndex']
        pkid = r10.json()['data']['rows'][0]['pkId']

        print("上下移动积木")
        r101=task_block_exchange(t,stepid)
        assert r101.json()['code'] == '00000000'

        print('步骤：删除积木')
        r11 = task_block_delete(t, pkid, stepid, blockindex)
        assert r11.json()['code'] == '00000000'

        print('步骤：删除任务')
        r12 = task_del(t, taskid)
        assert r12.json()['code'] == '00000000'

    @allure.story('新增单节点岗位任务-绑定积木-审核-验收-回退-审核-验收-发布-停用')
    def test_task_3(self, get_token_fixture):
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
        r7 = task_get_block(t, '01')
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

        print('步骤：回退')
        r11 = task_back(t, taskid)
        assert r11.json()['code'] == '00000000'

        print('步骤：审核任务')
        r12 = task_check(t, taskid)
        assert r12.json()['code'] == '00000000'

        print('步骤：验收任务')
        r13 = task_acceptance(t, taskid)
        assert r13.json()['code'] == '00000000'

        print('步骤：查询任务的casebody')
        r14 = task_get_casebody(t, casedefid)
        assert r14.json()['code'] == '00000000'
        casebody = r14.json()['data']['caseDefBody']

        print('步骤：查询任务主题下的任务列表，获取相关参数')
        r15 = task_query_theme_task(t, themeid)
        assert r15.json()['code'] == '00000000'

        # actionparam=r15.json()['data']['rows'][0]['reTaskDef']['actionParam']
        # biztag = r15.json()['data']['rows'][0]['reTaskDef']['bizTag']
        crtts = r15.json()['data']['rows'][0]['reTaskDef']['crtTs']
        crtuser = r15.json()['data']['rows'][0]['reTaskDef']['crtUser']
        updatets = r15.json()['data']['rows'][0]['reTaskDef']['updateTs']
        updateuser = r15.json()['data']['rows'][0]['reTaskDef']['updateUser']
        # tasktitle= r15.json()['data']['rows'][0]['reTaskDef']['taskTitle']
        # zruser= r15.json()['data']['rows'][0]['reTaskDef']['zrUser']

        print('步骤：发布任务')
        r16 = task_publish(t, canfb, canht, cansc, canset, cansh, canty, canys, casedefid, caseid, casetype, crtts,
                           crtuser, distype, funcid, taskid, taskname, taskinitdays, themeid, themename, updatets,
                           updateuser, casebody)
        assert r16.json()['code'] == '00000000'

        print('步骤：停用任务')
        r17 = task_stop(t, taskid)
        assert r17.json()['code'] == '00000000'

@allure.feature("任务明细查询")
class Test_task_detail:
    @allure.story('查询我的任务-查询中心任务-查询全部任务')
    def test_task_detail1(self,get_token_fixture):
        t=get_token_fixture

        print('步骤：查询我的任务')
        r = task_query_6(t,1,'')
        assert r.json()['code'] == '00000000'

        print('步骤：查询中心任务')
        r1 = task_query_6(t, 2,'')
        assert r1.json()['code'] == '00000000'

        print('步骤：查询全部任务')
        r2 = task_query_6(t, 3,'')
        assert r2.json()['code'] == '00000000'

    @allure.story('任务定制发布任务-任务明细查询我的任务-查询任务详情-详情查看执行记录-重新执行-修改结束时间-手工确认')
    def test_task_detail2(self, get_token_fixture):
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
        r7 = task_get_block(t, '01')
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

        print('步骤：任务明细查询我的任务')
        r14 = task_query_6(t, 1,taskname)
        assert r14.json()['code'] == '00000000'
        taskexecid=r14.json()['data']['rows'][0]['pkId']

        print('步骤：查看任务详情')
        r15 = task_get_breif(t, taskexecid)
        assert r15.json()['code'] == '00000000'
        data = r15.json()['data']
        data = json.loads(data)

        stepcode = data["caseSteps"][0]['stepCode']
        stepexecid = data["caseSteps"][0]['stepExecId']
        jobid = data["caseSteps"][0]['jobId']
        stepstatus = data["caseSteps"][0]['stepStatus']
        taskid_breif = data["caseSteps"][0]['taskId']
        caseid_breif = data["caseSteps"][0]['caseId']

        print('步骤：查看任务详情-查询执行记录')
        r16 = task_get_breif_execlog(t, stepexecid)
        assert r16.json()['code'] == '00000000'

        print('步骤：查看任务详情-重新执行')
        r17 = task_get_breif_exec(t, caseid_breif, stepcode, taskid_breif)
        assert r17.json()['code'] == '00000000'

        print('步骤：查看任务详情-修改结束时间')
        r18 = task_get_breif_edit_planendtime(t, stepexecid)
        #assert r18.json()['code'] == '00000000'

        print('步骤：查看任务详情-手工确认-更新状态')
        r181 = task_get_breif_confirm_update(t,stepstatus,jobid,stepcode,caseid,stepexecid)
        # assert r181.json()['code'] == '00000000'

        print('步骤：查看任务详情-手工确认')
        r19 = task_get_breif_confirm(t, stepstatus, jobid, stepcode, caseid_breif, stepexecid, taskid_breif)
        assert r19.json()['code'] == '00000000'


@allure.feature("审批中心")
class Test_task_approval:
    @allure.story('查询任务-催办-通过')
    def test_task_approval(self,get_token_fixture):
        t = get_token_fixture

        print('步骤：查询我的审批：1')
        r = task_approval_list(t,"1")
        assert r.json()['code'] == '00000000'

        applydata = r.json()['data']['rows'][0]['applyData']
        applydate = r.json()['data']['rows'][0]['applyDate']
        applyusername = r.json()['data']['rows'][0]['applyUsername']
        approvalusername= r.json()['data']['rows'][0]['approvalUsername']
        id= r.json()['data']['rows'][0]['id']
        isagency = r.json()['data']['rows'][0]['isAgency']
        reason = r.json()['data']['rows'][0]['reason']
        status = r.json()['data']['rows'][0]['status']
        summary = r.json()['data']['rows'][0]['summary']
        type = r.json()['data']['rows'][0]['type']
        urgenum = r.json()['data']['rows'][0]['urgeNum']

        print('步骤：查询我的发起：2')
        r1 = task_approval_list(t, "2")
        assert r1.json()['code'] == '00000000'

        print('步骤：催办')
        r2 = task_approval_urge(t,applydata,applydate, applyusername, approvalusername, id, isagency, reason, status,
                                summary, type, urgenum)
        assert r2.json()['code'] == '00000000'

        print('步骤：通过')
        r3 = task_approval_pass(t,applydata,applydate,applyusername,approvalusername,id,isagency,reason,status,summary,type,urgenum)
        assert r3.json()['code'] == '00000000'

    @allure.story('查询任务-拒绝')
    def test_task_approval2(self, get_token_fixture):
        t = get_token_fixture

        print('步骤：查询我的审批：1')
        r = task_approval_list(t, "1")
        assert r.json()['code'] == '00000000'

        applydata = r.json()['data']['rows'][0]['applyData']
        applydate = r.json()['data']['rows'][0]['applyDate']
        applyusername = r.json()['data']['rows'][0]['applyUsername']
        approvalusername = r.json()['data']['rows'][0]['approvalUsername']
        id = r.json()['data']['rows'][0]['id']
        isagency = r.json()['data']['rows'][0]['isAgency']
        reason = r.json()['data']['rows'][0]['reason']
        status = r.json()['data']['rows'][0]['status']
        summary = r.json()['data']['rows'][0]['summary']
        type = r.json()['data']['rows'][0]['type']
        urgenum = r.json()['data']['rows'][0]['urgeNum']

        print('步骤：拒绝')
        r1 = task_approval_refuse(t, applydata, applydate, applyusername, approvalusername, id, isagency, reason, status,
                                summary, type, urgenum)
        assert r1.json()['code'] == '00000000'


@allure.feature("任务中心")
class Test_task_center:
    @allure.story('查询今日必办-置顶-取消置顶-查询超时任务-查询今日异常-查询可提前办-查询我的分布-查询仅待办-查询仅转交-查询仅协作')
    def test_task_center1(self,get_token_fixture):
        t = get_token_fixture

        print('步骤：查询今日必办，获取当前列表数据')
        r = task_query_1(t)
        assert r.json()['code'] == '00000000'
        taskid=r.json()['data']['rows'][-1]['taskId']

        print('步骤：置顶')
        r1 =task_topping(t,taskid)
        assert r1.json()['code'] == '00000000'

        print('步骤：取消置顶')
        r2 = task_cancelTopping(t,taskid)
        assert r2.json()['code'] == '00000000'

        print('步骤：查询超时任务')
        r4 = task_query_2(t)
        assert r4.json()['code'] == '00000000'

        print('步骤：查询今日异常')
        r5 = task_query_3(t)
        assert r5.json()['code'] == '00000000'

        print('步骤：查询可提前办')
        r6 = task_query_4(t)
        assert r6.json()['code'] == '00000000'

        print('步骤：查询我的发布')
        r7 = task_query_5(t)
        assert r7.json()['code'] == '00000000'

        print('步骤：查询仅待办')
        r8 = task_query_task(t,'01')
        assert r8.json()['code'] == '00000000'

        print('步骤：查询仅转交')
        r9 = task_query_task(t, '02')
        assert r9.json()['code'] == '00000000'

        print('步骤：查询仅协作')
        r10 = task_query_task(t, '03')
        assert r10.json()['code'] == '00000000'

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
        r7 = task_get_block(t, '01')
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

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        time.sleep(120)
        r14=task_query_fortaskname(t,taskname)
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        executeuser = r14.json()['data']['rows'][0]['executeUser']
        ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        updatets = r14.json()['data']['rows'][0]['updateTs']

        print('步骤：完成任务')
        r15 = task_submit(t,attuser,biztimefrom,biztimeto,caseid,crtts,crtuser,distype,exetime,executeuser,ispending,pkid,prdtinfo,process,taskexecauth,taskid,tasklevel,taskname,taskstatus,tasktag,tasktimefrom,tasktimeto,tasktype,updatets)
        assert r15.json()['code'] == '00000000'

    @allure.story('新增单节点岗位任务-绑定积木-审核-验收-发布-作废')
    def test_task_2(self, get_token_fixture):
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
        r7 = task_get_block(t, '01')
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

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        time.sleep(120)
        r14 = task_query_fortaskname(t, taskname)
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        executeuser = r14.json()['data']['rows'][0]['executeUser']
        ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        updatets = r14.json()['data']['rows'][0]['updateTs']

        print('步骤：')
        r15 =task_approval_type(t,'2')
        assert r15.json()['code'] == '00000000'

        print('步骤：作废任务')
        r16 = task_cancel(t,attuser,biztimefrom,biztimeto,caseid,crtts,crtuser,distype,exetime,executeuser,ispending,pkid,prdtinfo,process,taskexecauth,taskid,tasklevel,taskname,taskstatus,tasktag,tasktimefrom,tasktimeto,tasktype,updatets)
        assert r16.json()['code'] == '00000000'

    @allure.story('新增单节点岗位任务-绑定积木-审核-验收-发布-延期-通过')
    def test_task_3(self, get_token_fixture):

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
        r7 = task_get_block(t, '01')
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

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        time.sleep(120)
        r14 = task_query_fortaskname(t, taskname)
        assert r14.json()['code'] == '00000000'
        attuser = r14.json()['data']['rows'][0]['attUser']
        biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        executeuser = r14.json()['data']['rows'][0]['executeUser']
        ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        updatets = r14.json()['data']['rows'][0]['updateTs']

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
        r17 = task_approval_delay(t,'agnes',taskname,caseid,tasktimefrom,tasktimeto)
        assert r17.json()['code'] == '00000000'

        print('步骤：审批中心查询我的审批-获取数据')
        r18 = task_approval_list(t, '1')
        assert r18.json()['code'] == '00000000'

        list = r18.json()['data']['rows']
        dict={}
        for i in list:
            if caseid in  i['applyData']:
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
        idd=dict['id']

        print('步骤：审批中心审核通过')
        r20 = task_approval_pass(t, applydata, applydate, applyusername, approvalusername, idd, isagency, reason, status,
                                 summary, type, urgenum)
        assert r20.json()['code'] == '00000000'

    @allure.story('新增单节点岗位任务-绑定积木-审核-验收-发布-转办-拒绝')
    def test_task_4(self, get_token_fixture):
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
        r7 = task_get_block(t, '01')
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

        print('步骤：查询仅待办下特定名称的任务，获取相关参数')
        time.sleep(120)
        r14 = task_query_fortaskname(t, taskname)
        assert r14.json()['code'] == '00000000'
        print(r14.json()['data']['rows'])
        attuser = r14.json()['data']['rows'][0]['attUser']
        biztimefrom = r14.json()['data']['rows'][0]['bizTimeFrom']
        biztimeto = r14.json()['data']['rows'][0]['bizTimeTo']
        caseid = r14.json()['data']['rows'][0]['caseId']
        crtts = r14.json()['data']['rows'][0]['crtTs']
        crtuser = r14.json()['data']['rows'][0]['crtUser']
        distype = r14.json()['data']['rows'][0]['disType']
        exetime = r14.json()['data']['rows'][0]['exeTime']
        executeuser = r14.json()['data']['rows'][0]['executeUser']
        ispending = r14.json()['data']['rows'][0]['isPending']
        pkid = r14.json()['data']['rows'][0]['pkId']
        prdtinfo = r14.json()['data']['rows'][0]['prdtInfo']
        process = r14.json()['data']['rows'][0]['process']
        taskexecauth = r14.json()['data']['rows'][0]['taskExecAuth']
        taskid = r14.json()['data']['rows'][0]['taskId']
        pkid = r14.json()['data']['rows'][0]['pkId']
        tasklevel = r14.json()['data']['rows'][0]['taskLevel']
        taskname = r14.json()['data']['rows'][0]['taskName']
        taskstatus = r14.json()['data']['rows'][0]['taskStatus']
        tasktag = r14.json()['data']['rows'][0]['taskTag']
        tasktimefrom = r14.json()['data']['rows'][0]['taskTimeFrom']
        tasktimeto = r14.json()['data']['rows'][0]['taskTimeTo']
        tasktype = r14.json()['data']['rows'][0]['taskType']
        updatets = r14.json()['data']['rows'][0]['updateTs']

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
        r17 = task_approval_approval(t,'agnes',memberid,membername,taskname,caseid,taskid,pkid,tasktimefrom,tasktimeto)
        assert r17.json()['code'] == '00000000'

        print('步骤：审批中心查询我的审批-获取数据')
        r18 = task_approval_list(t, '1')
        assert r18.json()['code'] == '00000000'

        list = r18.json()['data']['rows']
        dict={}
        for i in list:
            if caseid in i['applyData']:
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
        idd=dict['id']

        print('步骤：审批中心审核拒绝')
        r20 = task_approval_refuse(t, applydata, applydate, applyusername, approvalusername, idd, isagency, reason,
                                 status,
                                 summary, type, urgenum)
        assert r20.json()['code'] == '00000000'


if __name__=='__main__':
    pytest.main(['../task_operate.py','-s'])

