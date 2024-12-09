
#通过函数封装不同测试环境基础路径
is_test_url = 2


def get_base_url():
    if is_test_url == 1:
        return test_base_url
    else:
        return produce_base_url


test_base_url = "http://172.21.0.52:8080/"    #测试环境
produce_base_url = "http://172.18.26.254:8080/"       #生产环境



# is_test_url = ["test", "produce"]
#
# base_urls = []
# def get_base_url():
#     for i in is_test_url:
#         if i == 'test':
#             base_urls.append(test_base_url)  # 将测试环境URL添加到列表中
#         elif i == "produce":
#             base_urls.append(produce_base_url)  # 将生产环境URL添加到列表中
#         return base_urls  # 返回包含所有基础URL的列表


