import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
"""测试数据路径"""
data_path = data_path + 'test_jsgl.yaml'
@allure.epic("系统管理")
@allure.feature("系统管理-角色管理")
class Test:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_role_add'))
    def test_role_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_role_queryList'))
    def test_role_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r=RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['data']
        appId = {}
        roleId = {}
        roleDesc = {}
        tenantId = {}
        appName = {}
        for i in list:
            if i['roleName'] == "角色test":
                appId = i['appId']
                roleId = i['roleId']
                roleDesc = i['roleDesc']
                tenantId = i['tenantId']
                appName = i['appName']
        data = {
            "appId": appId,
            "roleId": roleId,
            "roleDesc": roleDesc,
            "tenantId": tenantId,
            "appName": appName
        }
        write_yaml(data)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('roleId') == "roletest":
                new_data.append(data)
        assert new_data[0]['appId'] == 'AGNES'
        assert new_data[0]['roleName'] == '角色test'
        assert new_data[0]['roleDesc'] == 'a'


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_role_edit'))
    def test_role_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_role_queryList'))
    def test_check_edit_role_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r=RequestUtils().standard_yaml_case(caseinfo)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('roleId') == "roletest":
                new_data.append(data)
        assert new_data[0]['roleName'] == '角色test1'
        assert new_data[0]['roleDesc'] == 'aa'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_role_remove'))
    def test_role_remove(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_role_queryList'))
    def test_check_delete_role_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["q"] = read_yaml("roleId")
        r=RequestUtils().standard_yaml_case(caseinfo)
        assert r.json()["data"]["data"] == []