import pytest,requests
from lib.login import login

@pytest.fixture(scope='function')
def login_setup():
    s=requests.session()
    login(s)
    return s


