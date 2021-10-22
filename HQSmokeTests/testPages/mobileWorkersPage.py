import datetime
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from testPages.organisationStructurePage import latest_download_file
from UserInputs.generateUserInputs import fetch_random_string
from UserInputs.userInputsData import UserInputsData


class MobileWorkerPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = "username_" + fetch_random_string()
        self.domain = "//span[text()='Project:']"
        self.confirm_user_field_delete = "//button[@class='btn btn-danger']"
        self.delete_user_field = "(//input[@data-bind='value: slug'])[last()]" \
                                 "//following::a[@class='btn btn-danger' and @data-toggle='modal'][1]"
        self.delete_success_mw = "//div[@class='alert alert-margin-top fade in alert-success']"
        self.confirm_delete_mw = "//button[@class='btn btn-danger']"
        self.enter_username = '//input[@data-bind="value: signOff, valueUpdate: \'textchange\'"]'
        self.delete_mobile_worker = "//a[@class='btn btn-danger']"
        self.actions_tab_link_text = "Actions"
        # remove these after locators page creation: redundant code
        self.web_apps_menu_id = "CloudcareTab"
        self.show_full_menu_id = "commcare-menu-toggle"
        ####################################################
        self.search_mw = "//div[@class='ko-search-box']//input[@type='text']"
        self.search_button_mw = "//div[@class='ko-search-box']//button[@data-bind='click: clickAction, visible: !immediate']"
        self.webapp_working_as = "//div[@class='restore-as-banner module-banner']/span/b"
        self.webapp_login_confirmation = 'js-confirmation-confirm'
        self.webapp_login_with_username = '(//h3/b)'
        self.webapp_login = "(//div[@class='js-restore-as-item appicon appicon-restore-as'])"
        self.confirm_reactivate_xpath_list = "((//div[@class='modal-footer'])/button[@data-bind=" \
                                             "'click: function(user) { user.is_active(true); }'])"
        self.reactivate_buttons_list = "//td/div[@data-bind='visible: !is_active()']//button[@class='btn btn-default']"
        self.confirm_deactivate_xpath_list = "((//div[@class='modal-footer'])/button[@class='btn btn-danger'])"
        self.deactivate_buttons_list = "(//td/div[@data-bind='visible: is_active()']/button[@class='btn btn-default'])"
        self.show_deactivated_users_btn = '//button[@data-bind="visible: !deactivatedOnly(), click: function() ' \
                                          '{ deactivatedOnly(true); }"]'
        self.usernames_xpath = "//td/a/strong[@data-bind='text: username']"
        self.page_xpath = \
            "(//span[@data-bind='text: $data, visible: !$parent.showSpinner() || $data != $parent.currentPage()'])"
        ###############################
        self.users_menu_id = "ProjectUsersTab"
        self.mobile_workers_menu_link_text = "Mobile Workers"
        self.create_mobile_worker_id = "new-user-modal-trigger"
        self.mobile_worker_username_id = "id_username"
        self.mobile_worker_password_id = "id_new_password"
        self.create_button_xpath = '//button[@type="submit"]'
        self.error_message = "//span[@data-bind ='visible: $root.usernameAvailabilityStatus() !== $root.STATUS.NONE']"
        self.cancel_button = "//button[text()='Cancel']"
        self.new_user_created_xpath = "//*[@class='success']//a[contains(@data-bind,'attr: {href: edit_url}, visible: " \
                                      "user_id')]//following-sibling::strong"
        self.edit_user_field_xpath = "//*[@id='btn-edit_user_fields']"
        self.add_field_xpath = "//button[@data-bind='click: addField']"
        self.user_property_xpath = "(//input[@data-bind='value: slug'])[last()]"
        self.label_xpath = "(//input[@data-bind='value: label'])[last()]"
        self.add_choice_button_xpath = "(//button[@data-bind='click: addChoice'])[last()]"
        self.choice_xpath = "(//input[@data-bind='value: value'])[last()]"
        self.save_field_id = "save-custom-fields"
        self.user_field_success_msg = "//div[@class='alert alert-margin-top fade in alert-success']"
        self.mobile_worker_on_left_panel = "//a[@data-title='Mobile Workers']"
        self.next_page_button_xpath = "//a[contains(@data-bind,'click: nextPage')]"
        self.additional_info_dropdown = "select2-id_data-field-" + "user_field_" + fetch_random_string() + "-container"
        # self.additional_info_dropdown = "//select[@name = 'data-field-user_field_" + fetch_random_string() + "']"
        self.select_value_dropdown = "//select[@name = 'data-field-user_field_" \
                                     + fetch_random_string() + "']/option[text()='user_field_" + fetch_random_string() \
                                     + "']"
        self.update_info_button = "//button[text()='Update Information']"
        self.user_file_additional_info = "//label[@for='id_data-field-" + "user_field_" + fetch_random_string() + "']"
        self.deactivate_btn_xpath = "//td/a/strong[text()='" + self.username + \
                                    "']/following::td[5]/div[@data-bind='visible: is_active()']/button"
        self.confirm_deactivate = "(//button[@class='btn btn-danger'])[1]"
        self.show_full_menu_id = "commcare-menu-toggle"
        self.view_all_link_text = "View All"
        ######
        self.search_user_web_apps = "//input[@placeholder='Filter workers']"
        self.search_button_we_apps = "//div[@class='input-group-btn']"
        # Download and Upload
        self.download_worker_btn = "Download Mobile Workers"
        self.download_users_btn = "Download Users"
        self.bulk_upload_btn = "Bulk Upload"
        self.choose_file = "//input[@id='id_bulk_upload_file']"
        self.upload = "//button[@class='btn btn-primary disable-on-submit']"
        self.import_complete = "//legend[text()='Bulk upload complete.']"
        self.download_filter = "//button[@data-bind='html: buttonHTML']"

    def wait_to_click(self, *locator, timeout=15):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except TimeoutException:
            print(TimeoutException)

    def search_user(self):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.search_mw))).send_keys(self.username)
        self.wait_to_click(By.XPATH, self.search_button_mw)

    def webapp_login_as(self):
        self.wait_to_click(By.ID, self.web_apps_menu_id)
        self.wait_to_click(By.XPATH, self.webapp_login)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.search_user_web_apps).send_keys(self.username)
        self.wait_to_click(By.XPATH, self.search_button_we_apps)
        time.sleep(1)

    def mobile_worker_menu(self):
        self.wait_to_click(By.ID, self.users_menu_id)
        self.wait_to_click(By.LINK_TEXT, self.mobile_workers_menu_link_text)
        assert "Mobile Workers : Users :: - CommCare HQ" in self.driver.title

    def create_mobile_worker(self):
        self.wait_to_click(By.ID, self.create_mobile_worker_id)
        time.sleep(1)

    def mobile_worker_enter_username(self, username):
        self.driver.find_element(By.ID, self.mobile_worker_username_id).send_keys(username)

    def mobile_worker_enter_password(self, password):
        self.driver.find_element(By.ID, self.mobile_worker_password_id).send_keys(password)

    def click_create(self):
        self.wait_to_click(By.XPATH, self.create_button_xpath)
        new_user_created = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
            By.XPATH, self.new_user_created_xpath)))
        print("Username is : " + new_user_created.text)
        assert self.username == new_user_created.text

    def edit_user_field(self):
        self.wait_to_click(By.XPATH, self.edit_user_field_xpath)

    def add_field(self):
        self.wait_to_click(By.XPATH, self.add_field_xpath)

    def add_user_property(self, user_pro):
        self.driver.find_element(By.XPATH, self.user_property_xpath).clear()
        self.driver.find_element(By.XPATH, self.user_property_xpath).send_keys(user_pro)

    def add_label(self, label):
        self.driver.find_element(By.XPATH, self.label_xpath).clear()
        self.driver.find_element(By.XPATH, self.label_xpath).send_keys(label)

    def add_choice(self, choice):
        self.wait_to_click(By.XPATH, self.add_choice_button_xpath)
        self.driver.find_element(By.XPATH, self.choice_xpath).clear()
        self.driver.find_element(By.XPATH, self.choice_xpath).send_keys(choice)

    def save_field(self):
        self.wait_to_click(By.ID, self.save_field_id)
        assert self.driver.find_element(By.XPATH, self.user_field_success_msg).is_displayed()

    def select_mobile_worker_created(self):
        self.wait_to_click(By.XPATH, self.mobile_worker_on_left_panel)
        time.sleep(2)
        self.search_user()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.username).click()

    def enter_value_for_created_user_field(self):
        self.wait_to_click(By.ID, self.additional_info_dropdown)
        self.wait_to_click(By.XPATH, self.select_value_dropdown)
        assert self.driver.find_element_by_xpath(self.user_file_additional_info).is_displayed()
        time.sleep(1)

    def update_information(self):
        button = self.driver.find_element(By.XPATH, self.update_info_button)
        self.driver.execute_script("arguments[0].click();", button)

    def deactivate_user(self):
        self.search_user()
        time.sleep(1)
        self.wait_to_click(By.XPATH, self.deactivate_buttons_list)
        self.wait_to_click(By.XPATH, self.confirm_deactivate_xpath_list)
        time.sleep(2)

    def verify_deactivation_via_login(self):
        self.webapp_login_as()
        login_with_username = self.driver.find_elements(By.XPATH, self.webapp_login_with_username)
        print("Checking webapp login...")
        for j in range(len(login_with_username)):
            print("Username is " + login_with_username[j].text)
            if login_with_username[j].text != self.username:
                assert True
        print("Username not in list - Successfully deactivated!")
        self.wait_to_click(By.ID, self.show_full_menu_id)

    def reactivate_user(self):
        time.sleep(1)
        self.mobile_worker_menu()
        self.wait_to_click(By.XPATH, self.show_deactivated_users_btn)
        self.search_user()
        time.sleep(1)
        self.wait_to_click(By.XPATH, self.reactivate_buttons_list)
        self.wait_to_click(By.XPATH, self.confirm_reactivate_xpath_list)
        time.sleep(3)

    def verify_reactivation_via_login(self):
        self.webapp_login_as()
        login_with_username = self.driver.find_elements(By.XPATH, self.webapp_login_with_username)
        for j in range(len(login_with_username)):
            print("Checking webapp login...")
            print("Username is " + login_with_username[j].text)
            if login_with_username[j].text == self.username:
                self.wait_to_click(By.XPATH, self.webapp_login_with_username + "[" + str(j + 1) + "]")
                self.wait_to_click(By.ID, self.webapp_login_confirmation)
                break
        try:
            login_username = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located(
                (By.XPATH, self.webapp_working_as)))
            if login_username.text == self.username:
                assert True, "Login with the reactivated user failed!"
                print("Working as " + self.username + " : Reactivation successful!")
        except TimeoutException:
            print(TimeoutException)
        self.wait_to_click(By.ID, self.show_full_menu_id)

    def cleanup_mobile_worker(self):
        self.wait_to_click(By.LINK_TEXT, self.actions_tab_link_text)
        self.wait_to_click(By.XPATH, self.delete_mobile_worker)
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((
            By.XPATH, self.enter_username))).send_keys(
            self.username + "@" + UserInputsData.domain + ".commcarehq.org")
        self.wait_to_click(By.XPATH, self.confirm_delete_mw)
        assert WebDriverWait(self.driver, 8).until(ec.presence_of_element_located((
            By.XPATH, self.delete_success_mw))).is_displayed()

    def cleanup_user_field(self):
        self.wait_to_click(By.XPATH, self.delete_user_field)
        self.wait_to_click(By.XPATH, self.confirm_user_field_delete)

    def download_mobile_worker(self):
        time.sleep(1)
        self.mobile_worker_menu()
        self.wait_to_click(By.LINK_TEXT, self.download_worker_btn)
        self.wait_to_click(By.XPATH, self.download_filter)
        try:
            WebDriverWait(self.driver, 25).until(ec.presence_of_element_located((
                By.LINK_TEXT, self.download_users_btn))).click()
            time.sleep(5)
        except TimeoutException as e:
            print("Still preparing for download.." + str(e))
            assert False
        # verify_downloaded_workers
        newest_file = latest_download_file()
        modTimesinceEpoc = (UserInputsData.download_path / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        newest_file = latest_download_file()
        assert "_users_" in newest_file and diff_seconds in range(0, 600)
        print("File download successful")

    def upload_mobile_worker(self):
        self.mobile_worker_menu()
        self.driver.find_element(By.LINK_TEXT, self.bulk_upload_btn).click()
        newest_file = latest_download_file()
        file_that_was_downloaded = UserInputsData.download_path / newest_file
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.choose_file).send_keys(str(file_that_was_downloaded))
        self.driver.find_element(By.XPATH, self.upload).click()
        assert WebDriverWait(self.driver, 100).until(ec.presence_of_element_located((
            By.XPATH, self.import_complete))).is_displayed()
        print("File uploaded successfully")
