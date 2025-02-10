import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.read_yml import get_current_time
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'systemmanagementyaml/test_zhgl.yaml'
@allure.epic("系统管理")
@allure.feature("系统管理-租户管理")
class Test:
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_add'))
    def test_tenant_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryList'))
    def test_tenant_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['data']
        updateUser = {}
        id = {}
        tenantName = {}
        tenantId = {}
        validSdateDt = {}
        total = {}
        for i in list:
            if i['tenantId'] == "6666":
                updateUser = i['updateUser']
                id = i['id']
                tenantName = i['tenantName']
                tenantId = i['tenantId']
                validSdateDt = i['validSdateDt']
        total=r.json()['data']['page']['total']
        data = {
            "updateUser": updateUser,
            "id": id,
            "tenantName": tenantName,
            "tenantId": tenantId,
            "validSdateDt": validSdateDt,
            "total": total
        }
        write_yaml(data)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('tenantId') == "6666":
                new_data.append(data)
        assert new_data[0]['tenantName'] == '租户666'
        assert new_data[0]['status'] == '00'
        assert new_data[0]['validSdateDt'] == '2024-12-26'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_edit'))
    def test_tenant_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryList'))
    def test_check_edit_tenant_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('tenantId') == "6666":
                new_data.append(data)
        assert new_data[0]['tenantName'] == '租户6666'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_disable'))
    def test_tenant_disable(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryList'))
    def test_check_disable_tenant_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('tenantId') == "6666":
                new_data.append(data)
        assert new_data[0]['status'] == '01'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_enable'))
    def test_tenant_enable(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryList'))
    def test_check_enable_tenant_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        datas = r.json()["data"]['data']
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('tenantId') == "6666":
                new_data.append(data)
        assert new_data[0]['status'] == '00'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_remove'))
    def test_tenant_remove(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_tenant_queryList'))
    def test_check_delete_tenant_queryList(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response=RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['page']['total'] == int(total)-1