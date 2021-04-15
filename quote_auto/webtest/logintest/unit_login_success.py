import time
import unittest
import sys
sys.path.append('D:\\GXA\\Python\\PyCharm\\PythonProject\\Project01')
from HwTestReport import HTMLTestReportEN
from HTMLTestRunner import HTMLTestRunner
from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.page.loginpage import LoginPage
from quote_auto.unit.exl_operation import ExlOperation
from quote_auto.webtest.customertest.unit_customer_success import CustomerSuccessCase
from quote_auto.webtest.logintest.unit_login_failed import LoginFailedCase


class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.exl_op = ExlOperation('../../config/logincase.xlsx')

    # def test_1_login_success(self):
    #     self.login_page.login('lili', 'lili1234')
    #     self.assertEqual(self.login_page.get_success_text(),'欢迎使用报价管理系统')

    def test_1_login_success(self):
        self.login_page.login(self.exl_op.get_cell_value(1,2),self.exl_op.get_cell_value(1,3))
        self.assertEqual(self.login_page.get_success_text(),self.exl_op.get_cell_value(1,4))

    def tearDown(self) -> None:
        UseBrowser.quit()
    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    # 测试套件
    suite = unittest.TestSuite()
    # 加载case
    login_failed_test = unittest.TestLoader().loadTestsFromTestCase(LoginFailedCase)
    login_successed_test = unittest.TestLoader().loadTestsFromTestCase(LoginSuccessCase)
    cuctomer_success_test = unittest.TestLoader().loadTestsFromTestCase(CustomerSuccessCase)
    # case加入到测试套件
    case_count = [login_failed_test, login_successed_test, cuctomer_success_test]
    # case_count=[login_successed_test,login_failed_test]
    suite.addTests(case_count)
    '''
    # # 需要一个文本测试运行对象
    # runner = unittest.TextTestRunner(verbosity=2)
    '''
    # 生成报告的方式运行对象
    # 设置报告文件的时间
    # file_date=time.strftime('%Y-%m-%d_%H_%M_%S')
    # 写入报告的文件
    # fp=open('../../report/'+file_date+'.html','wb+')
    with open('../../report/report.html','wb+') as fp:

        runner=HTMLTestReportEN(stream=fp, verbosity=2, title='Quote Project', description='UI Auto Test')
        # 执行套件case
        runner.run(suite)
    # fp.close()
