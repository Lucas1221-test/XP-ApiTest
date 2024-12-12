import pytest, requests

from common.base_url import get_base_url
from common.yaml_utils import clear_yaml, write_yaml, clear_token_yaml
from lib.login import login
from common.files_path import data_path, token_path

import yaml,os
from config import HOST1,user1,pw1
data_path = data_path + 'test_business_management.yaml'
#作用域为session的fixture函数，返回token
@pytest.fixture(scope="session",)
def get_token_fixture():
    r = login(HOST1,user1,pw1)
    token = r.json()['data']['attrs']['token']
    return token

#返回全局host
@pytest.fixture(scope="session")
def get_environments():
    current_path = os.path.dirname(os.path.realpath(__file__))
    ymlpath = os.path.join(os.path.dirname(current_path), 'data', 'environments.yaml')
    with open(ymlpath, 'r') as stream:
        return yaml.safe_load(stream)['environments']['active']['base_url']

@pytest.fixture(scope="session", autouse=True)
def test_login():
    url = get_base_url() + 'api/gf-admin/gf/index/login'
    json = {
        "userId": "agnes",
        # "password": "04eb67a63a00be680255e493fa65c29cf01af0ebec4bb2182f122c1e44ac9b8df4c9656802f0d1d658b4dcf1645aa583dc8fedad4e8029830ac36f8300d82c2621f1000efd305bcd9c8fde0ffacae040c5031b2acea377a905ecf8887811560e238eff2188e194298b42"
        "password": "04e3abfcb8de452428bf686cb270986cb58bd2458074acd88b232a3969a6e92a97b3e2f2aca8b65e20f63ed001896f6855b19ed93b107df86ad38e51fd60f0129a6f6fa2b14777271a4775b41217e9ebc1503bf73e61088ceb87f8302c26a8e56ed08f42e4793d11166e1d"
        # "password": "04d314a81249ab09f7f72c58a2dd65acce49a7e72739da7b995630a60c37ff44a2c09a0f350288c9fb754b9db96021a077391d0bbfa76edfc815bd74d6d1a27f67c1b741f96e3ee70104cfbc47398610173ffa63165478c997fc67af5c071ef1a6aca480f3345a235c37"
    }
    res = requests.post(url=url, json=json)
    token = res.json()['data']['attrs']['token']
    token = 'token=' + token
    data = {"token": token}
    with open(token_path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


@pytest.fixture(scope="class", autouse=True)
def connection_database():
    clear_yaml()


@pytest.fixture(scope="session", autouse=True)
def connection_database1():
    clear_token_yaml()

