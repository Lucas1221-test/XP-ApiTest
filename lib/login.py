import hashlib
import requests
from config import HOST1

'''
def md5(str):
    a=hashlib.md5()
    a.update(str.encode('utf8'))
    return a.hexdigest()
'''

def login(s):
    url=f"{HOST1}/api/gf-admin/gf/index/login"
    payload={
            "userId": "agnes",
            "password": "04ade38818827068bb6e0ad9a8d902be7e9cb3b69145c3e6d1eca35d2bfc8933393c73893efa2649053b4ea12ef34b4fbf903d1cab8da9bea1fa5bacc844f5c7c2c0e400c05cf7de0980e3f8d12e96497ac9983518b034ecc5692e1f5d9653e8f3af7e72dc7b027c2e3b",
            "captcha": "",
            "captchaId": ""
    }
    r=s.post(url=url,json=payload)
    return r

if __name__=='__main__':
    s=requests.session()
    r=login(s)
    print(r.text)
