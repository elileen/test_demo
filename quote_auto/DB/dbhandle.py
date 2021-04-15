# -*- coding: utf-8 -*-
# Datetime： 2021-04-13 14:46 
# Author： elileen
# QQ：2049146393
import pymysql



class DBHandle:
    def __init__(self,host,port,database,username,password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    # 获取数据库连接
    def get_connect(self):
        try:
            conn = pymysql.connect(host=self.host, port=self.port, database=self.database,
                                        user=self.username, password=self.password, charset='utf8')
            return conn
        except Exception as e:
            print(e,'\n connect failed!')

    # 查询数据
    def sql_search(self,sql,para):
        res = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql,para)
            res = cursor.fetchall()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e,'\nsql operation error！')
        finally:
            cursor.close()
            conn.close()

        return res

    # 修改数据
    def sql_modify(self,sql,para):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql,para)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e, '\nsql operation error！')
        finally:
            cursor.close()
            conn.close()


db=DBHandle('localhost',3306,'quote','root','123456')
db.sql_modify('delete from tb_customer where customerNO=%s',["234567头大"])


