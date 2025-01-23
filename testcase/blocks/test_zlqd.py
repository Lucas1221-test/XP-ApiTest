import allure
import pytest
from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path

"""测试数据路径"""
data_path = data_path + 'blocksyaml/test_zlqd.yaml'
@allure.epic("场景开发-积木管理")
@allure.feature("资料清单类-资料清单")
class Test:
    # 获取积木类型
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_brick_type'))
    def test_get_brick_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 检查积木名称
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_zlqd'))
    def test_add_zlqd(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 获取积木编码
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_get_zlqd_blockCode'))
    def test_info_get_zlqd_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增资料清单积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_pre_save'))
    def test_info_zlqd_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增资料清单积木保存填写参数
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_add'))
    def test_info_zlqd_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 查看资料清单列表
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list'))
    def test_info_zlqd_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['rows']
        updateUser = {}
        crtUser = {}
        for i in list:
            if i['blockCode'] == read_yaml('blockCode'):
                crtUser = i['crtUser']
                updateUser = i['updateUser']
        data = {
            "crtUser": crtUser,
            "updateUser": updateUser
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
        assert new_data[0]['blockName'] == '111'
        assert new_data[0]['blockType'] == '07'
        assert new_data[0]['dealType'] == '20'

    # 编辑资料清单积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_edit'))
    def test_info_zlqd_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否编辑成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list_check'))
    def test_info_zlqd_list_edit_check(self, caseinfo):
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
                                            'info_zlqd_copy_get_blockCode'))
    def test_info_zlqd_copy_get_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 复制资料清单积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_copy'))
    def test_info_zlqd_copy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否复制成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list_check'))
    def test_info_zlqd_list_copy_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('copy_blockCode'):
                new_data.append(data)
        assert new_data[0]['blockName'] == '111(copy)'

    # 审核资料清单积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_approve'))
    def test_info_zlqd_approve(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否审核成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list_check'))
    def test_info_zlqd_list_approve_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['status'] == '02'

    # 发布资料清单积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_publish'))
    def test_info_zlqd_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否发布成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list_check'))
    def test_info_zlqd_list_publish_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['status'] == '03'

    # 删除资料清单积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_delete'))
    def test_info_zlqd_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list_check'))
    def test_info_zlqd_list_delete_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total)

    # 获取复制的积木pkid
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list'))
    def test_info_zlqd_list_get_copy_pkid(self, caseinfo):
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

    # 删除复制的积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_delete'))
    def test_info_zlqd_delete_copy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        print(caseinfo)
        caseinfo["request"]["json"]["ids"] = read_yaml("copy_pkId")
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlqd_list_check'))
    def test_sys_delete_zlqd_list_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total) - 1

# 资料清单类-资料审阅
@allure.epic("场景开发-积木管理")
@allure.feature("资料清单类-资料审阅")
class Test1:
    # 获取积木类型
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_brick_type'))
    def test_get_brick_type(self, caseinfo):
        allure.dynamic.story("积木定义-资料清单-资料审阅")
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 检查积木名称
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_zlsy'))
    def test_add_zlsy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 获取积木编码
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_get_blockCode'))
    def test_info_zlsy_get_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增资料审阅积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_pre_save'))
    def test_info_zlsy_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 新增资料审阅积木保存填写参数
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_add'))
    def test_info_zlsy_add(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 查看资料审阅列表
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list'))
    def test_info_zlsy_list(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        r = RequestUtils().standard_yaml_case(caseinfo)
        list = r.json()['data']['rows']
        updateUser = {}
        crtUser = {}
        dealConfJson = {}
        for i in list:
            if i['blockCode'] == read_yaml('blockCode'):
                crtUser = i['crtUser']
                updateUser = i['updateUser']
                dealConfJson = i['dealConfJson']
        data = {
            "crtUser": crtUser,
            "updateUser": updateUser,
            "dealConfJson": dealConfJson
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
        assert new_data[0]['blockName'] == '111'
        assert new_data[0]['dealType'] == '24'
        assert new_data[0]['dealConfJson'] == '[{"fileName":"资料","docId":"1$1$"}]'

    # 编辑RPA任务推送积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_edit'))
    def test_info_zlsy_edit(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否编辑成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list_check'))
    def test_info_zlsy_list_edit_chek(self, caseinfo):
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
                                            'info_zlsy_copy_get_blockCode'))
    def test_info_zlsy_copy_get_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 复制资料审阅积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_copy'))
    def test_info_zlsy_copy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否复制成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list_check'))
    def test_info_zlsy_list_copy_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('copy_blockCode'):
                new_data.append(data)
        assert new_data[0]['blockName'] == '111(copy)'

    # 审核RPA任务推送资料审阅积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_approve'))
    def test_info_zlsy_approve(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否审核成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list_check'))
    def test_info_zlsy_list_approve_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['status'] == '02'

    # 发布资料审阅积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_publish'))
    def test_info_zlsy_publish(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否发布成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list_check'))
    def test_info_zlsy_list_publish_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        res = RequestUtils().standard_yaml_case(caseinfo)
        datas = res.json()["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
                new_data.append(data)
        assert new_data[0]['status'] == '03'

    # 删除资料审阅积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_delete'))
    def test_info_zlsy_delete(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list_check'))
    def test_info_zlsy_list_delete_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total)

    # 获取复制的积木pkid
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list'))
    def test_info_zlsy_list_get_copy_pkid(self, caseinfo):
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

    # 删除复制的积木
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_delete'))
    def test_info_zlsy_delete_copy(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        print(caseinfo)
        caseinfo["request"]["json"]["ids"] = read_yaml("copy_pkId")
        RequestUtils().standard_yaml_case(caseinfo)

    # 验证是否删除成功
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'info_zlsy_list_check'))
    def test_sys_delete_zlqd_list_check(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        total = read_yaml("total")
        assert res['data']['total'] == int(total) - 1