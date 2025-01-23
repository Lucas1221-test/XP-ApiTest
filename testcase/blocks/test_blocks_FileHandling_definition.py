import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.files_path import data_path
from common.yaml_utils import read_yaml, write_yaml

"""测试数据路径"""
data_path = data_path + 'blocksyaml/test_blocks_FileHandling_definition.yaml'

@allure.epic("场景开发-积木管理")
@allure.feature("数据计算类积木")
class Test:

    """
        积木定义-获取积木类型：文件处理类
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_fh_brick_type'))
    def test_get_fh_brick_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-新增前查询列表数据总数
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_before_add_fh_blocks'))
    def test_check_before_add_fh_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-文件处理类-新增：在线编辑 积木处理类型
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_fhedit_interface_collection'))
    def test_add_fhedit_interface_collection(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-新增在线编辑积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_fhedit_blockCode'))
    def test_get_fhedit_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-新增在线编辑积木后pre-save
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_fhedit_pre_save'))
    def test_add_fhedit_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-文件处理类-新增在线编辑 新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_add_fhedit_interface_blocks'))
    def test_add_fhedit_interface_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-新增在线编辑积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_fhedit_blocks'))
    def test_check_after_add_fhedit_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('新增在线编辑积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        id = read_yaml("pre_save_fhedit_pkId")
        for data in datas:
            pkid = data["pkId"]
            if pkid == id:
                new_data.append(data)
        assert res['data']['total'] == read_yaml("pre_fh_total") + 1
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockName'] == read_yaml("fhedit_blockName")
        assert new_data[0]['blockDesc'] == "test-add"
    """
        积木定义-数据计算类-模型计算编辑保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_edit_fhedit_interface_building_blocks'))
    def test_edit_fhedit_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-编辑保存在线编辑积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_fhedit_blocks'))
    def test_check_edit_after_fhedit_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('编辑在线编辑积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if data.get('blockCode') == read_yaml("fhedit_blockCode"):
                new_data.append(data)
        assert new_data[0]['blockName'] == "autotest-文件处理类-在线编辑-edit"
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockDesc'] == "test-edit"

    """
        积木定义-文件处理类-复制在线编辑积木获取新的blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_fhedit_copy_blockCode'))
    def test_get_fhedit_copy_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-文件处理类-复制保存在线编辑积木
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_copy_fhedit_interface_building_blocks'))
    def test_copy_fhedit_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-复制保存在线编辑积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_fhedit_blocks'))
    def test_check_after_copy_fhedit_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('复制模型计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml("fhedit_copy_blockCode"):
                new_data.append(data)
        fhedit_copy_pkId = new_data[0].get("pkId")
        data = {"fhedit_copy_pkId": fhedit_copy_pkId}
        write_yaml(data)
        assert new_data[0]['blockName'] == 'autotest-文件处理类-在线编辑-edit(copy)'
        assert new_data[0]['status'] == '01'
        assert res['data']['total'] == read_yaml("pre_fh_total") + 2

    """
    积木定义-文件处理类-在线编辑审核数据
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_fhedit_approve_blocks'))
    def test_fhedit_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-文件处理类-在线编辑审核数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_fhedit_blocks'))
    def test_check_after_fhedit_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('在线编辑审核数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    (data.get('pkId') == read_yaml("pre_save_fhedit_pkId")) or (
                    data.get('pkId') == read_yaml("fhedit_copy_pkId"))):
                new_data.append(data)
        assert new_data[0]['status'] == '02'
        assert new_data[1]['status'] == '02'

    """
        积木定义-文件处理类-在线编辑发布数据
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_fhedit_publish_blocks'))
    def test_fhedit_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-在线编辑发布数据后检查
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_fhedit_blocks'))
    def test_check_after_fhedit_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('在线编辑发布数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_fhedit_pkId") or data.get('pkId') == read_yaml(
                "fhedit_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'

    """
        积木定义-文件处理类-在线编辑删除数据
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_fhedit_delete_blocks'))
    def test_fhedit_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-文件处理类-在线编辑删除数据后检查
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_fhedit_blocks'))
    def test_check_after_fhedit_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('在线编辑删除数据后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_fhedit_pkId") or data.get('pkId') == read_yaml(
                "fhedit_copy_pkId")):
                new_data.append(data)
        assert new_data == []
