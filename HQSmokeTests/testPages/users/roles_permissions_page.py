import time

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string

from selenium.webdriver.common.by import By


class RolesPermissionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.role_name_created = "role_" + fetch_random_string()

        self.roles_menu = (By.XPATH, "//a[@data-title='Roles & Permissions']")
        self.add_new_role = (By.XPATH, "//button[@data-bind='click: function () {$root.setRoleBeingEdited($root.defaultRole)}']")
        self.role_name = (By.ID, "role-name")
        self.edit_web_user_checkbox = (By.ID, "edit-web-users-checkbox")
        self.save_button = (By.XPATH, "//button[@class='btn btn-primary disable-on-submit']")
        self.role_created = (By.XPATH, "//span[text()='" + str(self.role_name_created) + "']")
        self.edit_created_role = (By.XPATH, "//span[text()='" + str(self.role_name_created) + "']//following::td[10]/button[1]")
        self.delete_role = (By.XPATH, "//span[text()='" + str(self.role_name_created) + "']//following::td[10]/button[2]")
        self.edit_mobile_worker_checkbox = (By.ID, "edit-commcare-users-checkbox")
        self.role_renamed = (By.XPATH, "//span[text()='" + str(self.role_name_created) + "']")
        self.confirm_role_delete = (By.XPATH, "//div[@class='btn btn-danger']")

    def roles_menu_click(self):
        self.wait_to_click(self.roles_menu)
        assert "Roles & Permissions : Users :: - CommCare HQ" in self.driver.title

    def add_role(self):
        self.wait_to_click(self.add_new_role)
        self.wait_to_clear(self.role_name)
        self.send_keys(self.role_name, self.role_name_created)
        self.click(self.edit_web_user_checkbox)
        self.move_to_element_and_click(self.save_button)
        assert self.is_present_and_displayed(self.role_created), "Role not added successfully!"

    def edit_role(self):
        self.wait_to_click(self.edit_created_role)
        self.wait_to_clear(self.role_name)
        self.send_keys(self.role_name, self.role_name_created)
        self.move_to_element_and_click(self.edit_mobile_worker_checkbox)
        self.move_to_element_and_click(self.save_button)
        assert self.is_present_and_displayed(self.role_renamed), "Role not edited successfully!"
        time.sleep(1)

    def cleanup_role(self):
        self.wait_to_click(self.delete_role)
        self.wait_to_click(self.confirm_role_delete)
