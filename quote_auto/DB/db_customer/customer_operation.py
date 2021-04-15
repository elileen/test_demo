# -*- coding: utf-8 -*-
# Datetime： 2021-04-13 14:57 
# Author： elileen
# QQ：2049146393
from quote_auto.DB.dbhandle import DBHandle

class DB_CustomerOp:

    def __init__(self):
        self.db_handle = DBHandle('localhost',3306,'quote','root','123456')

    def del_custoemr_by_custonerNO(self,custonerNO):
        self.db_handle.sql_modify('delete from tb_customer where customerNO=%s',[custonerNO])

    # 查询某个数据与页面查询的数据进行对比查看是否添加成功
    def search_id_name(self,id):
        res = self.db_handle.sql_search('select customerNO,customerName from tb_customer where customerNO=%s',id)
        return list(res[0])

    # 查询客户的编号，姓名，电话，地址，联系人进行对比查看是否添加成功
    def search_four_text(self,id):
        res = self.db_handle.sql_search('select customerNO,customerName,phone,address,relationman '
                                        'from tb_customer where customerNO=%s',id)
        return  list(res[0])

# db_cus=DB_CustomerOp()
# print(db_cus.search_four_text('0012345'))
# print(db_cus.search_id_name('12346237'))
# db_cus.del_custoemr_by_custonerNO('1234')