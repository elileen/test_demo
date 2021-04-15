from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.basic.weboperation import WebOperation
from quote_auto.unit.exl_operation import ExlOperation
from quote_auto.unit.log_info import LogInfo
from quote_auto.unit.yaml_operation import YamlOperation


class LoginPage:

    def __init__(self):
        self.ub = UseBrowser('Chrome')
        self.op = WebOperation(UseBrowser.driver)
        self.exlop=ExlOperation('../../config/logincase.xlsx')
        self.yaml_op=YamlOperation('../../config/AutoCase.yml')
        self.log=LogInfo()
    # 登录
    def login(self,username,password):
        try:
            self.log.set_message('info','打开quote网址')
            self.op.open_url(self.exlop.get_cell_value(1,1))
            self.log.set_message('info', '输入用户名:'+username)
            self.op.input_text_name(self.yaml_op.get_locator('LoginPage','username'),username)
            self.log.set_message('info','输入密码:'+password)
            self.op.input_text_name(self.yaml_op.get_locator('LoginPage','password'),password)
            self.log.set_message('info','点击提交')
            self.op.click_name(self.yaml_op.get_locator('LoginPage','submit'))
        except Exception as e:
            self.log.set_message('error',e)

    # 获取登录成功的信息,判断是否成功
    def get_success_text(self):
        self.op.change_frame_element_name('main')
        return self.op.get_text_xpath(self.yaml_op.get_locator('LoginPage','successinfo'))
        # text = self.op.get_text_xpath('/html/body/table/tbody/tr[1]/td/span')
        # if text == '欢迎使用报价管理系统':
        #     print('login_success case pass')
        # else:
        #     print('login_success case failed')

    # 获取登录失败的信息
    def get_failed_text(self):
        return self.op.get_text_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')
        # text=self.op.get_text_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')
        # if text=='请勿非法登录！':
        #     print('login_failed case pass')
        # else:
        #     print('login_failed case failed')

# if __name__ == '__main__':
#     loginpage = LoginPage()
#     loginpage.login('admin',123456)
#     loginpage.get_success_text()
#     UseBrowser.quit()

