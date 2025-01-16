"""
@Filename:  class
@Describe:  ...
@Author:    xuhui.ding
@Time:      2025/1/9 12:10
"""
from contextlib import contextmanager


@contextmanager
def add_test_prefix(cls):
    # 保存原始类方法
    original_methods = {attr_name: getattr(cls, attr_name) for attr_name in dir(cls)
                        if callable(getattr(cls, attr_name)) and not attr_name.startswith('__')}

    # 添加带有前缀的函数
    for attr_name, attr in original_methods.items():
        new_name = 'test_' + attr_name
        setattr(cls, new_name, attr)  # 设置新方法

    try:
        yield cls
    finally:
        # 删除带有前缀的函数，恢复原始状态
        for attr_name in original_methods:
            new_name = 'test_' + attr_name
            if hasattr(cls, new_name):
                delattr(cls, new_name)
