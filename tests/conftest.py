import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = None


# random browser selection method
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    # random browser selection through cmd
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        service_obj = Service("D:/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("D:/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("D:/IEDriverServer.exe")
        driver = webdriver.Ie(service=service_obj)
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys('Admin')
    driver.find_element(By.NAME, "password").send_keys('admin123')
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    request.cls.driver = driver
    yield
    driver.close()
