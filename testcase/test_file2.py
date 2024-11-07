import pytest
from lib.login import login

def setup_module():
    print("初始化...")

def teardown_module():
    print("清理....")

def test_login1(login_setup):
    s=login_setup
    print('步骤一：登录')
    r=login(s)
    #assert r.json()['ok']=='true'
    assert r.json()['message']=='ok'


if __name__=='__main__':
    pytest.main(['../test_file2.py','-s'])

