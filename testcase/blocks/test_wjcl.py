import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
"""测试数据路径"""
data_path = data_path + 'blocksyaml/test_wjcl.yaml'
@allure.epic("场景开发-积木管理")
@allure.feature("文件处理类-混合处理")
class Test:
    # 获取积木类型
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_brick_type'))
    def test_get_brick_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增新增文件服务器配置
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_save_server'))
    def test_save_server(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 获取文件服务器配置id
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'get_serverId'))
    def test_get_serverId(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['rows']
        serverId = {}
        for i in list:
            if i['serverName'] == '1':
                serverId = i['serverId']
        data = {
            "serverId": serverId
        }
        write_yaml(data)
        new_data = []
        for data1 in list:
            if isinstance(data1, dict) and data1.get('serverName') == "1":
                new_data.append(data1)
        assert new_data[0]['serverAddress'] == "1"
        assert new_data[0]['serverPort'] == "1"
        assert new_data[0]['serverUser'] == "1"

    # 检查积木名称
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_mixemail'))
    def test_add_mixemail(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 获取积木编码
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_blockCode'))
    def test_mixEmail_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增文件处理积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_pre_save'))
    def test_mixEmail_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增文件处理保存填写参数
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_add'))
    def test_mixEmail_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 查看文件处理列表
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list'))
    def test_mixEmail_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['rows']
        updateUser = {}
        crtUser = {}
        list_dealId = {}
        for i in list:
            if i.get('blockCode') == read_yaml('blockCode'):
                crtUser = i['crtUser']
                updateUser = i['updateUser']
                list_dealId = i['dealId']
        data = {
            "crtUser": crtUser,
            "updateUser": updateUser,
            "list_dealId": list_dealId
        }
        write_yaml(data)
        blockName = read_yaml("blockName")
        data1 = {"copy_blockName": blockName + "(copy)"}
        write_yaml(data1)
        # 验证是否新增成功
        datas = r.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['blockName'] == "111"
        assert new_data[0]['dealType'] == "07"

    # 获取处理过程信息
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_proc_info'))
    def test_mixEmail_proc_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 编辑文件处理积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_edit'))
    def test_mixEmail_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否编辑成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list_check'))
    def test_mixEmail_list_edit_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['blockName'] == '1111'

    # 获取复制的积木编码
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_copy_get_blockCode'))
    def test_mixEmail_copy_get_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 获取复制积木的处理过程信息
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_copy_proc_info'))
    def test_mixEmail_copy_proc_info(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 复制文件处理积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_copy'))
    def test_mixEmail_copy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否复制成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list_check'))
    def test_mixEmail_list_copy_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('copy_blockCode'):
                new_data.append(data)
        assert new_data[0]['blockName'] == "111(copy)"

    # 审核文件处理积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_approve'))
    def test_mixEmail_approve(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否审核成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list_check'))
    def test_mixEmail_list_approve_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['status'] == "02"

    # 发布文件处理积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_publish'))
    def test_mixEmail_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否发布成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list_check'))
    def test_mixEmail_list_publish_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['status'] == "03"

    # 获取复制的积木pkid
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list'))
    def test_delete_mixEmail_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['rows']
        copy_pkId = {}
        for i in list:
            if i.get('blockCode') == read_yaml('copy_blockCode'):
                copy_pkId = i['pkId']
        data = {
            "copy_pkId": copy_pkId
        }
        write_yaml(data)

    # 删除文件处理积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_delete'))
    def test_mixEmail_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list_check'))
    def test_mixEmail_list_delete_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response=RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total)

    # 删除复制的积木
    @pytest.mark.parametrize("caseinfo",
                                 read_case_yaml(data_path,
                                                'mixEmail_delete'))
    def test_mixEmail_delete_copy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        print(caseinfo)
        caseinfo["request"]["json"]["ids"] =read_yaml("copy_pkId")
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'mixEmail_list_check'))
    def test_mixEmail_list_delete_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response=RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total)-1

    # 删除文件服务器配置
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'server_delete'))
    def test_server_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'get_serverId_list'))
    def test_get_serverId_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        server_total = read_yaml("server_total")
        assert res['data']['total'] == int(server_total)-1

