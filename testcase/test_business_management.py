import json
import time
from datetime import datetime
from pathlib import Path
from io import StringIO
import allure
import pytest
import yaml

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml

"""测试数据路径"""
new_data_path = data_path + 'test_business_management.yaml'

data_path1 = data_path + 'test_product_information.yaml'
@allure.epic("基础功能")
@allure.feature("基础信息")
class Test:
    """获取产品productId"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_code_query'))
    def test_code_query(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo['request']['json']['productCode'] = '8888-edit'
        RequestUtils().standard_yaml_case(caseinfo)

    """市场日历--测试用例"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_jump_market_calendar'))
    def test_jump_market_calendar(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_init_calendar'))
    def test_init_calendar(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_list_view'))
    def test_list_view(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_filter_calendar_by_market'))
    def test_filter_calendar_by_market(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        workdayId = res['data']['rows'][0]['workdayId']
        data = {"workdayId": workdayId}
        write_yaml(data)
        workday = res['data']['rows'][0]['workday']
        data = {"workday": workday}
        write_yaml(data)
        crtTs = res['data']['rows'][0]['crtTs']
        today = datetime.today().strftime('%Y-%m-%d')
        assert today in crtTs


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_trading_day_change'))
    def test_trading_day_change(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_filter_calendar_by_market'))
    def test_after_trading_day_change(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        new_workday = res['data']['rows'][0]['workday']
        old_workday = read_yaml("workday")
        assert new_workday != old_workday


    """外部机构-测试用例"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_add_institution_type'))
    def test_add_institution_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_query_institution_type'))
    def test_query_institution_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        rows = res.json()["data"]["rows"]
        new_data = []
        for row in rows:
            if isinstance(row, dict) and row.get('orgTypeName') == 'd测试':
                new_data.append(row)
        extOrgId = new_data[0]['orgTypeId']
        data = {"extOrgId": extOrgId}
        write_yaml(data)
        assert new_data[0]['orgTypeCode'] == '0001'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_edit_institution_type'))
    def test_edit_institution_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_query_institution_type'))
    def test_check_after_edit_institution_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        rows = res.json()["data"]["rows"]
        new_data = []
        for row in rows:
            if isinstance(row, dict) and row.get('orgTypeId') == read_yaml("extOrgId"):
                new_data.append(row)
        assert new_data[0]['orgTypeCode'] == '0001-edit'
        assert new_data[0]['orgTypeName'] == 'd测试-编辑'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_get_superior_institution'))
    def test_get_superior_institution(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["children"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgType') == read_yaml('extOrgId'):
                new_data.append(data)
        parentExtOrgId = new_data[0]["id"]
        data = {"parentExtOrgId": parentExtOrgId}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_get_organization_type'))
    def test_get_organization_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        # datas = res.json()["data"]
        # new_data = []
        # for data in datas:
        #     if isinstance(data, dict) and data.get('orgTypeName') == 'd测试-编辑':
        #         new_data.append(data)
        #
        # orgTypeId = new_data[0]["orgTypeId"]
        # orgTypeId = new_data[0]["orgTypeId"]
        #
        # write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_add_external_organization'))
    def test_add_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_check_after_add_external_organization'))
    def test_check_after_add_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["children"]
        new_datas = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgType') == read_yaml("extOrgId"):
                new_datas.append(data)
        datas = []
        new_datas = new_datas[0]["children"]
        for data in new_datas:
            if isinstance(data, dict) and data.get('extOrgName') == '测试':
                datas.append(data)
        external_organization_id = datas[0].get("id")
        extOrgType = datas[0].get("extOrgType")
        new_extOrgId = datas[0].get("extOrgId")
        data = {"new_extOrgId": new_extOrgId}
        write_yaml(data)
        data = {"extOrgType": extOrgType}
        write_yaml(data)
        data = {"external_organization_id": external_organization_id}
        write_yaml(data)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_edit_external_organization'))
    def test_edit_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_check_after_edit_external_organization'))
    def test_check_after_edit_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgId') == read_yaml('new_extOrgId'):
                new_data.append(data)
        assert new_data[0]['extOrgCode'] == '007-edit'
        assert new_data[0]['extOrgName'] == '测试-edit'
        assert new_data[0]['extOrgNameShort'] == 'test-edit'
        assert new_data[0]['extOrgRemark'] == '测试-edit'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_copy_external_organization'))
    def test_copy_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_check_after_edit_external_organization'))
    def test_check_after_copy_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgCode') == '007-copy':
                new_data.append(data)
        copy_extOrgId = new_data[0].get("extOrgId")
        data = {"copy_extOrgId": copy_extOrgId}
        write_yaml(data)
        assert new_data[0]['extOrgName'] == '测试-copy'
        assert new_data[0]['extOrgNameShort'] == 'test-copy'
        assert new_data[0]['extOrgRemark'] == '测试-copy'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_del_external_organization'))
    def test_del_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_del_after_copy_external_organization'))
    def test_del_after_copy_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_get_superior_institution'))
    def test_check_after_del_external_organization(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('external_organization_id') == read_yaml('external_organization_id'):
                new_data.append(data)
        assert new_data == []

    """机构联系人维护"""
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_add_organization_contact'))
    def test_add_organization_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_organization_contact_list'))
    def test_check_after_add_organization_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("编辑机构联系人后校验")
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgId') == read_yaml("new_extOrgId"):
                new_data.append(data)
        linkmanId = new_data[0]['linkmanId']
        data = {"linkmanId": linkmanId}
        write_yaml(data)
        assert new_data[0]['linkmanDept'] == '研发'
        assert new_data[0]['linkmanMobile'] == '13199999999'
        assert new_data[0]['linkmanName'] == '测试人员'
        assert new_data[0]['linkmanRemark'] == '测试-新增'
        assert new_data[0]['linkmanRoleId'] == '测试'
        assert new_data[0]['linkmanStatus'] == '01'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_edit_organization_contact'))
    def test_edit_organization_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_organization_contact_list'))
    def test_check_after_edit_organization_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("编辑机构联系人后校验")
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgId') == read_yaml("new_extOrgId"):
                new_data.append(data)
        linkmanName = new_data[0]['linkmanName']
        data = {"linkmanName": linkmanName}
        write_yaml(data)
        assert new_data[0]['linkmanDept'] == '研发-编辑'
        assert new_data[0]['linkmanMobile'] == '13188888888'
        assert new_data[0]['linkmanName'] == '测试人员-编辑'
        assert new_data[0]['linkmanRemark'] == '测试-编辑'
        assert new_data[0]['linkmanRoleId'] == '测试编辑'
        assert new_data[0]['linkmanStatus'] == '02'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_del_organization_contact'))
    def test_del_organization_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_organization_contact_list'))
    def test_check_after_del_organization_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title("删除机构联系人后校验")
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('extOrgId') == read_yaml("new_extOrgId"):
                new_data.append(data)
        assert new_data == []


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_del_institution_type'))
    def test_del_institution_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_query_institution_type'))
    def test_check_after_del_institution_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        rows = res.json()["data"]["rows"]
        new_data = []
        extOrgId = read_yaml("extOrgId")
        for row in rows:
            if isinstance(row, dict) and row.get('orgTypeName') == extOrgId:
                new_data.append(row)
        assert new_data == []


    """产品联系人维护"""
    @allure.description("获取用户信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_get_user_info'))
    def test_get_user_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_get_tree_code'))
    def test_get_tree_code(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_add_product_type'))
    def test_add_product_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

        @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(new_data_path,
                                'test_check_after_add_product_type'))
        def test_check_after_add_product_type(self, caseinfo):
            allure.dynamic.story(caseinfo['story'])
            allure.dynamic.title(caseinfo['title'])
            res = RequestUtils().standard_yaml_case(caseinfo)
            datas = res.json()["data"]
            new_data = []
            for data in datas:
                if isinstance(data, dict) and data.get('treeName') == "测试-结构名称":
                    new_data.append(data)
            pkId = new_data[0]["pkId"]
            data = {"pkId": pkId}
            write_yaml(data)
            assert new_data[0]["treeCode"] == "0009"
            assert new_data[0]["productPermission"] == "0"
            assert new_data[0]["isShowUndis"] == "1"


    @allure.description("获取系统用户信息")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_get_system_user_info'))
    def test_get_system_user_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_add_product_type_node'))
    def test_add_product_type_node(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_sl_product_type'))
    def test_sl_product_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_add_product_contact'))
    def test_add_product_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path ,
                            'test_check_after_add_product_contact'))
    def test_check_after_add_product_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        data = res.json()["data"]["rows"]
        new_data = []
        for item in data:
            if item.get("tempName") == 'dtest':
                new_data.append(item)

        # 提取第一个匹配项的 pkId
        product_contact_pkId = new_data[0]["pkId"]
        data = {"product_contact_pkId": product_contact_pkId}
        write_yaml(data)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_del_product_contact'))
    def test_del_product_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_check_after_del_product_contact'))
    def test_check_after_del_product_contact(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
        

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_query_product_type_info'))
    def test_query_product_type_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_edit_product_type'))
    def test_edit_product_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_check_after_edit_product_type_info'))
    def test_check_after_edit_product_type_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_del_product_type_node'))
    def test_del_product_type_node(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                                            'test_del_product_type'))
    def test_del_product_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(new_data_path,
                            'test_check_after_product_type_info'))
    def test_check_after_product_type_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path + 'test_product_information.yaml',
                            'test_del_product'))
    def test_del_product(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path + 'test_product_information.yaml',
                            'test_check_after_del_product'))
    def test_check_after_del_product(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
