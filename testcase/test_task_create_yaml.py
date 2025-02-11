import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml
from hotloads.debug_talk import DebugTalk

"""测试数据路径"""
data_path = data_path + 'task_create.yaml'

@allure.epic("任务定制")
@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-发布")
class Test1:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"]= "api/agnes-ac/v1/ac/case/def/case-body?caseDefId="+read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme_task2'))
    def test_task_query_theme_task2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

        task_status=read_yaml('task_status')
        assert task_status=='03'

@allure.feature("新增单节点岗位任务-绑定积木-上下移动积木顺序-删除积木-删除任务")
class Test2:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_saveblock'))
    def test_task_saveblock2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_step'))
    def test_task_get_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(30)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_step_block'))
    def test_task_get_step_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_block_exchange'))
    def test_task_block_exchange(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_block_delete'))
    def test_task_block_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_del'))
    def test_task_del(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

@allure.feature("新增单节点岗位任务-绑定积木-审核-验收-回退-审核-验收-发布-停用")
class Test3:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_model'))
    def test_task_get_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_pre_save'))
    def test_task_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_save_xcpmodel'))
    def test_task_save_xcpmodel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["xcpInfo"]["body"]["fieldList"] = DebugTalk().set_xcpmodel()
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme'))
    def test_task_query_theme(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_single_step'))
    def test_task_get_single_step(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_frequencyinfo'))
    def test_task_get_frequencyinfo(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_add'))
    def test_task_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["caseDefBody"] = DebugTalk().set_casebody(read_yaml('taskname'),
                                                                              read_yaml('stepcode'))
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_block'))
    def test_task_get_block(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockType"] = '01'
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_saveblock'))
    def test_task_saveblock(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_back'))
    def test_task_back(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_check'))
    def test_task_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_acceptance'))
    def test_task_acceptance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_get_casebody'))
    def test_task_get_casebody(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = "api/agnes-ac/v1/ac/case/def/case-body?caseDefId=" + read_yaml('casedefid')
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme_task'))
    def test_task_query_theme_task(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_publish'))
    def test_task_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_stop'))
    def test_task_stop(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_task_query_theme_task2'))
    def test_task_query_theme_task2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

        task_status = read_yaml('task_status')
        assert task_status == '09'

'''
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_task_theme_save'))
    def test_task_theme_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
'''