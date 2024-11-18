import pytest,allure
from lib.task import task_get_model, task_pre_save, task_add, task_saveblock, task_check, task_acceptance, \
    task_publish,task_add_quick,task_publish_quick,task_submit,task_stop,task_del,task_query_theme_task_casedefid,task_get_step,task_get_step_block,\
    task_editblock,task_block_delete,task_block_exchange,task_get_block,task_get_single_step

@allure.epic("任务定制")
@allure.feature("任务操作")
class Test_task:
    @allure.story('新增任务')
    def test_task_create(self,get_token_fixture):
        t=get_token_fixture
        print('步骤一：获取实例id')
        r=task_get_model(t)
        caseid=r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤二：填写任务名称')
        r1=task_pre_save(t,caseid)
        assert r1.json()['code']=='00000000'
        taskname=r1.json()['data']['reTaskDef']['taskName']
        taskid=r1.json()['data']['reTaskDef']['taskId']
        casedefid=r1.json()['data']['caseDefId']

        print('步骤三：任务配置')
        r2 = task_add(t,taskname,caseid,taskid,casedefid)
        assert r2.json()['code'] == '00000000'

    @allure.story('新增任务-审核任务')
    def test_task_check(self,get_token_fixture):
        t=get_token_fixture
        print('步骤一：获取实例id')
        r = task_get_model(t)
        caseid = r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤二：填写任务名称')
        r1 = task_pre_save(t, caseid)
        assert r1.json()['code'] == '00000000'
        taskname = r1.json()['data']['reTaskDef']['taskName']
        taskid = r1.json()['data']['reTaskDef']['taskId']
        casedefid = r1.json()['data']['caseDefId']

        print('步骤三：任务配置')
        r2 = task_add(t, taskname, caseid, taskid, casedefid)
        assert r2.json()['code'] == '00000000'

        print('步骤四：审核任务')
        r4 = task_check(t,taskid)
        assert r4.json()['code'] == '00000000'

    @allure.story('新增任务-审核任务-验收任务')
    def test_task_acceptance(self,get_token_fixture):
        t=get_token_fixture
        print('步骤一：获取实例id')
        r = task_get_model(t)
        caseid = r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤二：填写任务名称')
        r1 = task_pre_save(t, caseid)
        assert r1.json()['code'] == '00000000'
        taskname = r1.json()['data']['reTaskDef']['taskName']
        taskid = r1.json()['data']['reTaskDef']['taskId']
        casedefid = r1.json()['data']['caseDefId']

        print('步骤三：任务配置')
        r2 = task_add(t, taskname, caseid, taskid, casedefid)
        assert r2.json()['code'] == '00000000'

        print('步骤四：审核任务')
        r4 = task_check(t, taskid)
        assert r4.json()['code'] == '00000000'

        print('步骤五：验收任务')
        r5 =task_acceptance(t,taskid)
        assert r5.json()['code'] == '00000000'

    @allure.story('新增任务-审核任务-验收任务-发布任务-完成')
    def test_task_publish(self,get_token_fixture):
        t=get_token_fixture
        print('步骤一：获取实例id')
        r = task_get_model(t)
        caseid = r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤二：填写任务名称')
        r1 = task_pre_save(t, caseid)
        assert r1.json()['code'] == '00000000'
        taskname = r1.json()['data']['reTaskDef']['taskName']
        taskid = r1.json()['data']['reTaskDef']['taskId']
        casedefid = r1.json()['data']['caseDefId']
        crtts = r1.json()['data']['reTaskDef']['crtTs']

        print('步骤三：任务配置')
        r2 = task_add(t, taskname, caseid, taskid, casedefid)
        assert r2.json()['code'] == '00000000'

        print('步骤四：审核任务')
        r4 = task_check(t, taskid)
        assert r4.json()['code'] == '00000000'

        print('步骤五：验收任务')
        r5 = task_acceptance(t, taskid)
        assert r5.json()['code'] == '00000000'

        print('步骤六：发布任务')
        r6 = task_publish(t,casedefid,caseid,taskid,taskname,crtts)
        assert r6.json()['code'] == '00000000'

        print('步骤七：完成任务')
        r7 = task_submit(t,caseid,taskid,taskname,crtts)
        assert r7.json()['code'] == '00000000'

    @allure.story('新增任务-绑定积木-编辑积木-删除积木')
    def test_task_saveblock(self,get_token_fixture):
        t=get_token_fixture
        print('步骤一：获取实例id')
        r = task_get_model(t)
        caseid = r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤二：填写任务名称')
        r1 = task_pre_save(t, caseid)
        assert r1.json()['code'] == '00000000'
        taskname = r1.json()['data']['reTaskDef']['taskName']
        taskid = r1.json()['data']['reTaskDef']['taskId']
        casedefid = r1.json()['data']['caseDefId']

        print('步骤三：任务配置')
        r2 = task_add(t, taskname, caseid, taskid, casedefid)
        assert r2.json()['code'] == '00000000'

        '''
        print('步骤四：获取当前case下所有的step')
        r3 = task_get_step(t,caseid)
        assert r3.json()['code'] == '00000000'
        stepid=r3.json()['data'][0]['stepCode']
'''

        print('步骤四：获取当前case下的step')
        r3 = task_get_single_step(t)
        assert r3.json()['code'] == '00000000'
        stepid = r3.json()['data']

        print('步骤五：获取第一个积木类型下所有的积木块')
        r4 = task_get_block(t,'01')
        assert r4.json()['code'] == '00000000'
        blockcode = r4.json()['data'][0]['blockCode']
        blocktype = r4.json()['data'][0]['blockType']

        print('步骤六：新增积木')
        r5 = task_saveblock(t,stepid,caseid,blocktype,blockcode)
        assert r5.json()['code'] == '00000000'

        print('步骤七：获取当前step下所有的block')
        r6 = task_get_step_block(t, stepid)
        assert r6.json()['code'] == '00000000'
        blockindex = r6.json()['data']['rows'][0]['childBlockIndex']
        blockcodes = r6.json()['data']['rows'][0]['childBlockCode']
        blocktypes = r6.json()['data']['rows'][0]['childBlockType']
        pkid = r6.json()['data']['rows'][0]['pkId']

        print('步骤八：编辑积木')
        r7 = task_editblock(t,stepid,caseid,blocktypes,blockcodes,blockindex,pkid)
        assert r7.json()['code'] == '00000000'

        #print('步骤九：删除积木')
        #r8 = task_block_delete(t,pkid,stepid,blockindex)
        #assert r8.json()['code'] == '00000000'

@allure.feature("任务操作")
class Test_task2:
    @allure.story('快速新增任务-绑定积木-审核任务-验收任务-发布任务-停用-删除')
    def test_task_publish(self, get_token_fixture):
        t = get_token_fixture
        print('步骤一：获取实例id')
        r = task_get_model(t)
        caseid = r.json()['data']
        assert r.json()['code'] == '00000000'

        print('步骤二：快速新增任务')
        r1 = task_add_quick(t, caseid)
        assert r1.json()['code'] == '00000000'
        taskid = r1.json()['data']['taskId']
        # casedefid = r1.json()['data']['caseDefId']
        taskname = r1.json()['data']['taskName']
        crtts = r1.json()['data']['crtTs']
        themeid = r1.json()['data']['themeId']

        print('步骤三：获取快速新增任务的casedefid')
        r2 = task_query_theme_task_casedefid(t, themeid, taskname)
        assert r2.json()['code'] == '00000000'
        casedefid = r2.json()['data']['rows'][0]['caseDefId']

        #print('步骤四：绑定积木')
        #r3 = task_saveblock(t,stepid,caseid,blocktype,blockcode)
        #assert r3.json()['code'] == '00000000'

        print('步骤五：审核任务')
        r4 = task_check(t, taskid)
        assert r4.json()['code'] == '00000000'

        print('步骤六：验收任务')
        r5 = task_acceptance(t, taskid)
        assert r5.json()['code'] == '00000000'

        print('步骤七：发布任务')
        r6 = task_publish_quick(t, casedefid, caseid, taskid, taskname, crtts)
        assert r6.json()['code'] == '00000000'

        print('步骤八：停用任务')
        r7 = task_stop(t, taskid)
        assert r7.json()['code'] == '00000000'

        print('步骤九：删除任务')
        r8 = task_del(t, taskid)
        assert r8.json()['code'] == '00000000'

if __name__=='__main__':
    pytest.main(['../test_file2.py','-s'])

