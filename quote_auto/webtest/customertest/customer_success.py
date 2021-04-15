from quote_auto.basic.usebrowser import UseBrowser
from quote_auto.page.customerpage import CustomerPage


class CustomerSucceedTest:

    def set_up(self):
        self.customer_page=CustomerPage()

    def addcustomer_case_1(self):
        self.customer_page.add_customer('c1234545','','','','')
        text = self.customer_page.get_success_text()
        if text == '添加记录成功！':
            print('add_customer_case_1 pass')
        else:
            print('add_customer_case_1  failed')

    def addcustomer_case_2(self):
        self.customer_page.add_customer('c123576','sdfs','','','')
        text=self.customer_page.get_success_text()
        if text=='添加记录成功！':
            print('add_customer_case_2 pass')
        else:
            print('add_customer_case_2  failed')
    def addcustomer_case_3(self):
        self.customer_page.add_customer('c12352876','sdfs','123456543','','')
        text = self.customer_page.get_success_text()
        if text == '添加记录成功！':
            print('add_customer_case_3 pass')
        else:
            print('add_customer_case_3  failed')

    def addcustomer_case_4(self):
        self.customer_page.add_customer('c1236666412','sd4fs','12346654','v5fre','')
        text = self.customer_page.get_success_text()
        if text == '添加记录成功！':
            print('add_customer_case_4 pass')
        else:
            print('add_customer_case_4  failed')


    def tear_down(self):
        UseBrowser.quit()


if __name__ =='__main__':
    customer=CustomerSucceedTest()
    customer.set_up()
    # customer.addcustomer_case_1()
    # customer.addcustomer_case_2()
    # customer.addcustomer_case_3()
    customer.addcustomer_case_4()
    customer.tear_down()