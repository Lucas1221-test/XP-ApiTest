"""
@Filename:  account_information_management
@Describe:  账户信息管理
@Author:    xuhui.ding
@Time:      2025/3/25 17:06
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

data_path1 = data_path + 'account_management/account_information_management.yaml'


@allure.epic("增值模块")
@allure.feature("账户管理")
class Test:
    allure.description("获取产品信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_product_info'))
    def test_get_product_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["params"]["_t"] =  int(time.time())
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取账户类型")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_account_type_info'))
    def test_get_account_type_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取外部机构简称")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_wbjg_info'))
    def test_get_wbjg_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
        RelatedDept1 =  read_yaml("RelatedDept")
        RelatedDept1 = json.loads(RelatedDept1)
        RelatedDept1 = RelatedDept1[0]
        data = {"RelatedDept1": RelatedDept1}
        write_yaml(data)

    allure.description("获取套打模板")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_td_template'))
    def test_get_td_template(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取objectId")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_objectId'))
    def test_get_objectId(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("账户登记-上传开户材料")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_account_registration_upload'))
    def test_account_registration_upload(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("账户登记")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_account_registration'))
    def test_account_registration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("账户登记后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_view_details'))
    def test_view_details(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        data = res.json()["data"]["rows"]
        print(data)
        new_data = []
        for i in data:
            if i.get("baseDesc") == "自动化测试-账户登记":
                new_data.append(i)

        acct_pkId = new_data[0]["pkId"]
        acctId = new_data[0]["acctId"]

        data = {"acct_pkId": acct_pkId, "acctId": acctId}
        write_yaml(data)


    allure.description("查看账户登记详情")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_query_account_info'))
    def test_query_account_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("查看历史")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_query_history'))
    def test_query_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取objectId")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_objectId1'))
    def test_get_objectId1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # allure.description("变更账户信息")
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path1,
    #                         'test_change_account_info'))
    # def test_change_account_info(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)

    allure.description("删除账户类型")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_delete_account_type_management'))
    def test_delete_account_type_management(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("删除账户类型后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_delete'))
    def test_check_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)