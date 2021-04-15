from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.page.loginpage import LoginPage


class LoginFailedTest:

    def set_up(self):
        self.login_page=LoginPage()

    def login_case_1(self):
        self.login_page.login('admin','12345566')
        self.login_page.get_failed_text()


    def login_case_2(self):
        self.login_page.login('lili','lili156234')
        # text= self.login_page.get_failed_text()
        if self.login_page.get_failed_text()=='请勿非法登录！':
            print('login_failed case pass')
        else:
            print('login_failed case failed')


    def tear_down(self):
        UseBrowser.quit()

if __name__ == '__main__':
    login_faile=LoginFailedTest()
    login_faile.set_up()
    login_faile.login_case_2()
    login_faile.tear_down()