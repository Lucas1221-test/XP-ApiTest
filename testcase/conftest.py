import time

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
    # json=DebugTalk().set_sm2()
    json = {
        "userId": "agnes",
        "password": "0498e9543489833fcba3a9b04a6c3f1fd02d5f8387a580ece8386d38b46c5d2056c9c4313deb0fb8441d7d970a9ac66d17245d49e085d7475a7240d71b111dc608c4220d9ae36510439a7a0262755fda9b5b9663544dc64cd7f31ea938c512f50fea494aba675d9dc3019a"
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

