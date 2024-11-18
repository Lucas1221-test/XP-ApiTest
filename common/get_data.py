'''
import os
import json,logging

def get_json_data(file_path):
    """
    读取json文件中的数据
    :param file_path: 文件路径
    :return:
    """
    if os.path.exists(file_path):
        files = os.path.splitext(file_path)
        filename, suffix = files  # 获取文件后缀
        if suffix == '.json':
            with open(file_path, 'r', encoding="utf-8") as fp:
                data = json.load(fp)
        else:
            logging.error('文件后缀名错误')
    else:
        logging.error('文件路径不存在')
    return data

test_cases = soup.find_all('test-case')
for test_case in test_cases:
    name = test_case.get('name')
    description = test_case.description.text
    status = test_case.status.get('status')
    # 输出测试用例信息
    print('Test Case Name: ' + name)
    print('Description: ' + description)
    print('Status: ' + status)

steps = test_case.find_all('step')
for step in steps:
    name = step.name.text
    status = step.status.get('status')
    # 输出测试步骤信息
    print('Step Name: ' + name)
    print('Status: ' + status)

time = test_case.time.get('duration')
# 输出测试执行时间信息
print('Test Execution Time: ' + time + ' ms')

test_suite = soup.find('test-suite')
passed = test_suite.statistic.get('passed')
failed = test_suite.statistic.get('failed')
skipped = test_suite.statistic.get('skipped')
# 输出测试结果统计信息
print('Tests Passed: ' + passed)
print('Tests Failed: ' + failed)
print('Tests Skipped: ' + skipped)
'''

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:42:26 2023

@author: fkxxgis
"""

import json
from openpyxl import Workbook
jpath = 'C:/Users/EDY/Desktop/self_study/pytest_projects/report/temp/1e80a343-2ba2-4a1d-8ff3-cf7fcf9d3848-result.json'

def get_json_data(jpath):
    with open(jpath, 'r',encoding="utf-8") as f:
        data = json.load(f)
    for i in data:
        print(data[i])
    return data

def write_excel(data):
    wb = Workbook()
    ws = wb.active

    header = ["test_name", "test_status"]
    ws.append(header)

    for row in data:
        test_name = row[0]
        test_status = row[1]

        ws.append([test_name, test_status])

    wb.save('C:/Users/EDY/Desktop/report.xlsx')


if __name__=='__main__':
    jpath = 'C:/Users/EDY/Desktop/self_study/pytest_projects/report/temp/1e80a343-2ba2-4a1d-8ff3-cf7fcf9d3848-result.json'
    a=get_json_data(jpath)
    print(a)
    #write_excel(a)

