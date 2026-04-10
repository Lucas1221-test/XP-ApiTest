
import os

CURRENT_ENV = os.getenv("TEST_ENV", "test1")  # 可选值: test1, test2, prod

# 各环境下的服务 Base URL 映射表
BASE_URLS = {
    "test1": {
        "xp": "https://xp-passport-test1-api.helix.city/",
        "xp-1": "https://xp-payment-test1-api.helix.city/",
        "xp-server": "https://xp-service-test1-api.helix.city/",
        "cms": "https://xp-match-cms-test1.helix.city/",
        "order": "https://order-test1-api.helix.city",
        # 可继续添加其他服务，例如 "payment": "https://payment-test1.helix.city"
    },
    "test2": {
        "xp": "https://xp-passport-test2-api.helix.city/",
        "cms": "https://xp-match-cms-test2.helix.city/",
        "order": "https://order-test2-api.helix.city",
    },
    "prod": {
        "xp": "https://xp-passport-api.helix.city/",
        "admin": "https://xp-match-cms.helix.city/",
        "order": "https://order-api.helix.city",
    }
}

# 默认服务名（当用例未指定 service 时使用）
DEFAULT_SERVICE = "xp"


def get_base_url(service_name=None, env=None):
    """
    获取指定环境、指定服务的 Base URL

    :param service_name: 服务名称，如 'xp', 'admin', 'order'，默认使用 DEFAULT_SERVICE
    :param env: 环境名称，如 'test1', 'test2', 'prod'，默认使用 CURRENT_ENV
    :return: 对应的 Base URL 字符串
    :raises ValueError: 当环境或服务不存在时抛出
    """
    if service_name is None:
        service_name = DEFAULT_SERVICE
    if env is None:
        env = CURRENT_ENV

    env_config = BASE_URLS.get(env)
    if not env_config:
        raise ValueError(f"未找到环境配置: {env}，可用的环境: {list(BASE_URLS.keys())}")

    base_url = env_config.get(service_name)
    if not base_url:
        raise ValueError(f"环境 '{env}' 中未找到服务 '{service_name}'，可用的服务: {list(env_config.keys())}")

    return base_url
