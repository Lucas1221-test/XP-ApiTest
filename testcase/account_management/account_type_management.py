"""
@Filename:  account_type_management
@Describe:  账户类型管理
@Author:    xuhui.ding
@Time:      2025/3/25 16:15
"""
import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils

"""测试数据路径"""

data_path = data_path + 'account_management/account_type_management.yaml'

@allure.epic("增值模块")
@allure.feature("账户管理")
class Test:
    allure.description("获取结构信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_jg_info'))
    def test_get_jg_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("新增账户类型")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_account_type_management'))
    def test_add_account_type_management(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("新增账户类型后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_add'))
    def test_check_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("编辑账户类型")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_edit_account_type_management'))
    def test_edit_account_type_management(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("编辑账户类型后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_edit'))
    def test_check_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # allure.description("删除账户类型")
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_delete_account_type_management'))
    # def test_delete_account_type_management(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)
    #
    # allure.description("删除账户类型后校验")
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_check_delete'))
    # def test_check_delete(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)