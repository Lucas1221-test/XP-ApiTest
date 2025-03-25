"""
@Filename:  query_utils
@Describe:  ...
@Author:    xuhui.ding
@Time:      2025/3/25 11:53
"""

import datetime
from datetime import datetime, timedelta
import time

from common.request_utils import RequestUtils

class QueryUtils:
    def wait_until_total_positive(self, caseinfo, timeout=300):
        start_time = time.time()
        while True:
            # 发起请求获取最新响应
            res = RequestUtils().standard_yaml_case(caseinfo)
            total = res.json()["data"]["total"]

            # 检查 total 是否大于 0
            if total > 0:
                break

            # 检查是否超时
            if time.time() - start_time > timeout:
                print("超过最大等待时间，停止查询")
                break

            # 间隔 5 秒后重试
            time.sleep(5)
