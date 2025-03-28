"""
@Filename:  test_material_management.py
@Describe:  材料管理
@Author:    xuhui.ding
@Time:      2025/3/26 14:57
"""
import time

import allure
import pytest

from common.ddt_utils import read_case_yaml
from common.files_path import data_path
from common.request_utils import RequestUtils
from common.yaml_utils import read_yaml, write_yaml
from hotloads.debug_talk import DebugTalk

"""测试数据路径"""

data_path1 = data_path + 'account_management/test_material_management.yaml'


@allure.epic("增值模块")
@allure.feature("账户管理")
class Test:
    allure.description("获取目录名称")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_get_directory_name'))
    def test_get_directory_name(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("新增-账户材料目录")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_add_zhcl_directory'))
    def test_add_zhcl_directory(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("编辑-账户材料目录")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_edit_zhcl_directory'))
    def test_edit_zhcl_directory(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("材料配置")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_material_configuration'))
    def test_material_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("材料配置后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_material_configuration'))
    def test_check_material_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["folderPath"] = read_yaml('FolderPath')
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("修改标签")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_edit_label'))
    def test_edit_label(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("材料配置修改标签后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_edit_label'))
    def test_check_edit_label(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("材料配置后-上传文件")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_upload_file'))
    def test_upload_file(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("保存-上传文件")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_save_upload_file'))
    def test_save_upload_file(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("上传文件")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_update_file'))
    def test_update_file(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("上传文件")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_update_file'))
    def test_update_file(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("上传文件后检查")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_upload_file'))
    def test_check_upload_file(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    allure.description("下载文件")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_download_file'))
    def test_download_file(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["url"] = caseinfo["request"]["url"] + read_yaml("FileObjectId")
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("删除材料配置")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_delete_material_configuration'))
    def test_delete_material_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("删除材料配置后校验")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_check_delete_material_configuration'))
    def test_check_delete_material_configuration(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    allure.description("删除目录")
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path1,
                            'test_delete_zhcl_directory'))
    def test_delete_zhcl_directory(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)