import pymysql
from allure_commons import logger
from pymysql.cursors import DictCursor


class Dbconnect():
    def __init__(self,dbinfo):
        self.db=pymysql.connect(cursorclass=pymysql.cursors.DictCursor,**dbinfo)
        self.cursor=self.db.cursor()


    def select(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result

    def excute(self,sql2):
        try:
            self.cursor.excute(sql2)
            self.db.commit()
        except Exception as e:
            print("错误",e)
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()


    def get_result(self,sql,filename):
        results=self.select(sql)
        print("记录数:{}".format(len(results)))
        with open(filename,'w') as f:
            for one in results:
                f.write(str(one)+'\n')

        return results


if __name__=='__main__':
    dbinfo = {
        "host": "sh-tdsqlshard-ob3i44x2.sql.tencentcdb.com",
        "user": "agnes",
        "password": "Hex!1324",
        "port": "29452",
        "database": "agnes",
        "charset": "utf8"
    }
    mysql=pymysql.connect(dbinfo)
    result=mysql.select("SELECT * FROM `ac_hi_case_step_exec_log` where PK_ID='1ivthwi7m7swg'")
    print(result)
    mysql.close()
