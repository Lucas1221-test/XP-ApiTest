"""
@Filename:  testcase/database_util
@Describe:  ...
@Author:    dingxuhui
@Time:      2023/5/18 22:01
"""
import pymysql


#创建乘数据库链接
def create_connection():
    conn = pymysql.connect(
        user="root",
        password="admin123",
        host="localhost",
        database="phpwind",
        port=3306,)
    return conn


#执行sql语句
def execute_sql(sql):
    #创建游标
    conn = create_connection()
    cs = conn.cursor()
    try:
        #执行sq1
        cs.execute(sql)
        #提取值
        value = cs.fetchall()
    except Exception as e:
        print("查询用户数据出错：", e)
        value = None   # 添加默认值，避免在后续出现使用未赋值的情况

    #关闭链接
    cs.close()
    conn.close()
    return value
