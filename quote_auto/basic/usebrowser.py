import time
from selenium import webdriver

class UseBrowser:

    driver=None

    def __init__(self,browser_name):
        if browser_name=='Chrome':
            self.driver=webdriver.Chrome('../../chromedriver.exe')
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            UseBrowser.driver=self.driver
        else:
            # 打开火狐浏览器，注意这里传输的是谷歌浏览器，因为本机并无火狐浏览器驱动
            self.driver=webdriver.firefox('../chromedriver.exe')

    @classmethod
    def quit(cls):
        cls.driver.quit()


# if __name__=='__main__':
#     ub=UseBrowser()
#     time.sleep(3)
#     UseBrowser.quit()