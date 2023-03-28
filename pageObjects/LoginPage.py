from selenium.webdriver.common.by import By


class c_LoginScreenClass:
    text_UserName_Xpath = "//input[@placeholder='Username']"
    text_Passworde_Xpath = "//input[@placeholder='Password']"
    clk_LoginButton_Css = "button[type='submit']"
    clk_MenuButton_Xpath = "//span[@class='oxd-userdropdown-tab']"
    clk_LogoutButton_Css = "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > " \
                           "div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) " \
                           "> li:nth-child(4) > a:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.text_UserName_Xpath).clear()
        self.driver.find_element(By.XPATH, self.text_UserName_Xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_Passworde_Xpath).clear()
        self.driver.find_element(By.XPATH, self.text_Passworde_Xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.clk_LoginButton_Css).click()

    def menubutton(self):
        self.driver.find_element(By.XPATH, self.clk_MenuButton_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.clk_LogoutButton_Css).click()
