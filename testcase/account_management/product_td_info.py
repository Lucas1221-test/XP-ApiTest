"""
@Filename:  product_td_info
@Describe:  产品套打信息
@Author:    xuhui.ding
@Time:      2025/3/26 13:51
"""

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils

"""测试数据路径"""

data_path1 = data_path + 'account_management/product_td_info.yaml'


@allure.epic("增值模块")
@allure.feature("账户管理")
class Test:
    allure.description("获取受托人信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_str_info'))
    def test_get_str_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取托管行信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_tgh_info'))
    def test_get_tgh_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取代理人/托管人信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_dlr_info'))
    def test_get_dlr_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("新增产品套打信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_add_product_td_info'))
    def test_add_product_td_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("新增产品套打信息后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_add'))
    def test_check_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("编辑产品套打信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_edit_product_td_info'))
    def test_edit_product_td_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("编辑产品套打信息后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_edit'))
    def test_check_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    allure.description("删除产品套打信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_delete_product_td_info'))
    def test_delete_product_td_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("删除产品套打信息后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_delete'))
    def test_check_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)