import time

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.userInputs.user_inputs import UserData
from HQSmokeTests.testPages.users.org_structure_page import latest_download_file
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


class MobileWorkerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username = "username_" + fetch_random_string()
        self.login_as_usernames = '(//h3/b)'

        self.username_link = (By.LINK_TEXT, self.username)
        self.confirm_user_field_delete = (By.XPATH, "//button[@class='btn btn-danger']")
        self.delete_user_field = (By.XPATH, "(//input[@data-bind='value: slug'])[last()]//following::a[@class='btn btn-danger' and @data-toggle='modal'][1]")
        self.delete_success_mw = (By.XPATH, "//div[@class='alert alert-margin-top fade in alert-success']")
        self.confirm_delete_mw = (By.XPATH, "//button[@class='btn btn-danger']")
        self.enter_username = (By.XPATH, '//input[@data-bind="value: signOff, valueUpdate: \'textchange\'"]')
        self.delete_mobile_worker = (By.XPATH, "//a[@class='btn btn-danger']")
        self.actions_tab_link_text = (By.LINK_TEXT, "Actions")
        # remove these two after locators page creation: redundant code
        self.web_apps_menu_id = (By.ID, "CloudcareTab")
        self.show_full_menu_id = (By.ID, "commcare-menu-toggle")
        self.search_mw = (By.XPATH, "//div[@class='ko-search-box']//input[@type='text']")
        self.search_button_mw = (By.XPATH, "//div[@class='ko-search-box']//button[@data-bind='click: clickAction, visible: !immediate']")
        self.webapp_working_as = (By.XPATH, "//div[@class='restore-as-banner module-banner']/b")
        self.webapp_login_confirmation = (By.ID, 'js-confirmation-confirm')
        self.webapp_login_with_username = (By.XPATH, self.login_as_usernames)
        self.webapp_login = (By.XPATH, "(//div[@class='js-restore-as-item appicon appicon-restore-as'])")
        self.confirm_reactivate_xpath_list = (By.XPATH, "((//div[@class='modal-footer'])/button[@data-bind='click: function(user) { user.is_active(true); }'])")
        self.reactivate_buttons_list = (By.XPATH, "//td/div[@data-bind='visible: !is_active()']//button[@class='btn btn-default']")
        self.confirm_deactivate_xpath_list = (By.XPATH, "((//div[@class='modal-footer'])/button[@class='btn btn-danger'])")
        self.deactivate_buttons_list = (By.XPATH, "(//td/div[@data-bind='visible: is_active()']/button[@class='btn btn-default'])")
        self.show_deactivated_users_btn = (By.XPATH, '//button[@data-bind="visible: !deactivatedOnly(), click: function() { deactivatedOnly(true); }"]')
        self.usernames_xpath = (By.XPATH, "//td/a/strong[@data-bind='text: username']")
        self.page_xpath = (By.XPATH, "(//span[@data-bind='text: $data, visible: !$parent.showSpinner() || $data != $parent.currentPage()'])")

        self.users_menu_id = (By.ID, "ProjectUsersTab")
        self.mobile_workers_menu_link_text = (By.LINK_TEXT, "Mobile Workers")
        self.create_mobile_worker_id = (By.ID, "new-user-modal-trigger")
        self.mobile_worker_username_id = (By.ID, "id_username")
        self.mobile_worker_password_id = (By.ID, "id_new_password")
        self.create_button_xpath = (By.XPATH, '//button[@type="submit"]')
        self.error_message = (By.XPATH,  "//span[@data-bind ='visible: $root.usernameAvailabilityStatus() !== $root.STATUS.NONE']")
        self.cancel_button = (By.XPATH, "//button[text()='Cancel']")
        self.new_user_created_xpath = (By.XPATH, "//*[@class='success']//a[contains(@data-bind,'attr: {href: edit_url}, visible: user_id')]//following-sibling::strong")
        self.NEW = (By.XPATH, "//span[@class='text-success']")
        self.edit_user_field_xpath = (By.XPATH, "//*[@id='btn-edit_user_fields']")
        self.add_field_xpath = (By.XPATH, "//button[@data-bind='click: addField']")
        self.user_property_xpath = (By.XPATH, "(//input[@data-bind='value: slug'])[last()]")
        self.label_xpath = (By.XPATH, "(//input[@data-bind='value: label'])[last()]")
        self.add_choice_button_xpath = (By.XPATH, "(//button[@data-bind='click: addChoice'])[last()]")
        self.choice_xpath = (By.XPATH, "(//input[@data-bind='value: value'])[last()]")
        self.save_field_id = (By.ID, "save-custom-fields")
        self.user_field_success_msg = (By.XPATH, "//div[@class='alert alert-margin-top fade in alert-success']")
        self.mobile_worker_on_left_panel = (By.XPATH, "//a[@data-title='Mobile Workers']")
        self.next_page_button_xpath = (By.XPATH, "//a[contains(@data-bind,'click: nextPage')]")
        self.additional_info_dropdown = (By.ID, "select2-id_data-field-" + "user_field_" + fetch_random_string() + "-container")
        self.select_value_dropdown = (By.XPATH, "//select[@name = 'data-field-user_field_" + fetch_random_string() + "']/option[text()='user_field_" + fetch_random_string() + "']")
        self.update_info_button = (By.XPATH, "//button[text()='Update Information']")
        self.user_file_additional_info = (By.XPATH, "//label[@for='id_data-field-" + "user_field_" + fetch_random_string() + "']")
        self.deactivate_btn_xpath = (By.XPATH, "//td/a/strong[text()='" + self.username + "']/following::td[5]/div[@data-bind='visible: is_active()']/button")
        self.confirm_deactivate = (By.XPATH, "(//button[@class='btn btn-danger'])[1]")
        self.show_full_menu_id = (By.ID, "commcare-menu-toggle")
        self.view_all_link_text = (By.LINK_TEXT, "View All")
        self.search_user_web_apps = (By.XPATH, "//input[@placeholder='Filter workers']")
        self.search_button_we_apps = (By.XPATH, "//div[@class='input-group-btn']")
        # Download and Upload
        self.download_worker_btn = (By.LINK_TEXT, "Download Mobile Workers")
        self.download_users_btn = (By.LINK_TEXT, "Download Users")
        self.bulk_upload_btn = (By.LINK_TEXT, "Bulk Upload")
        self.choose_file = (By.XPATH, "//input[@id='id_bulk_upload_file']")
        self.upload = (By.XPATH, "//button[@class='btn btn-primary disable-on-submit']")
        self.import_complete = (By.XPATH, "//legend[text()='Bulk upload complete.']")
        self.download_filter = (By.XPATH, "//button[@data-bind='html: buttonHTML']")
        self.error_403 = (By.XPATH, "//h1[text()='403 Forbidden']")

    def search_user(self):
        self.wait_to_send_keys(self.search_mw, self.username)
        time.sleep(2)
        self.wait_to_click(self.search_button_mw)

    def webapp_login_as(self):
        self.wait_to_click(self.web_apps_menu_id)
        self.wait_to_click(self.webapp_login)
        time.sleep(1)
        self.send_keys(self.search_user_web_apps, self.username)
        self.wait_to_click(self.search_button_we_apps)
        time.sleep(1)

    def mobile_worker_menu(self):
        try:
            self.wait_to_click(self.users_menu_id)
            time.sleep(1)
        except TimeoutException:
            if not self.is_displayed(self.users_menu_id):
                self.click(self.show_full_menu_id)
                time.sleep(2)
                self.click(self.users_menu_id)
            elif self.is_displayed(self.error_403):
                self.driver.back()
                self.click(self.users_menu_id)
        except StaleElementReferenceException:
            self.driver.refresh()
            self.click(self.users_menu_id)
        self.wait_to_click(self.mobile_workers_menu_link_text)
        assert "Mobile Workers : Users :: - CommCare HQ" in self.driver.title, "Unable find the Users Menu."

    def create_mobile_worker(self):
        try:
            self.wait_to_click(self.create_mobile_worker_id)
            time.sleep(1)
        except (TimeoutException, NoSuchElementException):
            print("TIMEOUT ERROR: Couldn't find create mobile worker button. ")

    def mobile_worker_enter_username(self, username):
        self.send_keys(self.mobile_worker_username_id, username)

    def mobile_worker_enter_password(self, password):
        self.send_keys(self.mobile_worker_password_id, password)

    def click_create(self):
        self.wait_to_click(self.create_button_xpath)
        self.is_present_and_displayed(self.NEW)
        new_user_created = self.get_text(self.new_user_created_xpath)
        print("Username is : " + new_user_created)
        assert self.username == new_user_created, "Could find the new mobile worker created"
        print("Mobile Worker Created")

    def edit_user_field(self):
        self.wait_to_click(self.edit_user_field_xpath)

    def add_field(self):
        self.wait_to_click(self.add_field_xpath)

    def add_user_property(self, user_pro):
        self.clear(self.user_property_xpath)
        self.send_keys(self.user_property_xpath, user_pro)

    def add_label(self, label):
        self.clear(self.label_xpath)
        self.send_keys(self.label_xpath, label)

    def add_choice(self, choice):
        self.wait_to_click(self.add_choice_button_xpath)
        self.clear(self.choice_xpath)
        self.send_keys(self.choice_xpath, choice)

    def save_field(self):
        self.wait_to_click(self.save_field_id)
        assert self.is_displayed(self.user_field_success_msg), "Unable to save userfield."
        print("User Field Added")

    def select_mobile_worker_created(self):
        time.sleep(2)
        self.wait_to_click(self.mobile_worker_on_left_panel)
        time.sleep(2)
        self.search_user()
        time.sleep(3)
        self.click(self.username_link)

    def enter_value_for_created_user_field(self):
        self.wait_to_click(self.additional_info_dropdown)
        self.wait_to_click(self.select_value_dropdown)
        assert self.is_displayed(self.user_file_additional_info), "Unable to assign user field to user."

    def update_information(self):
        self.js_click(self.update_info_button)
        assert self.is_displayed(self.user_field_success_msg), "Unable to update user."
        print("User Field Visible and Added for User")
        time.sleep(2)

    def deactivate_user(self):
        try:
            self.search_user()
            time.sleep(1)
            self.wait_to_click(self.deactivate_buttons_list)
            self.wait_to_click(self.confirm_deactivate_xpath_list)
            time.sleep(3)
        except (TimeoutException, NoSuchElementException):
            print("TIMEOUT ERROR: Deactivation Unsuccessful.")

    def verify_deactivation_via_login(self):
        self.webapp_login_as()
        login_with_username = self.find_elements(self.webapp_login_with_username)
        print("Checking webapp login...")
        for j in range(len(login_with_username)):
            print("Username is " + login_with_username[j].text)
            assert login_with_username[j].text != self.username, "Deactivated mobile worker still visible"
            print("Username not in list - Successfully deactivated!")
        self.wait_to_click(self.show_full_menu_id)

    def reactivate_user(self):
        try:
            time.sleep(1)
            self.mobile_worker_menu()
            self.wait_to_click(self.show_deactivated_users_btn)
            self.search_user()
            time.sleep(1)
            self.wait_to_click(self.reactivate_buttons_list)
            self.wait_to_click(self.confirm_reactivate_xpath_list)
            time.sleep(3)
        except (TimeoutException, NoSuchElementException):
            print("TIMEOUT ERROR: Reactivation unsuccessful.")

    def verify_reactivation_via_login(self):
        self.webapp_login_as()
        login_with_username = self.find_elements(self.webapp_login_with_username)
        for j in range(len(login_with_username)):
            print("Checking webapp login...")
            print("Username is " + login_with_username[j].text)
            if login_with_username[j].text == self.username:
                self.reactivated_user = (By.XPATH, self.login_as_usernames + "[" + str(j + 1) + "]")
                self.wait_to_click(self.reactivated_user)
                self.wait_to_click(self.webapp_login_confirmation)
                break
        self.click(self.show_full_menu_id)
        login_username = self.get_text(self.webapp_working_as)
        assert login_username == self.username, "Reactivated user is not visible."
        print("Working as " + self.username + " : Reactivation successful!")
        time.sleep(1)

    def cleanup_mobile_worker(self):
        try:
            self.wait_to_click(self.actions_tab_link_text)
            self.wait_to_click(self.delete_mobile_worker)
            self.wait_to_send_keys(self.enter_username, self.username + "@" + self.get_domain() + ".commcarehq.org")
            self.wait_to_click(self.confirm_delete_mw)
        except (TimeoutException, NoSuchElementException):
            print("TIMEOUT ERROR: Could not delete the mobile worker")
            self.is_present_and_displayed(self.delete_success_mw), "Mobile User Deletion Unsuccessful"

    def cleanup_user_field(self):
        time.sleep(1)
        self.wait_to_click(self.delete_user_field)
        self.wait_to_click(self.confirm_user_field_delete)

    def download_mobile_worker(self):
        time.sleep(1)
        self.mobile_worker_menu()
        self.wait_to_click(self.download_worker_btn)
        self.wait_to_click(self.download_filter)
        try:
            self.wait_and_sleep_to_click(self.download_users_btn)
            time.sleep(5)
        except TimeoutException:
            print("TIMEOUT ERROR: Still preparing for download..Celery might be down..")
            assert False
        # verify_downloaded_workers
        newest_file = latest_download_file()
        self.assert_downloaded_file(newest_file, "_users_"), "Download Not Completed!"
        print("File download successful")

    def upload_mobile_worker(self):
        self.mobile_worker_menu()
        try:
            self.click(self.bulk_upload_btn)
            newest_file = latest_download_file()
            file_that_was_downloaded = UserData.DOWNLOAD_PATH / newest_file
            time.sleep(5)
            self.send_keys(self.choose_file, str(file_that_was_downloaded))
            self.wait_and_sleep_to_click(self.upload)
        except (TimeoutException, NoSuchElementException):
            print("TIMEOUT ERROR: Could not upload file")
        assert self.is_present_and_displayed(self.import_complete), "Upload Not Completed! Taking Longer to process.."
        print("File uploaded successfully")
