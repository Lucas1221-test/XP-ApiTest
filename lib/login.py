import requests

#登录
def login(host,user,pw):
    url=f"{host}/api/gf-admin/gf/index/login"
    payload={
            "userId": user,
            "password": pw,
            "captcha": "",
            "captchaId": ""
    }
    r=requests.post(url=url,json=payload,allow_redirects=False)
    return r


if __name__=='__main__':
    r=login()
    print(r)
