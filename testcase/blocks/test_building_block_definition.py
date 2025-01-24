import json
import time
from datetime import datetime
from pathlib import Path
from pprint import pprint
from random import random

import allure
import pytest


from common.ddt_utils import read_case_yaml
from common.request_utils import RequestUtils
from common.yaml_utils import write_yaml, read_yaml
from common.files_path import data_path
from hotloads.debug_talk import DebugTalk
"""测试数据路径"""
data_path = data_path + 'blocksyaml/test_building_block_definition.yaml'

@allure.epic("场景开发-积木管理")
@allure.feature("数据采集类积木")
class Test:
    """
      积木定义-获取积木类型:数据采集
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_dc_brick_type'))
    def test_get_dc_brick_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
      积木定义-数据采集-获取积木处理类型:接口采集
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_interface_collection'))
    def test_add_interface_collection(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
      积木定义-数据采集-接口采集:新增积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_blockCode'))
    def test_get_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集:新增积木后进行pre-save处理
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_pre_save'))
    def test_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        # caseinfo["request"]["json"]["blockType"] = read_yaml("blockType")
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-发送测试
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_send_test'))
    def test_send_test(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_interface_building_blocks'))
    def test_add_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        # caseinfo["request"]["json"]["blockType"] = read_yaml("blockType")
        RequestUtils().standard_yaml_case(caseinfo)

    """
            积木定义-数据采集-接口采集-新增接口采集类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_add_blocks'))
    def test_check_after_add_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('新增接口采集类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        # print(datas)
        new_data = []
        id = read_yaml("pre_save_pkId")
        # print(f"id：{id}")
        for data in datas:
            pkid = data["pkId"]
            # print(pkid)
            if pkid == id:
                new_data.append(data)
        assert new_data[0]['blockName'] == 'autotest-数据采集-接口采集'
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockName'] == read_yaml("blockName")


    """
      积木定义-数据采集-接口采集:复制积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_copy_blockCode'))
    def test_get_copy_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-复制保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dc_copy_blocks'))
    def test_dc_copy_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-复制接口采集类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_blocks'))
    def test_check_after_dc_copy_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('复制接口采集类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml("dc_copy_blockCode"):
                new_data.append(data)
        copy_pkId = new_data[0].get("pkId")
        data = {"copy_pkId": copy_pkId}
        write_yaml(data)
        assert new_data[0]['blockName'] == 'autotest-数据采集-接口采集-copy'
        assert new_data[0]['status'] == '01'

    """
            积木定义-数据采集-接口采集-编辑保存
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_add_interface_building_blocks'))
    def test_dc_edit_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('数据采集-接口采集-编辑保存')
        caseinfo['request']['json']['blockName'] = read_yaml("blockName") + "-edit"
        caseinfo['request']['json']['acReInterfaceDef']['dipName'] = read_yaml("blockName") + "-edit"
        caseinfo['request']['json']['blockDesc'] +="-edit"
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-编辑接口采集类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_blocks'))
    def test_check_after_dc_edit_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('编辑接口采集类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('pkId') == read_yaml("pre_save_pkId"):
                new_data.append(data)
        print("new_data %s"%new_data)
        assert new_data[0]['blockName'] == read_yaml("blockName") +'-edit'
        assert new_data[0]['status'] == '01'
        # assert new_data[0]['blockType'] == '1'

    """
        积木定义-数据采集-接口采集-审核数据
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_dc_approve_blocks'))
    def test_approve_audit_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-审核数据采集类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_blocks'))
    def test_check_after_dc_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('审核数据采集类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (data.get('pkId') == read_yaml("pre_save_pkId") or data.get('pkId') == read_yaml("copy_pkId")):
                new_data.append(data)
        assert new_data[0]['status'] == '02'
        assert new_data[1]['status'] == '02'

    """
            积木定义-数据采集-接口采集-发布数据
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_dc_publish_blocks'))
    def test_dc_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-发布数据采集类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_blocks'))
    def test_check_after_dc_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('发布数据采集类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (data.get('pkId') == read_yaml("pre_save_pkId") or data.get('pkId') == read_yaml("copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'

    """
        积木定义-数据采集-接口采集-删除数据
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_dc_delete_blocks'))
    def test_dc_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-接口采集-删除数据采集类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_blocks'))
    def test_check_after_dc_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('删除数据采集类积木后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (data.get('pkId') == read_yaml("pre_save_pkId") or data.get('pkId') == read_yaml("copy_pkId")):
                new_data.append(data)
        assert new_data == []

    """
        积木定义-数据采集-新增接口采集-获取ETL采集 单JOB类
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_fetch_dc_hexETL_type'))
    def test_fetch_dc_hexETL_type(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-ETL采集 单JOB类，新增积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_hexETL_blockCode'))
    def test_get_hexETL_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-新增数据采集-ETL单JOB-pre-save
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_dc_hexETL_pre_save'))
    def test_dc_hexETL_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集-ETL采集 单JOB类：加载映射字段
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dc_hexETL_onLoad'))
    def test_dc_hexETL_onLoad(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo['request']['json']['confName'] +=str(datetime.now().strftime("%Y%m%d%H%M%S"))
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集类-ETL采集 单JOB类-新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_dc_hexETL_blocks'))
    def test_add_dc_hexETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo['request']['json']['dopETLReConfDB']['confName'] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集类-ETL采集 单JOB类-新增hexETL类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_add_dchexETL_blocks'))
    def test_check_after_add_dchexETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('新增hexETL类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_hexETL_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '01'

    """
        积木定义-数据采集类-ETL采集 单JOB类-编辑保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_edit_dc_hexETL_blocks'))
    def test_edit_dc_hexETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo['request']['json']['dopETLReConfDB']['confName'] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        RequestUtils().standard_yaml_case(caseinfo)


    """
        积木定义-数据采集类-ETL采集 单JOB类-编辑hexETL类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_check_after_add_dchexETL_blocks'))
    def test_check_after_edit_dchexETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('编辑hexETL类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_hexETL_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '01'

    """
        积木定义-数据采集类-ETL采集 单JOB类-复制积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_copy_hexETL_blockCode'))
    def test_get_copy_hexETL_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
        积木定义-数据采集类-ETL采集 单JOB类-复制保存
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_copy_dc_hexETL_blocks'))
    def test_copy_dc_hexETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('新增数据采集-ETL单JOB-复制保存')
        caseinfo['request']['json']['blockName'] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        hexETL_copy_blockName=caseinfo['request']['json']['blockName']
        data = {"hexETL_copy_blockName": hexETL_copy_blockName}
        write_yaml(data)
        RequestUtils().standard_yaml_case(caseinfo)

    """
            积木定义-数据采集类-复制ETL采集单JOB类积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dchexETL_blocks'))
    def test_check_after_copy_dchexETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('复制ETL采集单JOB类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and data.get('blockCode') == read_yaml("copy_hexETL_blockCode"):
                new_data.append(data)
        hexETL_copy_pkId = new_data[0].get("pkId")
        data = {"hexETL_copy_pkId": hexETL_copy_pkId}
        write_yaml(data)
        assert new_data[0]['blockName'] == read_yaml("hexETL_copy_blockName")
        assert new_data[0]['status'] == '01'



    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dc_hexETL_approve_blocks'))
    def test_dc_hexETL_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dchexETL_blocks'))
    def test_check_after_dc_hexETL_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('审核ETL单JOB类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_hexETL_pkId") or data.get('pkId') == read_yaml("hexETL_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '02'

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_dc_hexETL_publish_blocks'))
    def test_dc_hexETL_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dchexETL_blocks'))
    def test_check_after_dc_hexETL_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('发布ETL单JOB类积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print(datas)
        print(id)
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_hexETL_pkId") or data.get('pkId') == read_yaml("hexETL_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'


    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_dc_hexETL_delete_blocks'))
    def test_dc_hexETL_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_dchexETL_blocks'))
    def test_check_after_dc_hexETL_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('删除数据采集类积木后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (data.get('pkId') == read_yaml("pre_save_hexETL_info") or data.get('pkId') == read_yaml("hexETL_copy_pkId")):
                new_data.append(data)
        assert new_data == []

    """
    积木定义-数据采集类-新增ETL采集多JOB积木前查询检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_before_add_mulETL_blocks'))
    def test_check_before_add_mulETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('新增ETL采集多JOB积木前查询检查')
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-新增：ETL采集-多JOB 积木处理类型
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_add_dc_mulETL_interface_collection'))
    def test_add_dc_mulETL_interface_collection(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-新增：ETL采集-多JOB积木后获取blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                            'test_get_mulETL_fhedit_blockCode'))
    def test_get_mulETL_fhedit_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)


    """
    积木定义-数据采集类-新增：ETL采集-多JOB积木后pre-save
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_add_mulETL_pre_save'))
    def test_add_mulETL_pre_save(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockName"] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集类-新增：ETL采集-多JOB 新增保存
    """
    @pytest.mark.parametrize("caseinfo",
                         read_case_yaml(data_path,
                                        'test_add_mulETL_interface_blocks'))
    def test_add_mulETL_interface_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["dopETLReConfDBVos"][0]["confName"]+= str(datetime.now().strftime("%Y%m%d%H%M%S"))
        caseinfo["request"]["json"]["dopETLReConfDBVos"][1]["confName"]+= str(datetime.now().strftime("%Y%m%d%H%M%S"))
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-新增：ETL采集-多JOB积木后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_mulETL_blocks'))
    def test_check_after_add_mulETL_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据采集类-ETL采集-多JOB')
        allure.dynamic.title('新增ETL采集多JOB积木后查询检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        id = read_yaml("pre_save_mulETL_pkId")
        for data in datas:
            pkid = data["pkId"]
            if pkid == id:
                new_data.append(data)
        # assert res['data']['total'] == read_yaml("pre_mulETL_total") + 1
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockName'] == read_yaml("mulETL_blockName")

    """
        积木定义-数据采集类-编辑：ETL采集-多JOB积木
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_edit_mulETL_interface_building_blocks'))
    def test_edit_mulETL_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-编辑：ETL采集-多JOB积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_mulETL_blocks'))
    def test_check_after_edit_mulETL_blocks(self, caseinfo):
        allure.dynamic.story('积木定义-数据采集类-ETL采集-多JOB')
        allure.dynamic.title('编辑ETL采集多JOB积木后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if data.get('blockCode') == read_yaml("mulETL_blockCode"):
                new_data.append(data)
        assert new_data[0]['blockName'] == "autotest-数据采集类-ETL多JOB-edit1"
        assert new_data[0]['status'] == '01'
        assert new_data[0]['blockDesc'] == "test-edit"

    """
        积木定义-数据采集类-复制ETL采集-多JOB积木获取新的blockCode
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_get_mulETL_copy_blockCode'))
    def test_get_mulETL_copy_blockCode(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集类-复制ETL采集-多JOB积木
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_copy_mulETL_interface_building_blocks'))
    def test_copy_mulETL_interface_building_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        caseinfo["request"]["json"]["blockName"] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        caseinfo["request"]["json"]["dopETLReConfDBVos"][0]["confName"] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        caseinfo["request"]["json"]["dopETLReConfDBVos"][1]["confName"] += str(datetime.now().strftime("%Y%m%d%H%M%S"))
        new_data = []
        data = {"mulETL_copy_blockName": caseinfo["request"]["json"]["blockName"]}
        new_data.append(data)
        # print("mulETL_copy_blockName %s"%data)
        write_yaml(new_data[0])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-复制保存ETL采集-多JOB积木后进行检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_mulETL_blocks'))
    def test_check_after_copy_mulETL_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('复制ETL采集-多JOB积木后检查')
        res=RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        print("datas 111 %s"%datas)
        new_data = []
        mulETL_copy_blockCode = read_yaml("mulETL_copy_blockCode")
        print("mulETL_copy_blockCode 111 %s" % mulETL_copy_blockCode)
        for data in datas:
            blockCode = data.get('blockCode')
            if mulETL_copy_blockCode == blockCode:
                new_data.append(data)
        mulETL_copy_pkId = new_data[0].get("pkId")
        data = {"mulETL_copy_pkId": mulETL_copy_pkId}
        print(data)
        write_yaml(data)
        assert new_data[0]['blockName'] == read_yaml("mulETL_copy_blockName")
        assert new_data[0]['status'] == '01'

    """
    积木定义-数据采集类-ETL采集-多JOB积木审核数据
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_mulETL_approve_blocks'))
    def test_mulETL_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
        积木定义-数据采集类-ETL采集-多JOB审核数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_mulETL_blocks'))
    def test_check_after_mulETL_approve_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('ETL采集-多JOB审核数据后检查')
        res = RequestUtils().standard_yaml_case(caseinfo)
        res = res.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    (data.get('pkId') == read_yaml("pre_save_mulETL_pkId")) or (
                    data.get('pkId') == read_yaml("mulETL_copy_pkId"))):
                new_data.append(data)
        assert new_data[0]['status'] == '02'
        assert new_data[1]['status'] == '02'

    """
        积木定义-数据采集类-ETL采集 多JOB发布数据
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_mulETL_publish_blocks'))
    def test_mulETL_publish_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-ETL采集 多JOB发布后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_mulETL_blocks'))
    def test_check_after_mulETL_publish_blocks(self, caseinfo):
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
                    data.get('pkId') == read_yaml("pre_save_mulETL_pkId") or data.get('pkId') == read_yaml(
                "mulETL_copy_pkId")):
                new_data.append(data)
        for item in new_data:
            assert item['status'] == '03'

    """
        积木定义-数据采集类-ETL采集 多JOB-删除数据
    """

    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_mulETL_delete_blocks'))
    def test_mulETL_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title(caseinfo['title'])
        RequestUtils().standard_yaml_case(caseinfo)

    """
    积木定义-数据采集类-ETL采集 多JOB删除数据后检查
    """
    @pytest.mark.parametrize("caseinfo",
                             read_case_yaml(data_path,
                                            'test_check_after_add_mulETL_blocks'))
    def test_check_after_mulETL_delete_blocks(self, caseinfo):
        allure.dynamic.story(caseinfo['story'])
        allure.dynamic.title('ETL采集多JOB删除数据后检查')
        response = RequestUtils().standard_yaml_case(caseinfo)
        res = response.json()
        datas = res["data"]["rows"]
        new_data = []
        for data in datas:
            if isinstance(data, dict) and (
                    data.get('pkId') == read_yaml("pre_save_mulETL_pkId") or data.get('pkId') == read_yaml(
                "mulETL_copy_pkId")):
                new_data.append(data)
        assert new_data == []









