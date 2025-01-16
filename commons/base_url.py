
#通过函数封装不同测试环境基础路径
is_test_url = 3


def get_base_url():
    if is_test_url == 1:
        return test_base_url
    elif is_test_url == 2:
        return dev
    else:
        return produce_base_url


dev = "http://172.18.25.250:8080/"        #OMS-dev环境
test_base_url = "http://172.21.0.52:8080/"    #测试环境
produce_base_url = "http://172.18.26.254:8080/"       #生产环境
