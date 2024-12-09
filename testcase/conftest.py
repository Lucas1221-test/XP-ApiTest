import pytest, requests

from common.base_url import get_base_url
from common.yaml_utils import clear_yaml, write_yaml
from lib.login import login
from common.files_path import data_path

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
        "password": "043a2af86b213accb9378539ad8fcf270f42fb81f727736b8bb280958ba0a9c41cf75c683876232b9fa24b800b097598a67d6627dfbe7b6d871b5304e9c89d759c29898aa25caac1122686366d57f4403c288cc8b930ba2dd7ff1b929d9e211c725a8aa713e6cf4920d9dc"
    }
    res = requests.post(url=url, json=json)
    token = res.json()['data']['attrs']['token']
    token = 'token=' + token
    data = {"token": token}
    write_yaml(data)
    return token




@pytest.fixture(scope="session", autouse=True)
def connection_database():
    clear_yaml()
