from pymysql import Connection

class Dbconnect_mysql():
    def __init__(self):
        self.conn = Connection(
            host='sh-tdsqlshard-ob3i44x2.sql.tencentcdb.com',
            user='agnes',
            password="Hex!1324",
            port=29452,
            database="agnes",
            charset="utf8"
        )

    #查询
    def select(self,sql):
        self.cursor = self.conn.cursor()  # 获取游标对象
        # conn.select_db("agnes")  # 选择数据库
        self.cursor.execute(sql)  # 查询语句

        result = self.cursor.fetchall()  # 获取查询结果
        return result

    # 插入
    def excute(self,sql):
        self.cursor = self.conn.cursor()  # 获取游标对象
        #conn.select_db("test_database")  # 选择数据库

        # 插入语句
        self.cursor.execute(sql)
        self.conn.commit()  # 提交事务

    #关闭
    def close(self):
        self.cursor.close()  # 关闭游标
        self.conn.close()  # 关闭连接



if __name__=='__main__':
    a=Dbconnect_mysql()
    result=a.select("select * from ac_re_task_def where TASK_ID='1j6tzf1f5spss'")
    print(result)
    a.close()


