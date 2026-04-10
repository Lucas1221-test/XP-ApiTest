"""
@Filename:  account_type_management
@Describe:  账户类型管理
@Author:    xuhui.ding
@Time:      2025/3/25 16:15
"""
import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils
from common.yaml_utils import read_yaml1, write_yaml1

"""测试数据路径"""

data_path = data_path + 'test_account_deposit.yaml'


@allure.feature("账户充值")
class Test:

    allure.description("获取余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_balance'))
    def test_get_balance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        global_main_balance = res.json()["data"]["main"]
        data = {"global_main_balance": global_main_balance}
        write_yaml1(data)


    allure.description("充值")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_recharge'))
    def test_recharge(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("cms获取充值id")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_recharge_id'))
    def test_get_recharge_id(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("cms审批充值")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_put_recharge'))
    def test_put_recharge(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    time.sleep(3)
    allure.description("校验充值后的余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_balance'))
    def test_check_balance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        assert float(balance) == float(read_yaml1('global_main_balance')) + int(101)
