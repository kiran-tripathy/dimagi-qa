import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from UserInputs.generateUserInputs import fetch_random_string


class ReportPage:

    def __init__(self, driver):
        self.driver = driver

        # Mobile Worker Reports
        self.worker_activity_rep = "Worker Activity"
        self.daily_form_activity_rep = "Daily Form Activity"
        self.submissions_by_form_rep = "Submissions By Form"
        self.form_completion_rep = "Form Completion Time"
        self.case_activity_rep = "Case Activity"
        self.completion_vs_submission_rep = "Form Completion vs. Submission Trends"
        self.worker_activity_times_rep = "Worker Activity Times"
        self.project_performance_rep = "Project Performance"

        # Inspect Data Reports
        self.submit_history_rep = "Submit History"
        self.case_list_rep = "Case List"

        # Manage Deployments Reports
        self.application_status_rep = "Application Status"
        self.agg_user_status_rep = "Aggregate User Status"
        self.raw_forms_rep = "Raw Forms, Errors & Duplicates"
        self.device_log_rep = "Device Log Details"
        self.app_error_rep = "Application Error Report"

        # Messaging Reports
        self.sms_usage_rep = "SMS Usage"
        self.messaging_history_rep = "Messaging History"
        self.message_log_rep = "Message Log"
        self.sms_opt_out_rep = "SMS Opt Out Report"
        self.scheduled_messaging_rep = "Scheduled Messaging Events"

        # Report Elements
        self.apply_id = "apply-filters"
        self.report_content_id = "report-content"
        self.save_xpath = "//button[@data-bind='click: setConfigBeingEdited']"
        self.custom_report_content_id = "report_table_configurable_wrapper"
        self.edit_report_id = "edit-report-link"
        self.delete_report_xpath = "//input[@value='Delete Report']"
        self.delete_success = "//div[@class='alert alert-margin-top fade in html alert-success']"
        self.homepage = ".//a[@href='/homepage/']"

        # Report Builder
        self.create_new_rep_id = "create-new-report-left-nav"
        self.report_name_textbox_id = "id_report_name"
        self.report_name_form = "report form " + fetch_random_string()
        self.report_name_case = "report case " + fetch_random_string()
        self.next_button_id = "js-next-data-source"
        self.save_and_view_button_id = "btnSaveView"
        self.form_or_cases = "//select[@data-bind='value: sourceType']"
        self.select_form_type = "//option[@value='form']"
        self.select_app = "//option[text()='Village Health']"

        # Saved Reports
        self.new_saved_report_name = "name"
        self.report_name_saved = "saved form " + fetch_random_string()
        self.save_confirm = '//div[@class = "btn btn-primary"]'
        self.saved_reports_menu_link = 'My Saved Reports'
        self.saved_report_created = "//a[text()='"+self.report_name_saved+"']"
        self.delete_saved = "(" + self.saved_report_created + \
                            "//following::button[@class='btn btn-danger add-spinner-on-click'])[1]"

        # Scheduled Reports
        self.scheduled_reports_menu_xpath = "//a[@href='#scheduled-reports']"
        self.create_scheduled_report = "//a[@class='btn btn-primary track-usage-link']"
        self.available_reports = "//li[@class='ms-elem-selectable']"
        self.submit_id = "submit-id-submit_btn"
        self.success_alert = "//div[@class='alert alert-margin-top fade in alert-success']"
        self.delete_scheduled = "(//a[contains(.,'" + self.report_name_saved + \
                                "')]//following::button[@class='btn btn-danger'])[1]"
        self.delete_scheduled_confirm = "//button[@class='send-stopper btn btn-danger disable-on-submit']"

    def wait_to_click(self, *locator, timeout=10):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except (NoSuchElementException, TimeoutException):
            print(NoSuchElementException, TimeoutException)

    def check_if_report_loaded(self):
        try:
            self.wait_to_click(By.ID, self.apply_id)
        except (TimeoutException, NoSuchElementException):
            print("Button Disabled")
        try:
            assert True == WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
                By.ID, self.report_content_id))).is_displayed()
        except TimeoutException:
            assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
                By.ID, self.custom_report_content_id))).is_displayed()
        print("Report loaded successfully!")

    def worker_activity_report(self):
        self.wait_to_click(By.LINK_TEXT, self.worker_activity_rep)
        self.check_if_report_loaded()

    def daily_form_activity_report(self):
        self.wait_to_click(By.LINK_TEXT, self.daily_form_activity_rep)
        self.check_if_report_loaded()

    def submissions_by_form_report(self):
        self.wait_to_click(By.LINK_TEXT, self.submissions_by_form_rep)
        self.check_if_report_loaded()

    def form_completion_report(self):
        self.wait_to_click(By.LINK_TEXT, self.form_completion_rep)
        self.check_if_report_loaded()

    def case_activity_report(self):
        self.wait_to_click(By.LINK_TEXT, self.case_activity_rep)
        self.check_if_report_loaded()

    def completion_vs_submission_report(self):
        self.wait_to_click(By.LINK_TEXT, self.completion_vs_submission_rep)
        self.check_if_report_loaded()

    def worker_activity_times_report(self):
        self.wait_to_click(By.LINK_TEXT, self.worker_activity_times_rep)
        self.check_if_report_loaded()

    def project_performance_report(self):
        self.wait_to_click(By.LINK_TEXT, self.project_performance_rep)
        self.check_if_report_loaded()

    def submit_history_report(self):
        self.wait_to_click(By.LINK_TEXT, self.submit_history_rep)
        self.check_if_report_loaded()

    def case_list_report(self):
        self.wait_to_click(By.LINK_TEXT, self.case_list_rep)
        self.check_if_report_loaded()

    def sms_usage_report(self):
        self.wait_to_click(By.LINK_TEXT, self.sms_usage_rep)
        self.check_if_report_loaded()

    def messaging_history_report(self):
        self.wait_to_click(By.LINK_TEXT, self.messaging_history_rep)
        self.check_if_report_loaded()

    def message_log_report(self):
        self.wait_to_click(By.LINK_TEXT, self.message_log_rep)
        self.check_if_report_loaded()

    def sms_opt_out_report(self):
        self.wait_to_click(By.LINK_TEXT, self.sms_opt_out_rep)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.report_content_id))).is_displayed()

    def scheduled_messaging_report(self):
        self.wait_to_click(By.LINK_TEXT, self.scheduled_messaging_rep)
        self.check_if_report_loaded()

    def delete_report(self):
        try:
            self.wait_to_click(By.ID, self.edit_report_id)
        except TimeoutException:
            self.driver.refresh()
            self.wait_to_click(By.ID, self.edit_report_id)
        self.wait_to_click(By.XPATH, self.delete_report_xpath)
        # assert True == WebDriverWait(self.driver, 10).until(ec.vi((
        #     By.XPATH, self.delete_success))).is_displayed()
        print("Report deleted successfully!")
        self.wait_to_click(By.XPATH, self.homepage)

    def create_report_builder_case_report(self):
        self.wait_to_click(By.ID, self.create_new_rep_id)
        self.driver.find_element(By.ID, self.report_name_textbox_id).send_keys(self.report_name_case)
        self.driver.find_element(By.XPATH, self.select_app).click()
        self.wait_to_click(By.ID, self.next_button_id)
        self.wait_to_click(By.ID, self.save_and_view_button_id)
        self.check_if_report_loaded()
        self.delete_report()

    def create_report_builder_form_report(self):
        self.wait_to_click(By.ID, self.create_new_rep_id)
        self.wait_to_click(By.XPATH, self.form_or_cases)
        self.wait_to_click(By.XPATH, self.select_form_type)
        self.driver.find_element(By.ID, self.report_name_textbox_id).send_keys(self.report_name_form)
        self.wait_to_click(By.ID, self.next_button_id)
        self.wait_to_click(By.ID, self.save_and_view_button_id)
        self.check_if_report_loaded()
        self.delete_report()

    def saved_report(self):
        try:
            self.wait_to_click(By.LINK_TEXT, self.case_activity_rep)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert.accept()
        self.wait_to_click(By.XPATH, self.save_xpath)
        self.driver.find_element(By.ID, self.new_saved_report_name).send_keys(self.report_name_saved)
        self.wait_to_click(By.XPATH, self.save_confirm)
        try:
            time.sleep(2)
            my_saved_rep = self.driver.find_element(By.LINK_TEXT, self.saved_reports_menu_link)
            self.driver.execute_script("arguments[0].click();", my_saved_rep)
        except StaleElementReferenceException:
            time.sleep(2)
            my_saved_rep = self.driver.find_element(By.LINK_TEXT, self.saved_reports_menu_link)
            self.driver.execute_script("arguments[0].click();", my_saved_rep)
        try:
            assert True == WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
                By.XPATH, self.saved_report_created))).is_displayed()
        except UnexpectedAlertPresentException:
            self.driver.refresh()
        print("Report Saved successfully!")

    def scheduled_report(self):
        self.wait_to_click(By.XPATH, self.scheduled_reports_menu_xpath)
        self.wait_to_click(By.XPATH, self.create_scheduled_report)
        self.wait_to_click(By.XPATH, self.available_reports)
        self.wait_to_click(By.ID, self.submit_id)
        assert True == WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
            By.XPATH, self.success_alert))).is_displayed()

    def delete_scheduled_and_saved_reports(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.delete_saved)
        self.wait_to_click(By.XPATH, self.scheduled_reports_menu_xpath)
        try:
            self.wait_to_click(By.XPATH, self.delete_scheduled)
        except StaleElementReferenceException:
            self.wait_to_click(By.XPATH, self.delete_scheduled)
        self.driver.find_element(By.XPATH, self.delete_scheduled_confirm)
