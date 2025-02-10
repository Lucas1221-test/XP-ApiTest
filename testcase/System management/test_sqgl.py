import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.read_yml import get_current_time
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'systemmanagementyaml/test_sqgl.yaml'
@allure.epic("系统管理")
@allure.feature("系统管理-授权管理")
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
        roleName = {}
        for i in list:
            if i['roleName'] == "角色test":
                appId = i['appId']
                roleId = i['roleId']
                roleDesc = i['roleDesc']
                tenantId = i['tenantId']
                appName = i['appName']
                roleName = i['roleName']
        data = {
            "appId": appId,
            "roleId": roleId,
            "roleDesc": roleDesc,
            "tenantId": tenantId,
            "appName": appName,
            "roleName": roleName
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
                                            'test_auth_saveRoleAuth'))
    def test_auth_saveRoleAuth(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_res_queryAuthList'))
    def test_res_queryAuthList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)
        assert read_yaml('roleResIds') == ['00000021']

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_addOrg'))
    def test_org_addOrg(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_getOrgTree'))
    def test_org_getOrgTree(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']
        orgName = {}
        orgType = {}
        orgSeq = {}
        orgId = {}
        for i in list:
            if i['orgCode'] == "111":
                orgName = i['orgName']
                orgType = i['orgType']
                orgSeq = i['orgSeq']
                orgId = i['orgId']
        data = {
            "orgName": orgName,
            "orgType": orgType,
            "orgSeq": orgSeq,
            "orgId": orgId
        }
        write_yaml(data)
        datas = r.json()["data"]
        a = {"len": len(r.json()['data'])}
        write_yaml(a)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('orgCode') == "111":
                new_data.append(data)
        assert new_data[0]['orgName'] == '机构test'
        assert new_data[0]['orgType'] == '01'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_user_addUser'))
    def test_user_addUser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_user_queryUserList'))
    def test_user_queryUserList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['data']
        data = {
            "total": r.json()['data']['page']['total']
        }
        write_yaml(data)
        new_data = []
        for data in list:
            if isinstance(data, dict) and data.get('userId') == "mmm":
                new_data.append(data)
        assert new_data[0]['validSdateDt'] == '2024-12-26'
        assert new_data[0]['userStatus'] == '02'
        assert new_data[0]['loginType'] == 'default'
        assert new_data[0]['loginCheckType'] == 'default,other'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_user_getByUserId'))
    def test_user_getByUserId(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_auth_addUserAuth'))
    def test_auth_addUserAuth(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_auth_removeUserAuth'))
    def test_auth_removeUserAuth(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_user_removeUser'))
    def test_user_removeUser(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_user_queryUserList'))
    def test_check_delete_user_queryUserList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['page']['total'] == int(total) - 1

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_removeOrg'))
    def test_org_removeOrg(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_getOrgTree'))
    def test_check_org_getOrgTree(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        assert len(r.json()['data']) == read_yaml("len") - 1

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