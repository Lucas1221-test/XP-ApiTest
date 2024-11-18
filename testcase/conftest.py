import pytest,requests
from lib.login import login
import yaml,os
from config import HOST1,user1,pw1

#作用域为session的fixture函数，返回token
@pytest.fixture(scope="session")
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

