import unittest

from quote_auto.DB.db_customer.customer_operation import DB_CustomerOp
from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.page.customerpage import CustomerPage
from quote_auto.unit.exl_operation import ExlOperation


class CustomerSuccessCase(unittest.TestCase):

    def setUp(self) -> None:
        self.customer_page = CustomerPage()
        self.db_customerop=DB_CustomerOp()
        self.exl_op = ExlOperation('../../config/logincase.xlsx','customer用例参数')

    def test_addcustomer_only_cNo(self):
        self.db_customerop.del_custoemr_by_custonerNO('c0096501')
        self.customer_page.add_customer('c0096501', '', '', '', '')
        self.assertEqual(self.customer_page.get_success_text(),'添加记录成功！')
        self.db_customerop.del_custoemr_by_custonerNO('c0096501')

    def test_addcustomer_cNO_cName(self):
        self.db_customerop.del_custoemr_by_custonerNO('c0096502')
        self.customer_page.add_customer('c0096502', 'mika', '', '', '')
        self.assertEqual(self.customer_page.get_success_text(),'添加记录成功！')
        self.db_customerop.del_custoemr_by_custonerNO('c0096502')

    def test_addcustomer_address_rman_null(self):
        self.db_customerop.del_custoemr_by_custonerNO('c0096503')
        self.customer_page.add_customer('c0096503', 'qinlin', '345645676733', '', '')
        self.assertEqual(self.customer_page.get_success_text(),'添加记录成功！')
        self.db_customerop.del_custoemr_by_custonerNO('c0096503')

    def test_addcustomer_rman_null(self):
        self.db_customerop.del_custoemr_by_custonerNO('c0096504')
        self.customer_page.add_customer('c0096504', 'hema', '45634453', 'New York', '')
        self.assertEqual(self.customer_page.get_success_text(),'添加记录成功！')
        self.db_customerop.del_custoemr_by_custonerNO('c0096504')

    def test_modify_customer_all(self):
        cno=self.exl_op.get_cell_value(1,2)
        lst = self.db_customerop.search_four_text(cno)
        cname=self.exl_op.get_cell_value(1,3)
        cphone=self.exl_op.get_cell_value(1,4)
        caddress=self.exl_op.get_cell_value(1,5)
        cman=self.exl_op.get_cell_value(1,6)
        text=self.exl_op.get_cell_value(1,7)
        self.customer_page.modify_customer(cno,cname,cphone,caddress,cman)
        self.assertEqual(self.customer_page.get_success_text(),text)
        self.customer_page.modify_customer(lst[0],lst[1],lst[2],lst[3],lst[4])

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    unittest.main()
