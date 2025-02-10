import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.read_yml import get_current_time
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'systemmanagementyaml/test_zdgl.yaml'
@allure.epic("系统管理")
@allure.feature("系统管理-字典管理")
class Test:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dict_addType'))
    def test_dict_addType(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryTypeList'))
    def test_tenant_queryTypeList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['data']
        updateUser = {}
        dictTypeId = {}
        appId = {}
        appName = {}
        dataType = {}
        for i in list:
            if i['dictTypeId'] == "111":
                updateUser = i['updateUser']
                dictTypeId = i['dictTypeId']
                appId = i['appId']
                appName = i['appName']
                dataType = i['dataType']
        data = {
            "updateUser": updateUser,
            "dictTypeId": dictTypeId,
            "appId": appId,
            "appName": appName,
            "dataType": dataType
        }
        write_yaml(data)
        total={"total":r.json()["data"]['page']['total']}
        write_yaml(total)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('dictTypeId') == "111":
                new_data.append(data)
        assert new_data[0]['dictTypeName'] == 'dict111'
        assert new_data[0]['dataType'] == '01'
        assert new_data[0]['appId'] == 'AGNES'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_editType'))
    def test_tenant_editType(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryTypeList'))
    def test_check_edit_tenant_queryTypeList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['data']
        dictTypeName = {}
        for i in list:
            if i['dictTypeId'] == "111":
                dictTypeName = i['dictTypeName']
        data = {
            "edit_dictTypeName": dictTypeName
        }
        write_yaml(data)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('dictTypeId') == "111":
                new_data.append(data)
        assert new_data[0]['dictTypeName'] == 'dict222'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_addDictItem'))
    def test_tenant_addDictItem(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryItemList'))
    def test_tenant_queryItemList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['data']
        dictId = {}
        dictName = {}
        for i in list:
            if i['dictTypeId'] == "111":
                dictId = i['dictId']
                dictName = i['dictName']
        data = {
            "dictId": dictId,
            "dictName": dictName,
        }
        write_yaml(data)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('dictTypeId') == "111":
                new_data.append(data)
        assert new_data[0]['dictId'] == '1'
        assert new_data[0]['dictName'] == '字典项test'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_editDictItem'))
    def test_tenant_editDictItem(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryItemList'))
    def test_check_edit_tenant_queryItemList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('dictTypeId') == "111":
                new_data.append(data)
        assert new_data[0]['dictName'] == '字典项test1'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_removeDictItem'))
    def test_tenant_removeDictItem(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryItemList'))
    def test_check_delete_tenant_queryItemList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["q"] = read_yaml("dictName")
        r = RequestUtils().standard_yaml_case(caseinfo)
        assert r.json()["data"]["data"] == []

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_removeType'))
    def test_tenant_removeType(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryTypeList'))
    def test_check_delete_tenant_queryTypeList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response=RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['page']['total'] == int(total)-1
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_case_yaml(data_path,
    #                                         'test_tenant_reloadCache'))
    # def test_tenant_reloadCache(self, caseinfo):
    #     allure.dynamic.story(caseinfo['story'])
    #     allure.dynamic.title(caseinfo['title'])
    #     RequestUtils().standard_yaml_case(caseinfo)