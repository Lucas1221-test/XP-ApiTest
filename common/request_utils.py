import json
import re
from io import StringIO
import jsonpath
import requests
import urllib3
import yaml

from common.assert_utils import assert_result
from common.yaml_utils import write_yaml
from hotloads.debug_talk import DebugTalk
from common.base_url import get_base_url
from common.logs_config import logger

# ========== 全局 YAML 配置：强制所有字符串输出带单引号 ==========
def quoted_str_representer(dumper, data):
    """自定义 YAML 字符串表示器，所有字符串输出为单引号格式"""
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")

yaml.add_representer(str, quoted_str_representer)
# =============================================================


class RequestUtils:
    def __init__(self):
        # 禁用 InsecureRequestWarning
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.sess = requests.Session()

    def standard_yaml_case(self, caseinfo):
        """处理标准化 YAML 测试用例"""
        logger.info("-----------测试用例请求开始-----------")

        # 在请求之前调用热加载，处理 YAML 中的动态方法调用
        yaml_str = yaml.dump(caseinfo, allow_unicode=True)
        yaml_str = self.replace_hotload(yaml_str)
        caseinfo = yaml.safe_load(StringIO(yaml_str))




        # 检查一级目录是否包含必要字段
        required_case_keys = {"name", "story", "title", "request", "validate"}
        if not required_case_keys.issubset(caseinfo.keys()):
            logger.error(f"YAML 一级目录必须包含以下字段: {required_case_keys}")
            return None

        # 检查 request 中必须字段
        request_keys = caseinfo["request"].keys()
        required_request_keys = {"method", "url"}
        if not required_request_keys.issubset(request_keys):
            logger.error(f"YAML 中的 request 部分必须包含以下字段: {required_request_keys}")
            return None

        # 处理 JSON 数据
        if "json" in caseinfo["request"]:
            json_data = caseinfo["request"]["json"]
            if isinstance(json_data, str):  # 如果是字符串形式
                try:
                    # 替换单引号为双引号并解析
                    json_data = json.loads(json_data.replace("'", '"'))
                    caseinfo["request"]["json"] = json_data
                except json.JSONDecodeError as e:
                    logger.error(f"JSON 格式错误: {e}")
                    raise ValueError(f"无效的 JSON 数据: {json_data}")
            elif isinstance(json_data, (dict, list)):  # 如果是字典或列表
                logger.info("JSON 数据已为字典或列表类型，无需转换")
            else:
                logger.warning(f"JSON 数据格式不符合预期: {json_data}，请检查用例")

        # 构造完整 URL
        if not caseinfo["request"]["url"].startswith("http"):
            service = caseinfo.get("service")
            base_url = get_base_url(service)
            caseinfo["request"]["url"] = base_url + caseinfo["request"]["url"]


        # 打印详细日志
        logger.info(f"用例名称: {caseinfo['name']}")
        logger.info(f"用户故事: {caseinfo['story']}")
        logger.info(f"用例标题: {caseinfo['title']}")
        logger.info(f"请求方式: {caseinfo['request']['method']}")
        logger.info(f"请求路径: {caseinfo['request']['url']}")
        if "headers" in request_keys:
            logger.info(f"请求头: {caseinfo['request']['headers']}")
        if "json" in request_keys:
            logger.info(f"请求 JSON 参数: {caseinfo['request']['json']}")
        if "data" in request_keys:
            logger.info(f"请求 DATA 参数: {caseinfo['request']['data']}")
        if "params" in request_keys:
            logger.info(f"请求 PARAMS 参数: {caseinfo['request']['params']}")
        if "files" in request_keys:
            logger.info(f"请求文件: {caseinfo['request']['files']}")

            # 处理文件上传
            for file_key, file_value in caseinfo["request"]["files"].items():
                caseinfo["request"]["files"][file_key] = open(file_value, "rb")

        # 发送请求
        res = self.send_all_request(**caseinfo["request"])

        # 打印响应内容
        logger.info(f"实际响应状态码: {res.status_code}")
        logger.info(f"实际响应内容: {res.text}")

        # 提取变量
        self.extract_yaml_value(caseinfo, res)

        # 校验断言
        if "validate" in caseinfo:
            assert_result(caseinfo["validate"], res)

        logger.info("接口测试通过")
        logger.info("-----------测试用例请求结束-----------\n")
        return res

    def send_all_request(self, **kwargs):
        # 完全禁用代理（忽略环境变量、session 配置和参数传入）
        self.sess.trust_env = False
        self.sess.proxies.clear()
        kwargs['proxies'] = {'http': None, 'https': None}
        return self.sess.request(**kwargs)

    def extract_yaml_value(self, caseinfo, res):
        """提取中间变量并保存到 YAML"""
        if "extract" in caseinfo.keys():
            for key, value in caseinfo["extract"].items():
                if "(.*?)" in value or "(.+?)" in value:  # 正则提取
                    zz_value = re.findall(value, res.text)
                    if not zz_value:
                        logger.warning(f"正则表达式未提取到值: {value}")
                    else:
                        # 保留正则提取的原始数据格式
                        data = {key: zz_value[0]} if len(zz_value) == 1 else {key: zz_value}
                        write_yaml(data)
                else:  # JSONPath 提取
                    try:
                        js_value = jsonpath.jsonpath(res.json(), value)
                        if js_value:
                            # 保留 JSONPath 提取的原始数据格式
                            data = {key: js_value[0]} if len(js_value) == 1 else {key: js_value}
                            write_yaml(data)
                        else:
                            logger.warning(f"JSONPath 未提取到值: {value}")
                    except ValueError as e:
                        logger.error(f"响应 JSON 解析失败: {e}")
                        raise ValueError("响应不是有效的 JSON 数据，无法使用 JSONPath 进行提取")

    def replace_hotload(self, yaml_str):
        """热加载 YAML 中的动态方法调用，保留 YAML 中的引号意图"""
        # 匹配占位符：${func(args)}，并同时捕获其前后的引号（可选）
        # 注意：这里使用更复杂的正则，捕获占位符及其可能的引号
        # 模式：可能存在的单引号/双引号 + 占位符 + 可能存在的相同引号
        # 由于占位符中不包含引号，所以可以安全匹配
        pattern = r"(['\"]?)\$\{(\w+)\(([^)]*?)\)\}(['\"]?)"

        def replacer(match):
            left_quote = match.group(1)  # 前置引号（如果有）
            func_name = match.group(2)  # 函数名
            args_str = match.group(3)  # 参数字符串
            right_quote = match.group(4)  # 后置引号（如果有）

            # 检查引号是否匹配（都为空或相同）
            if left_quote and right_quote and left_quote != right_quote:
                # 如果引号不匹配，忽略引号部分，按无引号处理
                left_quote = right_quote = ''

            # 调用函数获取新值
            if args_str == "":
                new_value = getattr(DebugTalk(), func_name)()
            else:
                # 参数按逗号分割，注意参数本身不能含逗号，这里保持原逻辑
                new_value = getattr(DebugTalk(), func_name)(*args_str.split(","))

            # 根据原占位符是否有引号来决定新值的输出形式
            if left_quote:
                # 如果原占位符被引号包围，强制新值转为字符串（即使原本是整数）
                new_value_str = "'" + str(new_value) + "'"
                # 保留原来的引号风格（单引号或双引号）
                # 注意：这里统一使用单引号，如果你需要区分，可以动态使用 left_quote
            else:
                # 无引号：保持原始类型的字符串表示（整数、列表等）
                if isinstance(new_value, str):
                    new_value_str = "'" + new_value + "'"  # 字符串自动加引号
                elif isinstance(new_value, (list, dict, tuple)):
                    new_value_str = str(new_value)  # 集合类型保持原样
                else:
                    # 数字、布尔等：不加引号
                    new_value_str = str(new_value)

            # 返回替换后的完整内容（包括引号，但引号已被包含在 new_value_str 中）
            # 这里用 new_value_str 直接替换整个匹配（包括原引号）
            return new_value_str

        # 执行替换
        yaml_str = re.sub(pattern, replacer, yaml_str)
        return yaml_str