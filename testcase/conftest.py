import pytest, requests

from common.base_url import get_base_url
from common.yaml_utils import clear_yaml, write_yaml, clear_token_yaml
from hotloads.debug_talk import DebugTalk
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
    json=DebugTalk().set_sm2()
    # json = {
    #     "userId": "agnes",
    #     "password": "04aadffb4193880ce5c1f92aac21369208e1a9f0f1bf6ef7aeddbf0b58f58c896a348479d8f59852fb8731e920a8c7fb4a2353cf1d64d2b24acd8a79f27099ec24d97be7c3d8eccfac5020be6975454f05a6bc8354086b9e7e18371c36cf76441a74a1004617506d33815d"
    # }
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

