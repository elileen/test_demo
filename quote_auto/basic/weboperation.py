import time

from quote_auto.basic.usebrowser import UseBrowser


class WebOperation:

    def __init__(self,driver):
        self.driver=driver

    # 打开网站
    def open_url(self,url):
        self.driver.get(url)

    # 通过name定位并清空
    def clear_name(self,name_locator):
        self.driver.find_element_by_name(name_locator).clear()

    # 通过name定位并传输参数
    def input_text_name(self,name_locator,text):
        self.driver.find_element_by_name(name_locator).send_keys(text)

    # 通过xpath定位并传输参数
    def input_text_xpath(self,xpath_locator,text):
        self.driver.find_element_by_xpath(xpath_locator).send_keys(text)

    # 通过name定位并点击
    def click_name(self,name_locator):
        self.driver.find_element_by_name(name_locator).click()

    # 通过xpath定位并点击
    def click_xpath(self,xpath_locator):
        self.driver.find_element_by_xpath(xpath_locator).click()

    # 获取文本信息
    def get_text_xpath(self,xpath_locator):
        return self.driver.find_element_by_xpath(xpath_locator).text

    # 切换窗体
    def change_window(self,title):
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            if self.driver.title == title:
                break

    # 通过xpath切换frame框架
    def change_frame_element_xpath(self,xpath_locator):
        self.driver.switch_to.default_content()
        element=self.driver.find_element_by_xpath(xpath_locator)
        self.driver.switch_to.frame(element)

    # 通过name切换frame框架
    def change_frame_element_name(self,name_locator):
        self.driver.switch_to.default_content()
        element=self.driver.find_element_by_name(name_locator)
        self.driver.switch_to.frame(element)


# if __name__ == '__main__':
#     ub = UseBrowser('Chrome')
#     op = WebOperation(UseBrowser.driver)
#     op.open_url('http://localhost:8080/JavaPrj_6/login.do')
#     op.input_text_name('username','admin')
#     op.input_text_name('password', '123456')
#     time.sleep(3)
#     op.click_name('submit')
#     time.sleep(5)
#     UseBrowser.quit()



