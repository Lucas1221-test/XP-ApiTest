
from config import HOST1
import allure,logging
import requests
from lib.login import login

@allure.step('日志1')
def create(s):
    url=f"{HOST1}/"
    payload={}
    r=s.post(url=url,json=payload)
    return r

@allure.step('日志2')
def get_list(s):
    url=f"{HOST1}/"
    params={}
    r=s.get(url=url,params=params)
    return r

if __name__=='__main__':
    s=requests.session()
    login(s)
    r=create(s)
    print(r.text)

