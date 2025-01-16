import jsonpath
import pytest

from commons.ddt_utils import read_case_yaml
from commons.files_path import data_path
from commons.request_utils import RequestUtils
#
# new_data_path = data_path + 'demo.yaml'
# caseinfo ={'name': 'test_get_brick_type', 'story': '积木定义-数据采集', 'title': '获取积木类型', 'request': {'method': 'POST', 'url': 'api/agnes-ac/v2/block/get-tree-node', 'headers': {'cookie': '${get_random_number()}'}}, 'extract': {'blockType': '$.data.children[0].id'}, 'validate': {'codes': 200, 'equals': {'msgType': 'success'}}}

# path = '$.request'
# key = "method"
# value = 'POST'

# import jsonpath
#
# def precise_filtering(res, caseinfo):
#     path = caseinfo["operation"]["path"]
#     key = caseinfo["operation"]["key"]
#     value = caseinfo["operation"]["value"]
#     # 使用 jsonpath 提取匹配结果
#     js_value = jsonpath.jsonpath(res, path)
#     new_res = {}
#     # 如果没有匹配到结果
#     if not js_value:
#         raise ValueError(f"没有找到该路径: {path}")
#
#     for i in js_value:
#         if i.get(key) == value:
#             res = i
#
#     if not res:
#         raise ValueError(f"{js_value}数据中未匹配到{key}为{value}的数据")
#
#     return new_res
#
#
