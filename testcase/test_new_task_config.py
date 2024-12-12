import random
import time

import allure
import pytest
import yaml

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import read_yaml
from common.files_path import data_path, extract_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'test_task_config.yaml'

@allure.epic("业务配置")
@allure.feature("时间表")
class Test:
#
# 排班管理方案
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notify_save'))
    def test_task_notify_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["planName"] = "自动化通知方案"+str(random.randint(100000,999999))
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_get_notify'))
    def test_task_get_notify(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notifyrule_save'))
    def test_task_notifyrule_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_get_notifyrule'))
    def test_task_get_notifyrule(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notify_get_userlist'))
    def test_task_notify_get_userlist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notify_get_config_fun'))
    def test_task_notify_get_config_fun(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notifyrule_saveemail'))
    def test_task_notifyrule_saveemail(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notifyrule_delete'))
    def test_task_notifyrule_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_notify_delete'))
    def test_task_notify_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_save'))
    def test_task_theme_todo_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["themeName"] = "自动化一级分组"+str(random.randint(100000,999999))
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_gettree'))
    def test_task_theme_todo_gettree(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_getthemeinfo'))
    def test_task_theme_todo_getthemeinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_querytasklistforsave'))
    def test_task_theme_todo_querytasklistforsave(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_savetasklink'))
    def test_task_theme_todo_savetasklink(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_querytasklist'))
    def test_task_theme_todo_querytasklist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_deletetasklink'))
    def test_task_theme_todo_deletetasklink(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_movestep'))
    def test_task_theme_todo_movestep(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_todo_delete'))
    def test_task_theme_todo_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
