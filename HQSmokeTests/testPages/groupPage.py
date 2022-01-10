import time

from HQSmokeTests.userInputs.generateUserInputs import fetch_random_string
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class GroupPage:

    def __init__(self, driver):
        self.driver = driver
        self.group_name_id = "id_group_name"
        self.add_group_button = "//button[@type='submit' and @class='btn btn-primary']"
        self.group_menu_xpath = "//a[@data-title='Groups']"
        self.users_drop_down = "//span[@class='select2-selection select2-selection--multiple']"
        self.select_user = "//li[text()='" + "username_" + fetch_random_string() + "']"
        self.update_button_id = "submit-id-submit"
        self.created_group = "group_" + fetch_random_string()
        self.edit_settings_link_text = "Edit Settings"
        self.group_name_input_id = "group-name-input"
        self.save_button_xpath = "//button[@type='submit' and text()='Save']"
        self.success_alert_id = "save-alert"
        self.remove_user_xpath = "//button[@title='Remove item']"
        self.delete_group = "//a[@class='btn btn-danger pull-right']"
        self.confirm_delete = "//button[@class='btn btn-danger disable-on-submit']"
        self.delete_success_message = "//div[@class='alert alert-margin-top fade in html alert-success']"

    def wait_to_click(self, *locator, timeout=3):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()

        except TimeoutException:
            print(TimeoutException)

    def click_group_menu(self):
        self.wait_to_click(By.XPATH, self.group_menu_xpath)

    def add_group(self):
        WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
            By.ID, self.group_name_id))).send_keys(self.created_group)
        self.wait_to_click(By.XPATH, self.add_group_button)
        print("Group Added")

    def add_user_to_group(self):
        self.driver.find_element(By.XPATH, self.users_drop_down).send_keys("username_" + fetch_random_string())
        self.wait_to_click(By.XPATH, self.select_user)
        try:
            self.wait_to_click(By.ID, self.update_button_id)
            time.sleep(2)
            self.click_group_menu()
            assert WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((
                By.LINK_TEXT, self.created_group))).is_displayed()
        except UnexpectedAlertPresentException as e:
            print(e)
            print("User Added to Group")

    def edit_existing_group(self):
        time.sleep(2)
        self.wait_to_click(By.LINK_TEXT, self.created_group)
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present(), 'Waiting for popup to appear.')

            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
        self.wait_to_click(By.LINK_TEXT, self.edit_settings_link_text)
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((
            By.ID, self.group_name_input_id))).clear()
        self.driver.find_element(
            By.ID, self.group_name_input_id).send_keys(self.created_group + "_rename")
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        assert WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.success_alert_id))).is_displayed()
        print("Renamed a group")

    def remove_user_from_group(self):
        self.wait_to_click(By.XPATH, self.remove_user_xpath)
        update_button = self.driver.find_element(By.ID, self.update_button_id)
        self.driver.execute_script("arguments[0].click();", update_button)
        assert WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((
            By.ID, self.success_alert_id))).is_displayed()
        print("Removed added user from group")

    def cleanup_group(self):
        self.wait_to_click(By.LINK_TEXT, self.created_group + "_rename")
        self.wait_to_click(By.XPATH, self.delete_group)
        self.wait_to_click(By.XPATH, self.confirm_delete)
        assert WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((
            By.XPATH, self.delete_success_message))).is_displayed()
        print("Clean up added group")
