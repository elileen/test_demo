import time

from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.basic.weboperation import WebOperation
from quote_auto.page.loginpage import LoginPage
from quote_auto.unit.exl_operation import ExlOperation


class CustomerPage:

    def __init__(self):
        self.ub = UseBrowser('Chrome')
        self.op = WebOperation(UseBrowser.driver)
        # self.exl_op=ExlOperation()

    # 添加客户
    def add_customer(self,customerNO,customerName,phone,address,relationman):
        self.op.open_url('http://localhost:8080/JavaPrj_6/login.do')
        self.op.input_text_name('username', 'admin')
        self.op.input_text_name('password', '123456')
        self.op.click_name('submit')
        self.op.change_frame_element_xpath('/html/frameset/frame[1]')
        time.sleep(1)
        self.op.click_xpath('//*[@id="Bar_panel0_b0"]/img')
        self.op.change_frame_element_name('main')
        self.op.click_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        self.op.change_window('新增客户信息')
        self.op.input_text_name('customerNO',customerNO)
        self.op.input_text_name('customerName',customerName)
        self.op.input_text_name('phone',phone)
        self.op.input_text_name('address',address)
        self.op.input_text_name('relationman', relationman)
        self.op.click_name('saveButton')

    def get_success_text(self):
        return self.op.get_text_xpath('html/body/center')[0:7]

    #遍历列表获取数据的行
    def find_by_cno(self,customerNO):
        i = 2
        while True:
            cNO=self.op.get_text_xpath('/html/body/center/form/table[1]/tbody/tr[{}]/td[1]'.format(i))
            time.sleep(1)
            if cNO==customerNO:
                return i
                break
            else:
                i+=2
                continue

    # 修改客户
    def modify_customer(self,customerNO,customerName,phone,address,relationman):
        self.op.open_url('http://localhost:8080/JavaPrj_6/login.do')
        self.op.driver.maximize_window()
        self.op.input_text_name('username', 'admin')
        self.op.input_text_name('password', '123456')
        self.op.click_name('submit')
        self.op.change_frame_element_xpath('/html/frameset/frame[1]')
        time.sleep(1)
        self.op.click_xpath('//*[@id="Bar_panel0_b0"]/img')
        self.op.change_frame_element_name('main')
        time.sleep(1)
        index=self.find_by_cno(customerNO)
        print(index)
        self.op.click_xpath('/html/body/center/form/table[1]/tbody/tr[{}]/td[7]/a[2]'.format(index))
        self.op.change_window('更新客户信息')
        time.sleep(1)
        self.op.clear_name('customerName')
        self.op.input_text_name('customerName',customerName)
        self.op.clear_name('phone')
        self.op.input_text_name('phone',phone)
        self.op.clear_name('address')
        self.op.input_text_name('address', address)
        self.op.clear_name('relationman')
        self.op.input_text_name('relationman', relationman)
        self.op.click_name('saveButton')

    # 删除客户
    def remove_customer(self):
        pass

    # 查询客户
    def search_customer(self):
        pass


# if __name__ == '__main__':
#     cus=CustomerPage()
#     cus.modify_customer('0012345','若12','1222222222','chydu','koko')
#     # cus.add_customer('c12445467','lolo','12345634565','成都','jojo')
#     cus.find_by_cno('0012345')
#     # cus.get_success_text()
#     UseBrowser.quit()
