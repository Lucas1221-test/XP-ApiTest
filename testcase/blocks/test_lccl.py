"""已确认该功能已删掉"""
# import allure
# import pytest
# from common.ddt_utils import read_case_yaml
# from common.request_utils import RequestUtils
# from common.yaml_utils import write_yaml, read_yaml
# from common.files_path import data_path
#
# """测试数据路径"""
# data_path = data_path + 'blocksyaml/test_lccl.yaml'
# @allure.epic("场景开发-积木管理")
# @allure.feature("流程处理类-流程处理")
# class Test:
#     # 获取积木类型
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'test_lccl_get_brick_type'))
#     def test_lccl_get_brick_type(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 检查积木名称
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'test_add_lccl'))
#     def test_add_lccl(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 获取积木编码
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_get_blockCode'))
#     def test_lccl_get_blockCode(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 新增流程处理积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_pre_save'))
#     def test_lccl_pre_save(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 新增流程处理积木保存填写参数
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_add'))
#     def test_lccl_add(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 查看流程处理列表
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list'))
#     def test_lccl_list(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         # 验证是否新增成功
#         res = RequestUtils().standard_yaml_case(caseinfo)
#         datas = res.json()["data"]["rows"]
#         new_data = []
#         for data in datas:
#             if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
#                 new_data.append(data)
#         assert new_data[0]['blockName'] == "111"
#         assert new_data[0]['dealType'] == "08"
#         blockName = read_yaml("blockName")
#         data1 = {"copy_blockName": blockName + "(copy)"}
#         write_yaml(data1)
#
#     # 编辑RPA任务推送积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_edit'))
#
#     def test_lccl_edit(self, caseinfo):
#
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 验证是否编辑成功
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list_check'))
#     def lccl_list_edit_check(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         res = RequestUtils().standard_yaml_case(caseinfo)
#         datas = res.json()["data"]["rows"]
#         new_data = []
#         for data in datas:
#             if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
#                 new_data.append(data)
#         assert new_data[0]['dealConfJson'] == '{\"param1\":\"\",\"url\":\"www1\",\"startType\":\"\",\"statusType\":\"\",\"nodeType\":\"\",\"startParam\":\"\",\"statusParam\":\"\",\"nodeParam\":\"\"}'
#
#     # 获取复制的积木编码
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_copy_get_blockCode'))
#     def test_lccl_copy_get_blockCode(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 复制流程处理积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_copy'))
#     def test_lccl_copy(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 验证是否复制成功
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list_check'))
#     def test_lccl_list_copy_check(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         res = RequestUtils().standard_yaml_case(caseinfo)
#         datas = res.json()["data"]["rows"]
#         new_data = []
#         for data in datas:
#             if isinstance(data, dict) and data.get('blockCode') == read_yaml('copy_blockCode'):
#                 new_data.append(data)
#         assert new_data[0]['blockName'] == "111(copy)"
#
#     # 审核流程处理积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_approve'))
#     def test_lccl_approve(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 验证是否审核成功
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list_check'))
#     def test_lccl_list_approve_check(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         res = RequestUtils().standard_yaml_case(caseinfo)
#         datas = res.json()["data"]["rows"]
#         new_data = []
#         for data in datas:
#             if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
#                 new_data.append(data)
#         assert new_data[0]['status'] == "02"
#
#     # 发布流程处理积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_publish'))
#     def test_lccl_publish(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 验证是否发布成功
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list_check'))
#     def test_lccl_list_publish_check(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         res = RequestUtils().standard_yaml_case(caseinfo)
#         datas = res.json()["data"]["rows"]
#         new_data = []
#         for data in datas:
#             if isinstance(data, dict) and data.get('blockCode') == read_yaml('blockCode'):
#                 new_data.append(data)
#         assert new_data[0]['status'] == "03"
#
#     # 删除流程处理积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_delete'))
#     def test_lccl_delete(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 验证是否删除成功
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list_check'))
#     def test_lccl_list_delete_check(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         response=RequestUtils().standard_yaml_case(caseinfo)
#         res = response.json()
#         total = read_yaml("total")
#         assert res['data']['total'] == int(total)
#
#     # 获取复制的积木pkid
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list'))
#     def test_lccl_list_get_copy_pkid(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         r = RequestUtils().standard_yaml_case(caseinfo)
#         list = r.json()['data']['rows']
#         copy_pkId = {}
#         for i in list:
#             if i.get('blockCode') == read_yaml('copy_blockCode'):
#                 copy_pkId = i['pkId']
#         data = {
#             "copy_pkId": copy_pkId
#         }
#         write_yaml(data)
#
#     # 删除复制的积木
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_delete'))
#     def test_lccl_delete_copy(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         print(caseinfo)
#         caseinfo["request"]["json"]["ids"] = read_yaml("copy_pkId")
#         RequestUtils().standard_yaml_case(caseinfo)
#
#     # 验证是否删除成功
#     @pytest.mark.parametrize("caseinfo",
#                              read_case_yaml(data_path,
#                                             'lccl_list_check'))
#     def test_lccl_delete_copy_list_check(self, caseinfo):
#         allure.dynamic.story(caseinfo['story'])
#         allure.dynamic.title(caseinfo['title'])
#         response = RequestUtils().standard_yaml_case(caseinfo)
#         res = response.json()
#         total = read_yaml("total")
#         assert res['data']['total'] == int(total) - 1