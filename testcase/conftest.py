
import pytest, requests

from common.base_url import get_base_url

from common.yaml_utils import clear_yaml, write_yaml, clear_token_yaml, write_yaml1

from common.files_path import data_path, token_path, user_path

import yaml

data_path = data_path + 'test_account_deposit.yaml'


@pytest.fixture(scope="session", autouse=True)
def test_login():
    url = get_base_url() + 'v1/login'
    with open(user_path, encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
    json = {
        "account": value["user1"]["user"],
        "code": value["user1"]["password"],
        "type": value["user1"]["type"],
        "msgId": ""}
    res = requests.post(url=url, json=json, verify=False)
    token = res.json()['data']['token']
    token = 'Bearer ' + token
    data = {"token": token}
    with open(token_path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


@pytest.fixture(scope="session", autouse=True)
def test_login_cms():
    url = get_base_url("cms") + 'api/user/guest/login/v1'
    with open(user_path, encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
    json = {
        "username": value["user2"]["user"],
        "password": value["user2"]["password"],
        "simpleCaptcha": {},
        "unionLoginType": 1}
    res = requests.post(url=url, json=json, verify=False)
    token = res.json()['data']['token']
    data = {"token_cms": token}
    with open(token_path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


@pytest.fixture(scope="class", autouse=True)
def connection_database():
    clear_yaml()


@pytest.fixture(scope="session", autouse=True)
def connection_database1():
    clear_token_yaml()

