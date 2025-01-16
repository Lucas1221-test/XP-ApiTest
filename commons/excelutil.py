import openpyxl
from openpyxl import Workbook
#from openpyxl.utils.dataframe import


'''
excel文件的读取
excel文件的读取依赖 xlrd 模块，首先安装xlrd模块 pip install xlrd
Excel文件的读取
1. 导入xlrd模块
2. 打开一个已经存在的Excel文件
3. 按 sheet表格的索引值 或 sheet表格的名称 打开一个sheet表格对象
4. 读取sheet表格里的数据

import xlrd

excelworkbook = xlrd.open_workbook('test_read_excel.xls')  # 打开Excel文件对象

sheet = excelworkbook.sheet_by_index(0)  # 按sheet表格的索引值获取sheet对象
sheet = excelworkbook.sheet_by_name('sheet1')  # 按sheet表格的名字获取sheet对象

print(sheet.nrows)  # 获取对应sheet的行数
print(sheet.ncols)  # 获取对应sheet的列数
print(sheet.cell(1, 0))  # 获取第2行第1列的值（行 列 从0开始）
print(sheet.row(2))   # 获取第3行整行的数据（从0开始），返回的是一个列表
print(sheet.row(3))   # 获取第4行整行的数据（从0开始），返回的是一个列表


excel文件的写入
excel文件的写入操作依赖xlwt模块，首先安装xlwt模块 pip install xlwt
Excel文件的写入
1. 导入xlwt模块
2. 创建一个Excel对象
3. 在创建的Excel对象中添加一个sheet表格
4. 往sheet表格里写入数据
5. 保存数据到Excel中

import xlwt

workbook = xlwt.Workbook()  # 创建一个Excel对象

wsheet = workbook.add_sheet('sheet1')  # 添加一个sheet对象

wsheet.write(0, 0, label='test string')  # 往第1行第1列写数据（行 列 从0开始）
wsheet.write(0, 1, label='123456')       # 往第1行第2列写数据（行 列 从0开始）

workbook.save('test_write_excel.xls')  # 保存写入的数据

'''