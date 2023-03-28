import time

# from pageObjects.LoginPage import LoginPage
# from pageObjects.AddCustomerPage import AddCustomer
# from pageObjects.SearchCustomerPage import SearchCustomer
# from utilities.BaseClass import BaseClass
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
# from selenium import webdriver
# from selenium.webdriver.common.by import By

from pageObjects.LoginPage import c_LoginScreenClass
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login(BaseClass):
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserPassword()

    def test_login_001(self, setup):
        log = self.getLogger()
        log.info("******************test_login_001**************")
        log.info("******************Verifying Login**************")
        self.driver = setup
        self.LoginPage = c_LoginScreenClass(self.driver)
        time.sleep(2)
        log.info("******************Enter UserName **************")
        self.LoginPage.setUserName(self.username)
        log.info("******************Enter Password **************")
        self.LoginPage.setPassword(self.password)
        log.info("******************Click On Login button **************")
        self.LoginPage.clickLogin()
        time.sleep(2)
        self.LoginPage.menubutton()
        time.sleep(2)
        self.LoginPage.clickLogout()
        log.info("****************** Click On Logout button **************")
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\OrangeHrm\\ScreenShots\\homePageTitle-pass2.png")
            assert True
            log.info("******************test_login_001 Passed **************")
            self.driver.close()
            # logger.info("******************Home Page Title Pass **************")
        else:
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\OrangeHrm\\ScreenShots\\homePageTitle-fail2.png")
            self.driver.close()
            log.info("******************test_login_001 Passed **************")
            # logger.info("******************Home Page Title Fail **************")
            assert False
        log.info("******************test_login_001 Execution Completed **************")
