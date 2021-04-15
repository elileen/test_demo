import unittest

from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.page.loginpage import LoginPage
from quote_auto.unit.exl_operation import ExlOperation


class LoginFailedCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def setUp(self) -> None:
        self.login_page=LoginPage()
        self.exl_op = ExlOperation('../../config/logincase.xlsx')

    def test_1_uname_upw_null(self):
        self.login_page.login(self.exl_op.get_cell_value(2,2),self.exl_op.get_cell_value(2,3))
        self.assertEqual(self.login_page.get_failed_text(),self.exl_op.get_cell_value(2,4))

    def test_2_upw_null(self):
        self.login_page.login(self.exl_op.get_cell_value(3,2),self.exl_op.get_cell_value(3,3))
        # self.login_page.login('lili', '')
        self.assertEqual(self.login_page.get_failed_text(),self.exl_op.get_cell_value(2,4))

    def test_3_uname_upw_error(self):
        self.login_page.login(self.exl_op.get_cell_value(4,2),self.exl_op.get_cell_value(4,3))
        self.assertEqual(self.login_page.get_failed_text(),self.exl_op.get_cell_value(2,4))

    def tearDown(self) -> None:
        UseBrowser.quit()



if __name__ == '__main__':
    unittest.main()
