from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
driver = None

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print ("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print ("Launching FireFox browser")
    else:
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # chrome_options.add_argument("--ignore-certificate-errors")
        # service_obj = Service()
        # driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        #driver = webdriver.Firefox()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")

        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(2)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

