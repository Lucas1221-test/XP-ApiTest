"""
@Filename:  exception
@Describe:  特殊场景：取消比赛、回滚结算
@Author:    lucas
@Time:      2026/4/3 14:15
"""
import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils
from common.yaml_utils import read_yaml, write_yaml

"""测试数据路径"""
data_path1 = data_path + 'test_account_deposit.yaml'
data_path2 = data_path + 'test_exception.yaml'
data_path = data_path + 'test_gotobet.yaml'


@allure.feature("取消比赛")
class Test:
    allure.description("获取篮球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                            'test_get_basketball_info'))
    def test_get_basketball_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_balance'))
    def test_get_balance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_go_to_bet'))
    def test_go_to_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取下单信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_order_info'))
    def test_get_order_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].stake_amount"] = '100'
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("下注后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_after_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        new_total_balance = res.json()["data"]["total"]
        data = {"new_total_balance": new_total_balance}
        write_yaml(data)
        assert float(balance) == float(read_yaml('main_balance')) - int(read_yaml("stake_amount"))



    allure.description("取消比赛")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                            'test_cancel_match'))
    def test_cancel_match(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("同步比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_sync_bet_result'))
    def test_sync_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("查看bet历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_history'))
    def test_get_bet_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()["data"]["list"]
        for i in res:
            if i['bet_id'] == read_yaml("bet_id"):
                assert i['status_text'] == "void"
                assert i['main_bet_amount'] == read_yaml("stake_amount")
                assert i["selections"][0]["sport_name"] == "Basketball"

    allure.description("查看transactions历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].amount"] = int(read_yaml("stake_amount"))
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(3)
    allure.description("取消比赛后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_after_bet1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('取消比赛后检查余额')
        res = RequestUtils().standard_yaml_case(caseinfo)
        new_total_balance = res.json()["data"]["total"]
        assert float(new_total_balance) == float(read_yaml("total_balance"))


    allure.description("回滚取消")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                            'test_rollback_cancel'))
    def test_rollback_cancel(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("同步比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_sync_bet_result'))
    def test_sync_bet_result1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(3)
    allure.description("回滚取消后查看订单")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_get_settled'))
    def test_check_after_bet2(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('回滚取消后检查余额')
        res = RequestUtils().standard_yaml_case(caseinfo)
        lists = res.json()["data"]["list"]
        for i in lists:
            if i["bet_id"] == read_yaml("bet_id"):
                assert i["stake_amount"] == read_yaml("stake_amount")
                assert i["status"] == 3



    allure.description("取消比赛")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                            'test_cancel_match'))
    def test_cancel_match1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("同步比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_sync_bet_result'))
    def test_sync_bet_result3(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


@allure.feature("回滚结算")
class Test1:
    allure.description("获取篮球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                            'test_get_basketball_info1'))
    def test_get_basketball_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_balance'))
    def test_get_balance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_go_to_bet'))
    def test_go_to_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("获取下单信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_order_info'))
    def test_get_order_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].stake_amount"] = '100'
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("下注后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_after_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        new_total_balance = res.json()["data"]["total"]
        data = {"new_total_balance": new_total_balance}
        write_yaml(data)
        assert float(balance) == float(read_yaml('main_balance')) - int(read_yaml("stake_amount"))

    allure.description("公布比赛结果/输")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_bet_result'))
    def test_get_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("同步比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_sync_bet_result'))
    def test_sync_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("查看比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_get_settled'))
    def test_get_settled(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        lists = res.json()["data"]["list"]
        for i in lists:
            if i["bet_id"] == read_yaml("bet_id"):
                assert i["status"] == 2



    allure.description("回滚比赛")

    @pytest.mark.parametrize("caseinfo", read_case_yaml(data_path2, 'test_rollback_settlement'))
    def test_rollback_settlement(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("同步比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_sync_bet_result'))
    def test_sync_bet_result1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("查看比赛结果")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path2,
                                            'test_get_settled'))
    def test_get_settled1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        lists = res.json()["data"]["list"]
        expected_bet_id = read_yaml("bet_id")
        for i in lists:
            assert i["bet_id"] != expected_bet_id, f"bet_id {i['bet_id']} should not equal {expected_bet_id}"


    allure.description("查看bet历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_history'))
    def test_get_bet_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()["data"]["list"]
        for i in res:
            if i['bet_id'] == read_yaml("bet_id"):
                assert i['status_text'] == "pending"
                assert i['main_bet_amount'] == read_yaml("stake_amount")
                assert i["selections"][0]["sport_name"] == "Basketball"

    allure.description("查看transactions历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].amount"] = -int(read_yaml("stake_amount"))
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("公布比赛结果后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_after_bet1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        new_total_balance = res.json()["data"]["total"]
        assert float(new_total_balance) == float(read_yaml("total_balance")) - float(read_yaml("stake_amount"))

