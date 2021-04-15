from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.page.loginpage import LoginPage
from quote_auto.unit.exl_operation import ExlOperation


class LoginSucceedTest:

    def set_up(self):
        self.login_page=LoginPage()
        self.exl_op = ExlOperation()

    def login_case_1(self):
        self.login_page.login('admin','123456')
        # self.login_page.get_success_text()
        if self.login_page.get_success_text() == '欢迎使用报价管理系统':
            print('login_success case pass')
        else:
            print('login_success case failed')

    def login_case_2(self):
        self.login_page.login('lili','lili1234')
        if self.login_page.get_success_text() == '欢迎使用报价管理系统':
            print('login_success case pass')
        else:
            print('login_success case failed')



    def tear_down(self):
        UseBrowser.quit()

if __name__ == '__main__':
    login_success=LoginSucceedTest()
    login_success.set_up()
    login_success.login_case_2()
    login_success.tear_down()