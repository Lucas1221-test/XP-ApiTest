import json
import time
from pathlib import Path
from pprint import pprint

import allure
import pytest


from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path

"""测试数据路径"""
data_path = data_path + 'test_product_information.yaml'

@allure.epic("基础功能")
@allure.feature("产品信息")
class Test:

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_query_product_information'))
    def test_query_product_information(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_save_product_code'))
    def test_save_product_code(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_save_product'))
    def test_save_product(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_code_query'))
    def test_code_query(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_edit_product_information'))
    def test_edit_product_information(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_edit'))
    def test_check_after_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_review_product'))
    def test_review_product(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_del_product'))
    # def test_del_product(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)

    # time.sleep(3)
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                         'test_check_after_del'))
    # def test_check_after_del(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_skip_product_authorize'))
    def test_skip_product_authorize(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_skip_product_contact'))
    def test_skip_product_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_refresh'))
    def test_refresh(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_jump_to_page'))
    def test_jump_to_page(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_jump_to_product_tree'))
    def test_jump_to_product_tree(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """产品参数"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_ta'))
    def test_add_ta(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_add_ta'))
    def test_check_after_add_ta(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()  # res 是字符串
        rows = res['data']['rows']
        new_data = []
        for row in rows:
            if row.get('paramName') == 'test001':
                new_data.append(row)
        pkId = ', '.join([row.get('pkId') for row in new_data])
        data = {"pkId": pkId}
        write_yaml(data)

    time.sleep(3)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_product_parameter_review'))
    def test_product_parameter_review(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        print(caseinfo)
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_review'))
    def test_check_after_review(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()  # res 是字符串
        rows = res['data']['rows']
        new_data = []
        for row in rows:
            if row.get('paramName') == 'test001':
                new_data.append(row)
        print(new_data)
        paramStatus = ', '.join([row.get('paramStatus') for row in new_data])
        assert paramStatus == "04"


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_del_product_parameter'))
    def test_del_ta_product_parameter(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    time.sleep(10)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_review'))
    def test_check_after_del_product_parameter(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("删除TA产品参数后校验")
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total)-1


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_ta'))
    def test_test_add_fa(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("新增FA产品参数")
        caseinfo['request']['json']['paramBizType'] = "FA"
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_add_ta'))
    def test_check_after_add_fa(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()  # res 是字符串
        rows = res['data']['rows']
        new_data = []
        for row in rows:
            if row.get('paramName') == 'test001':
                new_data.append(row)
        pkId = ', '.join([row.get('pkId') for row in new_data])
        data = {"pkId_fa": pkId}
        write_yaml(data)

    time.sleep(3)
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_del_product_parameter'))
    def test_del_fa_product_parameter(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('删除FA产品信息')
        RequestUtils().standard_yaml_case(caseinfo)


    """产品授权"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_query_org_tree'))
    def test_query_org_tree(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_user_permission_configuration'))
    def test_add_user_permission_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_add_user_permission_configuration'))
    def test_check_after_add_user_permission_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_del_user_permission_configuration'))
    def test_del_user_permission_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_del_user_permission_configuration'))
    def test_check_after_del_user_permission_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

