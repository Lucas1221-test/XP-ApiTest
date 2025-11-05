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
        "password": "04b1ba018bed208d9677dffcf4e82d6116b4e4ad311cad645e6bf6742e6fffa2be849d72b94cfdd65f4040ef8c53b5232c1bd4c55359140b2b0d87344f94d232267513513e891521d93d76a34cf41089939434d858da897f8590cfb166ea4753115be78ff29ec1"
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

