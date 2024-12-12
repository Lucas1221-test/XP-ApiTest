import pytest,allure

from lib.task_config import task_theme_todo_save,task_theme_todo_savetasklink,task_theme_todo_deletetasklink,\
    task_theme_todo_movestep,task_theme_todo_delete,task_theme_todo_gettree,task_theme_todo_querytasklist,task_theme_todo_querytasklistforsave
from lib.task_config import task_notify_save,task_get_notify,task_notify_get_config_fun,task_notifyrule_save,\
    task_get_notifyrule,task_notify_get_userlist,task_notify_delete,task_notifyrule_delete,task_notifyrule_saveemail

from lib.task_config import task_post_config_list,task_post_get_config_fun,task_info_save,task_info_get,task_info_delete,task_theme_todo_getthemeinfo

task_get_notify
@allure.feature("任务中心定义")
class Test_task_center_config:
    @allure.story('新增一级分组-关联任务-删除关联任务-上移分组-删除分组')
    def test_task_center_config(self,get_token_fixture):
        t=get_token_fixture

        print('步骤：新增一级分组（任务实例）')
        r = task_theme_todo_save(t,'00')
        assert r.json()['code'] == '00000000'

        print('步骤：查询分组列表，获取分组的basepath,themepkid,themepkname')
        r1 = task_theme_todo_gettree(t)
        assert r1.json()['code'] == '00000000'
        themepkid=r1.json()['data'][-1]['pkId']
        themepkname=r1.json()['data'][-1]['themeName']
        basepath=r1.json()['data'][-1]['basePath']
        parentthemeid = r1.json()['data'][-1]['parentThemeId']

        print('步骤：查询任务主题列表,获取themeid')
        r11 = task_theme_todo_getthemeinfo(t)
        assert r11.json()['code'] == '00000000'
        themeid = r11.json()['data'][-1]['themeId']

        print('步骤：查询任务列表,通过特定任务主题，获取关联任务的taskidlist')
        r2 = task_theme_todo_querytasklistforsave(t,themeid)
        assert r2.json()['code'] == '00000000'
        data = r2.json()['data']
        taskidlist = []
        for i in data:
            taskidlist.append(i['taskDefId'])

        print('步骤：关联任务')
        r3 = task_theme_todo_savetasklink(t,themepkid,themepkname,themeid,taskidlist,)
        assert r3.json()['code'] == '00000000'

        print('步骤：查询关联任务列表,获取关联任务的pkidlist')
        r4 = task_theme_todo_querytasklist(t,themepkid,basepath)
        assert r4.json()['code'] == '00000000'
        list=r4.json()['data']
        pkidlist=[]
        for i in list:
            pkidlist.append(i['pkId'])

        print('步骤：删除关联任务')
        r5 = task_theme_todo_deletetasklink(t,pkidlist)
        assert r5.json()['code'] == '00000000'

        print('步骤：上移/下移分组')
        r6 = task_theme_todo_movestep(t,themepkid,parentthemeid,'01')
        assert r6.json()['code'] == '00000000'

        print('步骤：删除分组')
        r7 = task_theme_todo_delete(t,themepkid)
        assert r7.json()['code'] == '00000000'

@allure.feature("任务通知方案")
class Test_task_notify:
    @allure.story('新增通知方案-新增通知规则-新增通知方式-删除通知规则-删除通知方案')
    def test_task_notify(self,get_token_fixture):
        t=get_token_fixture

        print('步骤：新增通知方案（产品任务）')
        r =task_notify_save(t,'1')
        assert r.json()['code'] == '00000000'

        print('步骤：查询通知方案，获取configid')
        r1 =task_get_notify(t)
        assert r1.json()['code'] == '00000000'
        configid = r1.json()['data'][0]['configId']

        print('步骤：查询通知对象，获取notifyrule')
        r2 = task_notify_get_config_fun(t)
        assert r2.json()['code'] == '00000000'
        notifyrule = r2.json()['data'][0]['fnId']

        print('步骤：新增通知规则')
        r3 = task_notifyrule_save(t,configid,notifyrule)
        assert r3.json()['code'] == '00000000'

        print('步骤：获取用户列表userid、username')
        r4 =task_notify_get_userlist(t)
        assert r4.json()['code'] == '00000000'
        username = r4.json()['data']['rows'][0]['userName']
        userid = r4.json()['data']['rows'][0]['userId']

        print('步骤：查询通知规则,获取通知规则的pkid')
        r5 = task_get_notifyrule(t,configid)
        assert r5.json()['code'] == '00000000'
        pkid = r5.json()['data'][0]['pkId']

        print('步骤：新增通知方式-邮件')
        r6 = task_notifyrule_saveemail(t, pkid, userid, username)
        assert r6.json()['code'] == '00000000'

        print('步骤：删除通知规则')
        r7 = task_notifyrule_delete(t,pkid)
        assert r7.json()['code'] == '00000000'

        print('步骤：删除通知方案（pkid是通知方案的configid）')
        r8 =task_notify_delete(t,configid)
        assert r8.json()['code'] == '00000000'

@allure.feature("任务分配方案")
class Test_task_apply:
    @allure.story('新增任务分配方案-删除任务分配方案')
    def test_task_apply(self,get_token_fixture):
        t=get_token_fixture

        print('步骤：查询产品任务("1")的任务配置列表,获取tasklist')
        r =task_post_config_list(t,'1')
        assert r.json()['code'] == '00000000'
        tasklist = r.json()['data']

        print('步骤：查询通知对象，获取fnid(customrule)')
        r1 = task_post_get_config_fun(t)
        assert r1.json()['code'] == '00000000'
        customrule = r1.json()['data'][0]['fnId']

        print('步骤：新增任务分配方案:产品任务-"1"，岗位任务-"2"')
        r2 = task_info_save(t,'1',customrule,tasklist)
        assert r2.json()['code'] == '00000000'

        print('步骤：查询任务分配方案列表，获取方案的pkid')
        r3 = task_info_get(t)
        assert r3.json()['code'] == '00000000'
        pkid = r3.json()['data'][0]['pkId']

        print('步骤：删除分配方案')
        r4 = task_info_delete(t,pkid)
        assert r4.json()['code'] == '00000000'

if __name__=='__main__':
    pytest.main(['../test_task_config.py','-s'])