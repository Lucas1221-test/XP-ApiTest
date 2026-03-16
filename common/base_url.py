
#通过函数封装不同测试环境基础路径
is_test_url = 5


def get_base_url():
    if is_test_url == 1:
        return test_base_url
    elif is_test_url == 2:
        return dev
    elif is_test_url == 3:
        return demo
    elif is_test_url == 4:
        return demo1
    elif is_test_url == 5:
        return hua_an
    else:
        return produce_base_url

#OMS-dev环境
dev = "http://172.18.25.250:8080/"
hua_an = "http://172.21.0.55:8080/"

test_base_url = "http://172.21.0.52:8080/"    #测试环境
produce_base_url = "http://172.18.26.254:8080/"
#生产环境

demo = "http://172.131.128.4:8080/"


demo1 = 'http://172.21.0.53:8080/'