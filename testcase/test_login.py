import pytest,allure
from lib.login import login
from common.read_yml import get_login_data

@allure.epic("登录模块")
@allure.feature("登录场景")
class Test_login:
    @allure.story('场景')
    @pytest.mark.parametrize("test_data", get_login_data())
    @allure.title("登录接口")
    def test_login(self,get_environments,test_data):
        host=get_environments
        r = login(host,test_data['name'],test_data['pw'])
        assert r.json()['status'] == '0000'

if __name__=='__main__':
    pytest.main(['../test_login.py','-s'])




