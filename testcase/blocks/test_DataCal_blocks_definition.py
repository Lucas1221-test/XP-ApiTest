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
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'blocksyaml/test_DataCal_blocks_definition.yaml'

@allure.epic("场景开发-积木管理")
@allure.feature("数据计算类积木")
class Test:
    """
    积木定义-获取积木类型：数据计算类
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_dcm_brick_type'))
    def test_get_dcm_brick_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)



    """
    积木定义-数据计算类-新增前查询列表数据总数
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_before_add_dcm_blocks'))
    def test_check_before_add_dcm_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据计算类-新增：模型计算 积木处理类型
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_dcm_interface_collection'))
    def test_add_dcm_interface_collection(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增模型计算积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_dcm_blockCode'))
    def test_get_dcm_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增模型计算积木后pre-save
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dcm_pre_save'))
    def test_add_dcm_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-新增模型计算 新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_add_dcm_interface_building_blocks'))
    def test_add_dcm_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增模型计算积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_add_dcm_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('新增模型计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        id = read_yaml("pre_save_dcm_pkId")
        for data in datas:
            pkid = data["pkId"]
            if pkid == id:
                new_data.append(data)
        assert res['data']['total'] == read_yaml("pre_add_total") + 1
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockName'] == read_yaml("dcm_blockName")
        assert new_data[0]['blockDesc'] == "test-add"
        assert new_data[0]['allowManualConfirm'] == '1'

    """
    积木定义-数据计算类-模型计算编辑保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_edit_dcm_interface_building_blocks'))
    def test_edit_dcm_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('数据计算类-模型计算-编辑保存')
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-编辑保存模型计算积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_edit_after_dcm_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('编辑模型计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if data.get('blockCode') == read_yaml("dcm_blockCode"):
                new_data.append(data)
        assert new_data[0]['blockName'] == "autotest-数据计算类-模型计算-edit"
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockDesc'] == "test-edit"


    """
        积木定义-数据计算类-复制模型计算积木获取新的blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_dcm_copy_blockCode'))
    def test_get_dcm_copy_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-复制保存模型计算积木
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_copy_dcm_interface_building_blocks'))
    def test_copy_dcm_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-复制保存模型计算积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_copy_dcm_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('复制模型计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml("dcm_copy_blockCode"):
                new_data.append(data)
        dcm_copy_pkId = new_data[0].get("pkId")
        data = {"dcm_copy_pkId": dcm_copy_pkId}
        write_yaml(data)
        assert new_data[0]['blockName'] == 'autotest-数据计算类-模型计算-copy'
        assert new_data[0]['status'] == '01'
        assert res['data']['total'] == read_yaml("pre_add_total") + 2




    """
    积木定义-数据计算类-模型计算审核数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dcm_approve_blocks'))
    def test_dcm_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-模型计算审核数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_dcm_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('模型计算审核数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    (data.get('pkId') == read_yaml("pre_save_dcm_pkId")) or (data.get('pkId') == read_yaml("dcm_copy_pkId"))):
                new_data.append(data)
        assert new_data[0]['status'] == '02'
        assert new_data[1]['status'] == '02'

    """
        积木定义-数据计算类-模型计算发布数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dcm_publish_blocks'))
    def test_dcm_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-模型计算发布数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_dcm_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('模型计算发布数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_dcm_pkId") or data.get('pkId') == read_yaml("dcm_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'

    """
        积木定义-数据计算类-模型计算删除数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dcm_delete_blocks'))
    def test_dcm_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-模型计算删除数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_dcm_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('模型计算删除数据后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_dcm_pkId") or data.get('pkId') == read_yaml("dcm_copy_pkId")):
                new_data.append(data)
        assert new_data == []

    """
       积木定义-数据计算类-新增：数值计算 积木处理类型
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dcc_interface_collection'))
    def test_add_dcc_interface_collection(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
       积木定义-数据计算类-新增：数值计算 积木处理类型
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcc_blocks1'))
    def test_check_after_add_dcc_blocks1(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增模型计算积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_dcc_blockCode'))
    def test_get_dcc_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增数值计算积木后pre-save
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dcc_pre_save'))
    def test_add_dcc_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-新增数值计算 新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dcc_interface_building_blocks'))
    def test_add_dcc_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据计算类-新增数值计算积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_add_dcc_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-数值计算')
        allure.dynamic.title('新增数值计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        id = read_yaml("pre_save_dcc_pkId")
        for data in datas:
            pkid = data["pkId"]
            if pkid == id:
                new_data.append(data)
        assert res['data']['total'] == read_yaml("pre_add_total") + 1

    """
    积木定义-数据计算类-数值计算编辑保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_edit_dcc_interface_building_blocks'))
    def test_edit_dcc_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-编辑保存数值计算积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_edit_after_dcc_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-数值计算')
        allure.dynamic.title('编辑数值计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if data.get('blockCode') == read_yaml("dcc_blockCode"):
                new_data.append(data)
        assert new_data[0]['blockName'] == "autotest-数据计算类-数值计算-edit"
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockDesc'] == "test-edit"

    """
        积木定义-数据计算类-复制数值计算积木获取新的blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_dcc_copy_blockCode'))
    def test_get_dcc_copy_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-复制保存数值计算积木
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_copy_dcc_interface_building_blocks'))
    def test_copy_dcc_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-复制保存数值计算积木后进行检查
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_copy_dcc_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-数值计算')
        allure.dynamic.title('复制数值计算积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml("dcc_copy_blockCode"):
                new_data.append(data)
        dcc_copy_pkId = new_data[0].get("pkId")
        data = {"dcc_copy_pkId": dcc_copy_pkId}
        write_yaml(data)
        assert new_data[0]['blockName'] == 'autotest-数据计算类-数值计算-copy'
        assert new_data[0]['status'] == '01'
        assert res['data']['total'] == read_yaml("pre_add_total") + 2

    """
    积木定义-数据计算类-数值计算审核数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dcc_approve_blocks'))
    def test_dcc_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-数值计算审核数据后检查
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_dcc_approve_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-数值计算')
        allure.dynamic.title('数值计算审核数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    (data.get('pkId') == read_yaml("pre_save_dcc_pkId")) or (
                    data.get('pkId') == read_yaml("dcc_copy_pkId"))):
                new_data.append(data)
        assert new_data[0]['status'] == '02'
        assert new_data[1]['status'] == '02'

    """
        积木定义-数据计算类-数值计算发布数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dcc_publish_blocks'))
    def test_dcc_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-数值计算发布数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_dcc_publish_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-数值计算')
        allure.dynamic.title('数值计算发布数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_dcc_pkId") or data.get('pkId') == read_yaml("dcc_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'

    """
        积木定义-数据计算类-数值计算删除数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dcc_delete_blocks'))
    def test_dcc_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-数值计算删除数据后检查
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dcm_blocks'))
    def test_check_after_dcc_delete_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-数值计算')
        allure.dynamic.title('数值计算删除数据后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_dcc_pkId") or data.get('pkId') == read_yaml(
                "dcc_copy_pkId")):
                new_data.append(data)
        assert new_data == []
        assert res["data"]["total"] == read_yaml("pre_add_total")


    """
    积木定义-数据计算类-新增前查询列表数据总数
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_before_add_dra_blocks'))
    def test_check_before_add_dra_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增报表稽核积木后获取blockCode
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_dra_blockCode'))
    def test_get_dra_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-新增报表稽核积木后pre-save
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dra_pre_save'))
    def test_add_dra_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-新增报表稽核 新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dra_interface_building_blocks'))
    def test_add_dra_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据计算类-新增报表稽核积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dra_blocks'))
    def test_check_after_add_dra_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-报表稽核')
        allure.dynamic.title('新增报表稽核积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        id = read_yaml("pre_save_dra_pkId")
        for data in datas:
            pkid = data["pkId"]
            if pkid == id:
                new_data.append(data)
        assert res['data']['total'] == read_yaml("pre_add_dra_total") + 1


    """
    积木定义-数据计算类-报表稽核编辑保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_edit_dra_interface_building_blocks'))
    def test_edit_dra_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据计算类-编辑保存报表稽核积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dra_blocks'))
    def test_check_edit_after_dra_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('编辑报表稽核积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if data.get('blockCode') == read_yaml("dra_blockCode"):
                new_data.append(data)
        assert new_data[0]['blockName'] == "autotest-数据计算类-报表稽核-edit"
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockDesc'] == "test-edit"


    """
        积木定义-数据计算类-复制报表稽核积木获取新的blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_dra_copy_blockCode'))
    def test_get_dra_copy_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-复制保存报表稽核积木
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_copy_dra_interface_building_blocks'))
    def test_copy_dra_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据计算类-复制保存报表稽核积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dra_blocks'))
    def test_check_after_copy_dra_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('复制报表稽核积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml("dra_copy_blockCode"):
                new_data.append(data)
        dra_copy_pkId = new_data[0].get("pkId")
        data = {"dra_copy_pkId": dra_copy_pkId}
        write_yaml(data)
        assert new_data[0]['blockName'] == 'autotest-数据计算类-报表稽核-edit(copy)'
        assert new_data[0]['status'] == '01'


    """
    积木定义-数据计算类-报表稽核审核数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dra_approve_blocks'))
    def test_dra_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据计算类-报表稽核审核数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dra_blocks'))
    def test_check_after_dra_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('报表稽核审核数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    (data.get('pkId') == read_yaml("pre_save_dra_pkId")) or (
                    data.get('pkId') == read_yaml("dra_copy_pkId"))):
                new_data.append(data)
        assert new_data[0]['status'] == '02'
        assert new_data[1]['status'] == '02'


    """
        积木定义-数据计算类-报表稽核发布数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dra_publish_blocks'))
    def test_dra_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据计算类-报表稽核发布数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dra_blocks'))
    def test_check_after_dra_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('报表稽核发布数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_dra_pkId") or data.get('pkId') == read_yaml("dra_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'

    """
        积木定义-数据计算类-报表稽核删除数据
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dra_delete_blocks'))
    def test_dra_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据计算类-报表稽核删除数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dra_blocks'))
    def test_check_after_dra_delete_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据计算类-报表稽核')
        allure.dynamic.title('报表稽核删除数据后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_dra_pkId") or data.get('pkId') == read_yaml(
                "dra_copy_pkId")):
                new_data.append(data)
        assert new_data == []


















