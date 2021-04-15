import unittest

from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.webtest.customertest.unit_customer_success import CustomerSuccessCase
from quote_auto.webtest.logintest.unit_login_failed import LoginFailedCase
from quote_auto.webtest.logintest.unit_login_success import LoginSuccessCase


# class MyTestCase(unittest.TestCase):

    # def tearDown(self) -> None:
    #     UseBrowser.quit()
    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    # unittest.main()
    # 测试套件
    suite = unittest.TestSuite()
    # 加载case
    login_failed_test = unittest.TestLoader().loadTestsFromTestCase(LoginFailedCase)
    login_successed_test = unittest.TestLoader().loadTestsFromTestCase(LoginSuccessCase)
    add_suctomer_success_test=unittest.TestLoader().loadTestsFromTestCase(CustomerSuccessCase)
    # case加入到测试套件
    case_count = [login_failed_test, login_successed_test,add_suctomer_success_test]
    suite.addTest(case_count)
    # 需要一个文本测试运行对象
    runner = unittest.TextTestRunner(verbosity=2)
    # 执行套件case
    runner.run(suite)