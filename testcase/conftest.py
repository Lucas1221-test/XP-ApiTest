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
        "password": "0447bbae08e985bebc8346fe19e2386f2bc5590bd23e8dd7ab80efe705f8d98965b23dc61988916b501856d4fe3bf3971589e3ee4679692d34096b225e69863f2ebe697eb75787f2f82624334366bda8d45b7f76f66e3ffae1115b9adab5744f8b69f9a9250d343d48a075"
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

