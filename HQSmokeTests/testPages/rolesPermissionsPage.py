import time

from HQSmokeTests.UserInputs.generateUserInputs import fetch_random_string
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class RolesPermissionPage:

    def __init__(self, driver):
        self.driver = driver
        self.roles_menu_xpath = "//a[@data-title='Roles & Permissions']"
        self.add_role_btn_xpath = "//button[@data-bind='click: function () {$root.setRoleBeingEdited($root.defaultRole)}']"
        self.role_name_id = "role-name"
        self.edit_web_user_checkbox = "edit-web-users-checkbox"
        self.save_btn_xpath = "//button[@class='btn btn-primary disable-on-submit']"
        self.role_created = "//span[text()='" + "role_name_" + fetch_random_string() + "']"
        self.edit_role_xpath = "//span[text()='" + "role_name_" + fetch_random_string() + "']//following::td[10]/button[1]"
        self.delete_role_xpath = "//span[text()='" + "role_name_" + fetch_random_string() + "']//following::td[10]/button[2]"
        self.edit_mobile_worker_checkbox = "edit-commcare-users-checkbox"
        self.role_renamed = "//span[text()='" + "role_name_" + fetch_random_string() + "']"
        self.confirm_role_delete = "//div[@class='btn btn-danger']"

    def wait_to_click(self, *locator, timeout=3):
        clickable = ec.element_to_be_clickable(locator)
        element = WebDriverWait(self.driver, timeout).until((clickable))
        element.click()

    def roles_menu_click(self):
        self.wait_to_click(By.XPATH, self.roles_menu_xpath)
        assert "Roles & Permissions : Users :: - CommCare HQ" in self.driver.title

    def add_role(self):
        self.wait_to_click(By.XPATH, self.add_role_btn_xpath)
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((
            By.ID, self.role_name_id))).clear()
        self.driver.find_element(By.ID, self.role_name_id).send_keys("role_name_" + fetch_random_string())
        self.driver.find_element(By.ID, self.edit_web_user_checkbox).click()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).perform()
        assert True == WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
            By.XPATH, self.role_created))).is_displayed()

    def edit_role(self):
        self.driver.find_element(By.XPATH, self.edit_role_xpath).click()
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((
            By.ID, self.role_name_id))).clear()
        self.driver.find_element(By.ID, self.role_name_id).send_keys("role_name_" + fetch_random_string())
        self.driver.find_element(By.ID, self.edit_mobile_worker_checkbox).click()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).perform()
        assert True == WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
            By.XPATH, self.role_renamed))).is_displayed()
        time.sleep(1)

    def cleanup_role(self):
        self.wait_to_click(By.XPATH, self.delete_role_xpath)
        self.wait_to_click(By.XPATH, self.confirm_role_delete)
