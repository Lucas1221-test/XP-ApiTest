
#通过函数封装不同测试环境基础路径
is_test_url = 3


def get_base_url():
    if is_test_url == 1:
        return test_base_url
    elif is_test_url == 2:
        return dev
    elif is_test_url == 3:
        return demo
    else:
        return produce_base_url

#OMS-dev环境
dev = "http://172.18.25.250:8080/"
# user3='agnes'
# pw3='045da7e9c91aa9eeb27ce67335010e8e2ac1cc6387d4438920a1f87386e7775cceb3a41f0f620d7056ae81bd74d6607ce561083677c9390af562340035b4e4c975bdf1e7ebb8c74f21af75b5e9e1adfd2c8628a78ad9363cdfd101494aa0f086768cc45a9cc731326367'


test_base_url = "http://172.21.0.52:8080/"    #测试环境
produce_base_url = "http://172.18.26.254:8080/"
#生产环境

demo = "http://172.131.128.4:8080/"
