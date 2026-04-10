import requests


def test1():
    url = 'https://xp-match-cms-test1.helix.city/api/user/guest/login/v1'
    json = {
    "username": "Lucas",
    "password": "Lucas123456",
    "simpleCaptcha": {
         # "id": "558b557b-cca4-481b-a31c-3e672906d6c1",
         # "value": "85"
    },
    "unionLoginType": 1
    }
    res = requests.post(url=url, json=json, verify=False)
    print(res.json())
