from time import sleep
from pageObject.adminpage import Admin
from utilities.baseclass import BaseClass


class Test_admin_suite(BaseClass):

    def test_admin_page(self):
        user = Admin(self.driver)
        user.admin_page_link().click()
        user.add_button().click()
        user.click_drp().click()
        role = user.userrole_li()
        if role != "ESS":
            user.userrole_li().click()

        user.emp_name().send_keys("Awais")

        sleep(10)
