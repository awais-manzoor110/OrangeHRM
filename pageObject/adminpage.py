from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Admin:
    def __init__(self, driver):
        self.driver = driver

    admin_link = (By.XPATH, "//li[@class='oxd-main-menu-item-wrapper'][1]")
    add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    role_drp_click = (By.XPATH, '(//div[@class="oxd-select-text--after"])[1]')
    userrole_list = (By.XPATH, '(//div[@class="oxd-select-dropdown --positon-bottom"])[1]')
    eName = (By.XPATH, "//input[@placeholder='Type for hints...']")

    def admin_page_link(self):
        return self.driver.find_element(*Admin.admin_link)

    def add_button(self):
        return self.driver.find_element(*Admin.add_btn)

    def click_drp(self):
        return self.driver.find_element(*Admin.role_drp_click)

    def userrole_li(self):
        return self.driver.find_element(*Admin.userrole_list)

    def emp_name(self):
        return self.driver.find_element(* Admin.eName)


