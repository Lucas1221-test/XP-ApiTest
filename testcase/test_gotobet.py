"""
@Filename:  account_type_management
@Describe:  账户类型管理
@Author:    xuhui.ding
@Time:      2025/3/25 16:15
"""
import math
import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils
from common.yaml_utils import read_yaml, write_yaml

"""测试数据路径"""
data_path1 = data_path + 'test_account_deposit.yaml'
data_path = data_path + 'test_gotobet.yaml'


@allure.feature("篮球bet-lose")
class Test:
    allure.description("获取篮球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
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
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注后检查余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_balance'))
    def test_check_balance_after_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        assert float(balance) == float(read_yaml('main_balance')) - int(100)

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
                assert i['status_text'] == "lose"
                assert i['stake_amount'] == '100'
                assert i["selections"][0]["sport_name"] == "Basketball"

    allure.description("查看transactions历史")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


@allure.feature("篮球bet-win")
class Test1:
    allure.description("获取篮球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_basketball_info1'))
    def test_get_basketball_info1(self, caseinfo):
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
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注后检查余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_balance'))
    def test_check_balance_after_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        assert float(balance) == float(read_yaml('main_balance')) - int(100)

    allure.description("公布比赛结果/赢")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_bet_result'))
    def test_get_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["outcomes"]["Market"][0]["outcome"][0]["result"] = '1'
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
                assert i['status_text'] == "win"
                assert i['stake_amount'] == '100'
                assert i["selections"][0]["sport_name"] == "Basketball"

    allure.description("查看transactions历史")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].amount"] = round(100 * read_yaml("outcome_value"), 4)
        RequestUtils().standard_yaml_case(caseinfo)


@allure.feature("足球bet-lose")
class Test2:
    allure.description("获取足球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_soccer_info'))
    def test_get_soccer_info(self, caseinfo):
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
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注后检查余额")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_balance'))
    def test_check_balance_after_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        assert float(balance) == float(read_yaml('main_balance')) - int(100)

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
            if ['bet_id'] == read_yaml("bet_id"):
                assert i['status_text'] == "lose"
                assert i['stake_amount'] == '100'
                assert i["selections"][0]["sport_name"] == "Soccer"


    allure.description("查看transactions历史")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


@allure.feature("足球bet-win")
class Test3:
    allure.description("获取足球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_soccer_info1'))
    def test_get_soccer_info1(self, caseinfo):
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
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_balance_after_bet(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        balance = res.json()["data"]["main"]
        assert float(balance) == float(read_yaml('main_balance')) - int(100)

    allure.description("公布比赛结果/赢")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_result'))
    def test_get_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["outcomes"]["Market"][0]["outcome"][0]["result"] = '1'
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
                assert i['status_text'] == "win"
                assert i['stake_amount'] == '100'
                assert i["selections"][0]["sport_name"] == "Soccer"

    allure.description("查看transactions历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].amount"] = round(100 * read_yaml("outcome_value"), 4)
        RequestUtils().standard_yaml_case(caseinfo)


@allure.feature("篮球/足球串关-win")
class Test4:

    allure.description("获取余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_get_balance'))
    def test_get_balance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取篮球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_basketball_info1'))
    def test_get_basketball_info1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取足球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_soccer_info_parlay'))
    def test_get_soccer_info_parlay(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_go_to_bet_parlay'))
    def test_go_to_bet_parlay(self, caseinfo):
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
        total_balance = res.json()["data"]["total"]
        data = {"total_balance": total_balance}
        write_yaml(data)
        assert float(balance) == float(read_yaml('main_balance')) - int(read_yaml("stake_amount"))

    allure.description("公布篮球比赛结果/赢")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_result'))
    def test_get_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["outcomes"]["Market"][0]["outcome"][0]["result"] = '1'
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("公布足球比赛结果/赢")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_result_1'))
    def test_get_bet_result_1(self, caseinfo):
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
                assert i['status_text'] == "win"
                assert i['stake_amount'] == read_yaml("stake_amount")
                assert i["selections"][0]["sport_name"] == "Basketball"
                assert i["selections"][1]["sport_name"] == "Soccer"

    allure.description("查看transactions历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].amount"] = round(int(read_yaml("stake_amount")) * read_yaml("outcome_value") * read_yaml("soccer_outcome_value"), 4)
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(3)
    allure.description("公布比赛结果后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_after_bet1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("公布比赛结果后检查余额")
        res = RequestUtils().standard_yaml_case(caseinfo)
        new_total_balance = float(res.json()["data"]["total"])
        amount = float(read_yaml('amount'))
        expected = float(read_yaml("total_balance")) + amount
        assert math.isclose(new_total_balance, expected, rel_tol=1e-9, abs_tol=1e-12)



@allure.feature("篮球/足球串关-lose")
class Test5:

    allure.description("获取余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_get_balance'))
    def test_get_balance(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取篮球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_basketball_info'))
    def test_get_basketball_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("获取足球信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_soccer_info_parlay_0'))
    def test_get_soccer_info_parlay(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下注")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_go_to_bet_parlay'))
    def test_go_to_bet_parlay(self, caseinfo):
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
        total_balance = res.json()["data"]["total"]
        data = {"total_balance": total_balance}
        write_yaml(data)
        assert float(balance) == float(read_yaml('main_balance')) - int(read_yaml("stake_amount"))

    allure.description("公布篮球比赛结果/lose")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_result'))
    def test_get_bet_result(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["outcomes"]["Market"][0]["outcome"][0]["result"] = '0'
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("公布足球比赛结果/lose")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_bet_result_1'))
    def test_get_bet_result_1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["outcomes"]["Market"][0]["outcome"][0]["result"] = '0'
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
                assert i['status_text'] == "lose"
                assert i['stake_amount'] == read_yaml("stake_amount")
                assert i["selections"][0]["sport_name"] == "Basketball"
                assert i["selections"][1]["sport_name"] == "Soccer"

    allure.description("查看transactions历史")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_transactions_history'))
    def test_get_transactions_history(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["validate"]["equals"]["data.list[0].amount"] = -int(read_yaml("stake_amount"))
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(3)
    allure.description("公布比赛结果后检查余额")

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                                            'test_check_balance'))
    def test_check_after_bet1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        new_total_balance = res.json()["data"]["total"]
        assert float(new_total_balance) == float(read_yaml("total_balance"))

