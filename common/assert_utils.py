from common.logs_config import logger
import jsonpath

from common.database_util import execute_sql


#总的断言方法
def assert_result(validate, res):
    for key, value in validate.items():
        if key == "codes":
            codes_assert(value, res.status_code)
        elif key == "equals":
            equals_assert(value, res.json())
        elif key == "contains":
            contains_assert(value, res.text)
        elif key == "database":
            database_assert(value, res.json())
        else:
            print("不支持断言方式")


#抛出断言错误的方法
def raise_assert_error(msg):
    logger.info(msg)
    raise AssertionError(msg)


# 断言状态码
def codes_assert(yq_code, sj_code):
    if yq_code != sj_code:
        raise_assert_error("code断言失败，预期结果："+str(yq_code)+",实际结果："+str(sj_code)+"")



# 递归的相等断言函数
def equals_assert(yq_value, sj_json_value):
    """
    深度递归比较预期值 (yq_value) 和实际值 (sj_json_value)。

    :param yq_value: 预期值字典或列表。
    :param sj_json_value: 实际的 JSON 响应结果。
    """

    # 判断预期值和实际值的类型是否一致
    if isinstance(yq_value, dict) and isinstance(sj_json_value, dict):
        # 遍历预期值的每个键值对
        for key, value in yq_value.items():
            jsonpath_expression = f"$..{key}"  # 允许深度匹配
            list_result = jsonpath.jsonpath(sj_json_value, jsonpath_expression)

            if list_result:  # 如果找到了结果
                if isinstance(value, (dict, list)):
                    # 如果预期值是嵌套结构，则递归比较
                    equals_assert(value, list_result[0])
                elif value not in list_result:
                    raise_assert_error(f"equals断言失败: {key} 的值不匹配，预期={value}，实际={list_result}")
            else:
                raise_assert_error(f"equals断言失败: 返回结果中没有键 {key}")
    elif isinstance(yq_value, list) and isinstance(sj_json_value, list):
        # 如果是列表类型，逐项比较
        if len(yq_value) != len(sj_json_value):
            raise_assert_error(f"equals断言失败: 列表长度不匹配，预期={len(yq_value)}，实际={len(sj_json_value)}")
        for expected_item, actual_item in zip(yq_value, sj_json_value):
            equals_assert(expected_item, actual_item)
    else:
        # 处理基本类型比较
        if yq_value != sj_json_value:
            raise_assert_error(f"equals断言失败: 值不匹配，预期={yq_value}，实际={sj_json_value}")


#包含断言
def contains_assert(yq_value, sj_test_value):
    if str(yq_value) not in sj_test_value:
        raise_assert_error("contains断言失败:返回结果中不包含"+str(yq_value)+"")


#数据库断言
def database_assert(yq_value, sj_json_value):
    for key, sql in yq_value.items():
        lists = jsonpath.jsonpath(sj_json_value, "$..%s" % key)
        if lists:
            try:
                select_result = execute_sql(sql)
            except:
                raise_assert_error("database数据库断言失败: SQL查询异常！请检查SQL语句！")
            else:
                #如果select_result的长度为0，则代表SQL没有查询到值
                if len(select_result) == 0:
                    raise_assert_error("database数据库断言失败: SQL查询没有结果返回！")
                else:
                    print("lists[0]%s" % lists[0])
                    print("select_result[0]%s" % select_result[0])
                    raise_assert_error("database数据库断言失败: 预期结果"+str(select_result[0])+"不等于SQL查询的实际结果"+str(lists[0])+"")
        else:
            raise_assert_error("database数据库断言失败：返回结果中没有:"+str(key)+"")
