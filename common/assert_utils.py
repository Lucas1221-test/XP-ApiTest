from common.logs_config import logger
import jsonpath
from common.database_util import execute_sql


# ==================== 总入口 ====================
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


# ==================== 辅助方法 ====================
def raise_assert_error(msg):
    logger.info(msg)
    raise AssertionError(msg)


def codes_assert(yq_code, sj_code):
    if yq_code != sj_code:
        raise_assert_error(f"code断言失败，预期结果：{yq_code}，实际结果：{sj_code}")


# ==================== 路径断言（支持数值宽容比较）====================
def equals_assert(equals_config, sj_json):
    if isinstance(equals_config, dict):
        for path, expected in equals_config.items():
            _assert_single_path(path, expected, sj_json)
    elif isinstance(equals_config, list):
        for item in equals_config:
            path = item.get("path")
            expected = item.get("expected")
            if path is None:
                raise_assert_error("equals断言失败：列表项中缺少 'path' 字段")
            _assert_single_path(path, expected, sj_json)
    else:
        raise_assert_error("equals断言失败：配置格式错误，应为 dict 或 list")


def _assert_single_path(path, expected, sj_json):
    jsonpath_expr = path if path.startswith('$') else f"$.{path}"
    result = jsonpath.jsonpath(sj_json, jsonpath_expr)
    if not result:
        raise_assert_error(f"equals断言失败：路径 {jsonpath_expr} 未找到")
    actual = result[0]
    _recursive_compare(expected, actual, jsonpath_expr)


def _is_numeric(value):
    """判断是否为数字（int, float, 数字字符串）"""
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return True
    if isinstance(value, str):
        try:
            float(value)
            return True
        except ValueError:
            return False
    return False


def _recursive_compare(expected, actual, context_path):
    if isinstance(expected, dict) and isinstance(actual, dict):
        for key, exp_val in expected.items():
            if key not in actual:
                raise_assert_error(f"equals断言失败：{context_path}.{key} 不存在于响应中")
            _recursive_compare(exp_val, actual[key], f"{context_path}.{key}")

    elif isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            raise_assert_error(f"equals断言失败：{context_path} 列表长度不匹配，预期 {len(expected)}，实际 {len(actual)}")
        for i, (exp_item, act_item) in enumerate(zip(expected, actual)):
            _recursive_compare(exp_item, act_item, f"{context_path}[{i}]")

    else:
        # 数字宽容比较：尝试将两者转为 float 比较
        if _is_numeric(expected) and _is_numeric(actual):
            if float(expected) != float(actual):
                raise_assert_error(f"equals断言失败：{context_path} 值不匹配，预期 {expected}，实际 {actual}")
        else:
            if expected != actual:
                raise_assert_error(f"equals断言失败：{context_path} 值不匹配，预期 {expected}，实际 {actual}")


def contains_assert(yq_value, sj_test_value):
    if str(yq_value) not in sj_test_value:
        raise_assert_error(f"contains断言失败:返回结果中不包含{str(yq_value)}")


def database_assert(yq_value, sj_json_value):
    for key, sql in yq_value.items():
        lists = jsonpath.jsonpath(sj_json_value, "$..%s" % key)
        if lists:
            try:
                select_result = execute_sql(sql)
            except:
                raise_assert_error("database数据库断言失败: SQL查询异常！请检查SQL语句！")
            else:
                if len(select_result) == 0:
                    raise_assert_error("database数据库断言失败: SQL查询没有结果返回！")
                else:
                    print("lists[0]%s" % lists[0])
                    print("select_result[0]%s" % select_result[0])
                    raise_assert_error("database数据库断言失败: 预期结果"+str(select_result[0])+"不等于SQL查询的实际结果"+str(lists[0])+"")
        else:
            raise_assert_error("database数据库断言失败：返回结果中没有:"+str(key)+"")