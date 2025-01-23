import requests
from gmssl import sm2, func

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

def login_mock(params, public_key):
        if public_key:
            # 假设 params['password'] 是字符串格式
            password = params.get('password')
            if password:
                sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=None)
                encrypted_password = sm2_crypt.encrypt(password.encode())
                # 在加密后的密码前加上 '04'
                params['password'] = '04' + encrypted_password.hex()

        url = 'http://172.21.0.52:8080/api/gf-admin/gf/index/login'  # 替换为实际的URL
        response = requests.post(url, json=params)
        return response

if __name__=='__main__':
    # r=login()
    # print(r)
    params = {
        'userId': 'agnes',
        'password': 'Agnes1324!'
    }
    public_key = '04abb2e4ea5937b038a066d7eee4a2583abf8b195e30e822046d6125a464413667214ad59d4099b5baf31f5b478e69aff110d4486645afb92babfb2cecb7ffd4e6'  # 如果有的话替换为你的公钥

    response = login_mock(params, public_key)
    print(response.status_code)
    print(response.json())  # 假设响应是JSON格式

