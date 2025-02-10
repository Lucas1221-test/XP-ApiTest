import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.read_yml import get_current_time
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'systemmanagementyaml/test_jggl.yaml'
@allure.epic("系统管理")
@allure.feature("系统管理-机构管理")
class Test:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_addOrg'))
    def test_org_addOrg(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_checkOrgCodeExist'))
    def test_org_checkOrgCodeExist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_checkOrgNameExist'))
    def test_org_checkOrgNameExist(self, caseinfo):
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
        updateUser = {}
        dataType = {}
        orgHierarchy = {}
        parentOrgId = {}
        parentOrgName = {}
        for i in list:
            if i['orgCode'] == "111":
                orgName = i['orgName']
                orgType = i['orgType']
                orgSeq = i['orgSeq']
                orgId = i['orgId']
                updateUser = i['updateUser']
                dataType = i['dataType']
                orgHierarchy = i['orgHierarchy']
                parentOrgId = i['parentOrgId']
                parentOrgName = i['parentOrgName']
        data = {
            "orgName": orgName,
            "orgType": orgType,
            "orgSeq": orgSeq,
            "orgId": orgId,
            "updateUser": updateUser,
            "dataType": dataType,
            "orgHierarchy": orgHierarchy,
            "parentOrgId": parentOrgId,
            "parentOrgName": parentOrgName,
        }
        write_yaml(data)
        a = {"len":len(r.json()['data'])}
        write_yaml(a)
        datas = r.json()["data"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('orgCode') == "111":
                new_data.append(data)
        assert new_data[0]['orgName'] == '机构test'
        assert new_data[0]['dataType'] == 'hr'
        assert new_data[0]['orgType'] == '01'
        assert new_data[0]['parentOrgId'] == 25
        assert new_data[0]['parentOrgName'] == "信息技术部"

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_editOrg'))
    def test_org_editOrg(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_checkOrgCodeExist'))
    def test_org_checkOrgCodeExist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["orgCode"] = "1111"
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_org_checkOrgNameExist'))
    def test_org_checkOrgNameExist(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["orgName"] = "机构test1"
        RequestUtils().standard_yaml_case(caseinfo)

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
        r=RequestUtils().standard_yaml_case(caseinfo)
        assert len(r.json()['data']) == read_yaml("len")-1