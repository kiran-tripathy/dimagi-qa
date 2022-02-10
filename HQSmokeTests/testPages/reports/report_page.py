import time

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from HQSmokeTests.userInputs.user_inputs import UserData


class ReportPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.report_name_form = "report form " + fetch_random_string()
        self.report_name_case = "report case " + fetch_random_string()
        self.report_name_saved = "saved form " + fetch_random_string()

        # Mobile Worker Reports
        self.worker_activity_rep = (By.LINK_TEXT, "Worker Activity")
        self.daily_form_activity_rep = (By.LINK_TEXT, "Daily Form Activity")
        self.submissions_by_form_rep = (By.LINK_TEXT, "Submissions By Form")
        self.form_completion_rep = (By.LINK_TEXT, "Form Completion Time")
        self.case_activity_rep = (By.LINK_TEXT, "Case Activity")
        self.completion_vs_submission_rep = (By.LINK_TEXT, "Form Completion vs. Submission Trends")
        self.worker_activity_times_rep = (By.LINK_TEXT, "Worker Activity Times")
        self.project_performance_rep = (By.LINK_TEXT, "Project Performance")

        # Inspect Data Reports
        self.submit_history_rep = (By.LINK_TEXT, "Submit History")
        self.case_list_rep = (By.LINK_TEXT, "Case List")

        # Manage Deployments Reports
        self.application_status_rep = (By.LINK_TEXT, "Application Status")
        self.agg_user_status_rep = (By.LINK_TEXT, "Aggregate User Status")
        self.raw_forms_rep = (By.LINK_TEXT, "Raw Forms, Errors & Duplicates")
        self.device_log_rep = (By.LINK_TEXT, "Device Log Details")
        self.app_error_rep = (By.LINK_TEXT, "Application Error Report")

        # Messaging Reports
        self.sms_usage_rep = (By.LINK_TEXT, "SMS Usage")
        self.messaging_history_rep = (By.LINK_TEXT, "Messaging History")
        self.message_log_rep = (By.LINK_TEXT, "Message Log")
        self.sms_opt_out_rep = (By.LINK_TEXT, "SMS Opt Out Report")
        self.scheduled_messaging_rep = (By.LINK_TEXT, "Scheduled Messaging Events")

        # Report Elements
        self.apply_id = (By.ID, "apply-filters")
        self.report_content_id = (By.ID, "report-content")
        self.save_xpath = (By.XPATH, "//button[@data-bind='click: setConfigBeingEdited']")
        self.custom_report_content_id = (By.ID, "report_table_configurable_wrapper")
        self.edit_report_id = (By.ID, "edit-report-link")
        self.delete_report_xpath = (By.XPATH, "//input[@value='Delete Report']")
        self.homepage = (By.XPATH, ".//a[@href='/homepage/']")

        # Report Builder
        self.create_new_rep_id = (By.ID, "create-new-report-left-nav")
        self.report_name_textbox_id = (By.ID, "id_report_name")

        self.next_button_id = (By.ID, "js-next-data-source")
        self.save_and_view_button_id = (By.ID, "btnSaveView")
        self.form_or_cases = (By.XPATH, "//select[@data-bind='value: sourceType']")
        self.select_form_type = (By.XPATH, "//option[@value='form']")
        self.select_app = (By.XPATH, "//option[text()='Village Health']")
        self.application = (By.XPATH, "//select[@data-bind='value: application']")

        self.select_source_id = (By.XPATH, "//select[@id='id_source']")
        self.select_form_type_value = "form"
        self.select_source_id_form_value = "Case List / Registration Form"
        self.select_source_id_case_value = "commcare-user"

        # Saved Reports
        self.new_saved_report_name = (By.ID, "name")
        self.save_confirm = (By.XPATH, '//div[@class = "btn btn-primary"]')
        self.saved_reports_menu_link = (By.LINK_TEXT, 'My Saved Reports')
        self.saved_report_created = (By.XPATH, "//a[text()='" + self.report_name_saved + "']")
        self.delete_saved = (By.XPATH, "(//a[text()='" + self.report_name_saved + "']//following::button[@class='btn btn-danger add-spinner-on-click'])[1]")

        # Scheduled Reports
        self.scheduled_reports_menu_xpath = (By.XPATH, "//a[@href='#scheduled-reports']")
        self.create_scheduled_report = (By.XPATH, "//a[@class='btn btn-primary track-usage-link']")
        self.available_reports = (By.XPATH, "//li[@class='ms-elem-selectable']")
        self.submit_id = (By.ID, "submit-id-submit_btn")
        self.success_alert = (By.XPATH, "//div[@class='alert alert-margin-top fade in alert-success']")
        self.select_all = (By.XPATH, "(//button[@data-bind='click: selectAll'])[1]")
        self.delete_selected = (By.XPATH,  "//a[@class='btn btn-danger']")
        self.delete_scheduled_confirm = (By.XPATH, "(//button[@data-bind='click: bulkDelete'])[1]")
        self.delete_success_scheduled = (By.XPATH, "//div[@class='alert alert-margin-top fade in alert-success']")

    def check_if_report_loaded(self):
        try:
            self.wait_to_click(self.apply_id)
        except (TimeoutException, NoSuchElementException):
            print("Button Disabled")
        try:
            assert self.is_visible_and_displayed(self.report_content_id)
        except TimeoutException:
            assert self.is_visible_and_displayed(self.custom_report_content_id)
        print("Report loaded successfully!")

    def worker_activity_report(self):
        self.wait_to_click(self.worker_activity_rep)
        self.check_if_report_loaded()

    def daily_form_activity_report(self):
        self.wait_to_click(self.daily_form_activity_rep)
        self.check_if_report_loaded()

    def submissions_by_form_report(self):
        self.wait_to_click(self.submissions_by_form_rep)
        self.check_if_report_loaded()

    def form_completion_report(self):
        self.wait_to_click(self.form_completion_rep)
        self.check_if_report_loaded()

    def case_activity_report(self):
        self.wait_to_click(self.case_activity_rep)
        self.check_if_report_loaded()

    def completion_vs_submission_report(self):
        self.wait_to_click(self.completion_vs_submission_rep)
        self.check_if_report_loaded()

    def worker_activity_times_report(self):
        self.wait_to_click(self.worker_activity_times_rep)
        self.check_if_report_loaded()

    def project_performance_report(self):
        self.wait_to_click(self.project_performance_rep)
        self.check_if_report_loaded()

    def submit_history_report(self):
        self.wait_to_click(self.submit_history_rep)
        self.check_if_report_loaded()

    def case_list_report(self):
        self.wait_to_click(self.case_list_rep)
        self.check_if_report_loaded()

    def sms_usage_report(self):
        self.wait_to_click(self.sms_usage_rep)
        self.check_if_report_loaded()

    def messaging_history_report(self):
        self.wait_to_click(self.messaging_history_rep)
        self.check_if_report_loaded()

    def message_log_report(self):
        self.wait_to_click(self.message_log_rep)
        self.check_if_report_loaded()

    def sms_opt_out_report(self):
        self.wait_to_click(self.sms_opt_out_rep)
        assert self.is_visible_and_displayed(self.report_content_id)

    def scheduled_messaging_report(self):
        self.wait_to_click(self.scheduled_messaging_rep)
        self.check_if_report_loaded()

    def delete_report(self):
        try:
            self.wait_to_click(self.edit_report_id)
        except TimeoutException:
            self.driver.refresh()
            self.wait_to_click(self.edit_report_id)
        self.wait_to_click(self.delete_report_xpath)
        print("Report deleted successfully!")
        self.wait_to_click(self.homepage)

    def create_report_builder_case_report(self):
        self.wait_to_click(self.create_new_rep_id)
        self.send_keys(self.report_name_textbox_id, self.report_name_case)
        self.click(self.select_app)
        self.select_by_text(self.select_source_id, self.select_source_id_case_value)
        self.wait_to_click(self.next_button_id)
        self.wait_to_click(self.save_and_view_button_id)
        self.check_if_report_loaded()
        self.delete_report()

    def create_report_builder_form_report(self):
        self.wait_to_click(self.create_new_rep_id)
        self.send_keys(self.report_name_textbox_id, self.report_name_form)
        self.select_by_value(self.form_or_cases, self.select_form_type_value)
        self.select_by_text(self.application, UserData.village_application)
        self.select_by_text(self.select_source_id, self.select_source_id_form_value)
        self.wait_to_click(self.next_button_id)
        self.wait_to_click(self.save_and_view_button_id)
        self.check_if_report_loaded()
        self.delete_report()

    def saved_report(self):
        self.wait_to_click(self.case_activity_rep)
        self.wait_to_click(self.save_xpath)
        self.send_keys(self.new_saved_report_name, self.report_name_saved)
        self.wait_to_click(self.save_confirm)
        time.sleep(2)
        self.js_click(self.saved_reports_menu_link)
        assert self.is_visible_and_displayed(self.saved_report_created)
        print("Report Saved successfully!")

    def scheduled_report(self):
        self.wait_to_click(self.scheduled_reports_menu_xpath)
        time.sleep(2)
        self.wait_to_click(self.create_scheduled_report)
        self.wait_to_click(self.available_reports)
        self.wait_to_click(self.submit_id)
        assert self.is_visible_and_displayed(self.success_alert)
        print("Scheduled Report Created Successfully")

    def delete_scheduled_and_saved_reports(self):
        self.js_click(self.saved_reports_menu_link)
        self.click(self.delete_saved)
        print("Deleted Saved Report")
        time.sleep(1)
        self.click(self.scheduled_reports_menu_xpath)
        try:
            self.wait_to_click(self.select_all)
            self.wait_to_click(self.delete_selected)
            self.click(self.delete_scheduled_confirm)
            assert self.is_visible_and_displayed(self.delete_success_scheduled)
            print("Deleted Scheduled Report")
        except TimeoutException:
            print("No exports available")
