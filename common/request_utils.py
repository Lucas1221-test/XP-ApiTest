import re
from io import StringIO
import jsonpath
import requests
import yaml

from common.assert_utils import assert_result
from common.yaml_utils import write_yaml
from hotloads.debug_talk import DebugTalk
from common.base_url import get_base_url
from common.logs_config import logger


class RequestUtils:
    def __init__(self):
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

        # 构造完整 URL
        if not caseinfo["request"]["url"].startswith("http"):
            caseinfo["request"]["url"] = get_base_url() + caseinfo["request"]["url"]

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
        """统一封装发送请求"""
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
                        data = {key: str(zz_value[0])} if len(zz_value) == 1 else {key: str(zz_value)}
                        write_yaml(data)
                else:  # JSONPath 提取
                    js_value = jsonpath.jsonpath(res.json(), value)
                    if js_value:
                        data = {key: str(js_value[0])} if len(js_value) == 1 else {key: str(js_value)}
                        write_yaml(data)
                    else:
                        logger.warning(f"JSONPath 未提取到值: {value}")

    def replace_hotload(self, yaml_str):
        """热加载 YAML 中的动态方法调用"""
        regexp = r"\$\{(.*?)\((['\"]?.*?['\"]?)\)\}"
        fun_list = re.findall(regexp, yaml_str)
        if fun_list:
            for f in fun_list:
                if not f[1]:  # 无参数
                    new_value = getattr(DebugTalk(), f[0])()
                else:  # 有参数
                    new_value = getattr(DebugTalk(), f[0])(*f[1].split(","))

                # 确保返回值是字符串，并添加引号
                if isinstance(new_value, str):
                    new_value = f"'{new_value}'"
                elif isinstance(new_value, int):  # 避免自动丢失前导零
                    new_value = f"'0{new_value}'" if new_value < 10 else str(new_value)

                # 替换原始值
                old_value = f"${{{f[0]}({f[1]})}}"
                yaml_str = yaml_str.replace(old_value, new_value)
        return yaml_str

