"""
@Filename:  td_model
@Describe:  套打模板
@Author:    xuhui.ding
@Time:      2025/3/26 10:58
"""

import json
import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils
from common.yaml_utils import read_yaml, write_yaml
from hotloads.debug_talk import DebugTalk

"""测试数据路径"""

data_path1 = data_path + 'account_management/td_model.yaml'


@allure.epic("增值模块")
@allure.feature("账户管理")
class Test:
    allure.description("套打模板-上传文件")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_td_model_upload'))
    def test_td_model_upload(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取上传文件objectId")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_file_objectId'))
    def test_get_file_objectId(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("新增套打模板")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_add_td_model'))
    def test_add_td_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("新增套打模板后检查")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_add'))
    def test_check_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("编辑套打模板")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_edit_td_model'))
    def test_edit_td_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("编辑套打模板后检查")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_edit'))
    def test_check_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("删除套打模板")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_delete_td_model'))
    def test_delete_td_model(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("删除套打模板后检查")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_delete'))
    def test_check_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)