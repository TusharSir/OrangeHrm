import time

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

#service_obj = Service()
driver = webdriver.Chrome()

driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print(driver.title)
driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
act_title = driver.title
if act_title == "OrangeHRM1":
        driver.save_screenshot("D:\\Credence Python Projects by Tushar Sir\\OrangeHrm\\ScreenShots\\homePageTitle-pass.png")
        assert True
        driver.close()
        #logger.info("******************Home Page Title Pass **************")
else:
        driver.save_screenshot("D:\\Credence Python Projects by Tushar Sir\\OrangeHrm\\ScreenShots\\homePageTitle-fail.png")
        driver.close()
        #logger.info("******************Home Page Title Fail **************")
        assert False
