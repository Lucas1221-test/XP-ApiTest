"""
@Filename:  aaa
@Describe:  ...
@Author:    xuhui.ding
@Time:      2024/12/20 16:54
"""
import pytest
from common.demo import add_test_prefix
from lib.test_bbb import Test, Test1, Test2


# class TestCase1:
#     # 应用装饰器
#     with add_test_prefix(Test):
#         Test()
#     with add_test_prefix(Test2):
#         Test2()

# if __name__ Test2()== '__main__':
#     execution_order = ["TestCase", "TestCase1"]
#     tasks = {"TestCase": TestCase, "TestCase1":TestCase1}
#     for task_name in execution_order:
#         tasks[task_name]().run()
#
# class Demo1:
#
#     Test().test_query_product_information()

# 确保类已定义
import inspect


def run_class_methods(cls):
    # 获取类中所有的方法
    methods = [method for method, _ in inspect.getmembers(cls, predicate=inspect.isfunction)]

    # 遍历并执行每个方法
    for method_name in methods:
        # 获取方法对象
        method = getattr(cls, method_name)
        # 创建类的实例（假设该类有无参数的构造函数）
        instance = cls()
        # 执行方法
        print(f"Running {method_name}...")
        method(instance)

# # 测试
# class Test3:
#     def test_query_product_information(self):
#         print("Executing test_query_product_information")
#
#     def test_save_product_code(self):
#         print("Executing test_save_product_code")
#
#     def test_save_product(self):
#         print("Executing test_save_product")

# 调用方法
run_class_methods(Test)