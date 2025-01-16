
import os

# 获取当前文件所在的路径
current_path = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录的绝对路径
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# 生成输出文件路径
extract_path = os.path.join(root_path, "extract.yaml")
token_path = os.path.join(root_path, "token.yaml")

"""日志路径"""
logs_path = os.path.join(root_path, 'output', 'logs')
temps_path = os.path.join(root_path, 'output', 'temps')
allure_path = os.path.join(root_path, 'output', 'allure_reports')


"""上传文件路径"""
files_path = os.path.join(root_path, 'files', '')

"""测试数据路径"""
data_path =  os.path.join(root_path, 'data', '')




