import os
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions 
from HQSmokeTests.UserInputs.userInputsData import UserInputsData
import pandas as pd
from HQSmokeTests.testCases.conftest import settings

def latest_download_file():
    os.chdir(UserInputsData.download_path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = max(files, key=os.path.getctime)
    print("File downloaded: " + newest)
    return newest


class ExportDataPage:

    def __init__(self, driver):  # initialize each WebElement here
        self.driver = driver
        self.data_dropdown = 'Data'  # Data dropdown
        self.view_all_link = 'View All'  # View All link

        # Delete Export
        self.delete_button = "//a[@class='btn btn-danger'][1]"
        self.delete_confirmation_button = "//button[@data-bind='click: deleteExport']"

        # Add Export
        self.add_export_button = "//a[@href='#createExportOptionsModal']"  # Add Export button
        self.app_dropdown = "//span[@aria-labelledby='select2-id_application-container']"  # Application dropdown
        self.select_app = "//li[text()='Village Health']"  # Selecting Village Health app
        self.menu_dropdown = "//span[@aria-labelledby='select2-id_module-container']"  # Menu dropdown in the modal
        self.select_menu = '//*[@id="select2-id_module-results"]/li[1]'  # Selecting first menu item
        self.form_dropdown = "//span[@aria-labelledby='select2-id_form-container']"  # Form dropdown in the modal
        self.select_form = '//*[@id="select2-id_form-results"]/li[1]'  # Selecting first form item
        self.add_export_conf = "//button[@data-bind='visible: showSubmit, disable: disableSubmit']"  # Add export
        self.export_name = '//*[@id="export-name"]'  # Custom name for the export
        self.export_settings_create = "//button[@class='btn btn-lg btn-primary']"  # Creating export
        self.date_range = "id_date_range"
        self.date_range_key = "//li[@data-range-key='Last 30 Days']"

        # Export Form and Case data variables
        self.export_form_data_link = 'Export Form Data'  # Export Form Data link on the left panel
        self.export_case_data_link = 'Export Case Data'  # Export Case Data link on the left panel
        self.export_form_case_data_button = "(//a[@class='btn btn-primary'])[2]"  # Export button on listing page
        self.prepare_export_button = "//button[@data-bind='disable: disablePrepareExport']"  # click prepare exports
        self.download_button = "//a[@class='btn btn-primary btn-full-width']"  # click download

        # Find Data By ID
        self.find_data_by_ID_link = 'Find Data by ID'  # Click findDataByID link
        self.find_data_by_ID_textbox = "//input[@placeholder='Form Submission ID']"  # Find data by ID textbox
        self.find_data_by_ID_button = "(//button[@data-bind='click: find, enable: allowFind'])[2]"
        self.view_FormID_CaseID = 'View'
        self.womanName_HQ = "(//div[@class='form-data-readable form-data-raw'])[1]"  # Property 'Woman's name' value HQ
        self.woman_case_name_HQ = "//th[@title='name']//following::td[1]"

        # Export SMS variables
        self.export_sms_link = "Export SMS Messages"  # Export Case Data on the left panel

        # Daily Saved Export variables, form, case
        self.edit_form_case_export = "(//a[@data-bind='click: editExport'])[1]"  # Edit an existing form/case export
        self.create_DSE_checkbox = '//*[@id="daily-saved-export-checkbox"]'  # Create a Daily Saved Export checkbox
        self.download_dse_form = "//span[text()='" + UserInputsData.form_export_name + \
                                 "']//following::a[@class='btn btn-info btn-xs']"
        self.download_dse_case = "//span[text()='" + UserInputsData.case_export_name + \
                                 "']//following::a[@class='btn btn-info btn-xs']"

        # Excel Dashboard Integrations, form, case
        self.export_excel_dash_int_link = 'Excel Dashboard Integration'  # Excel Dashboard Integrations left panel
        self.model_dropdown = '//*[@id="id_model_type"]'
        self.select_form_model = '//*[@id="id_model_type"]/option[3]'
        self.select_case_model = '//*[@id="id_model_type"]/option[2]'
        self.case_type_dropdown = '//*[@id="div_id_case_type"]/div/span/span[1]/span'
        self.select_case_type = '//*[@id="select2-id_case_type-results"]/li'
        self.update_data = "//button[@data-toggle='modal'][1]"
        self.update_data_conf = "//button[@data-bind='click: emailedExport.updateData']"
        self.copy_dashfeed_link = "(//span[contains(@data-bind, 'copyLinkRequested')])[1]"
        self.dashboard_feed_link = "//span[@class='input-group-btn']//preceding::a[@class='btn btn-info btn-xs']"

        # Power BI / Tableau Integration, Form
        self.powerBI_tab_int_link = 'PowerBi/Tableau Integration'
        self.copy_odatafeed_link = "//a[@class='btn btn-default btn-sm']"
        self.edit_button = "//input[@style='']//following::a[@data-bind='click: editExport'][1]"

        # Manage Forms
        self.manage_forms_link = '//*[@id="hq-sidebar"]/nav/ul[2]/li[3]/a'
        self.apply_button = '//*[@id="apply-btn"]'
        self.select_all_checkbox = "//input[@name='select_all']"
        # self.checkbox1 = "//input[@class='xform-checkbox'][1]"
        self.checkbox1 = "//*[@id='form_options']//*[@type='checkbox']"
        self.archive_button = '//*[@id="submitForms"]'
        self.success_message = "//div[@class='alert alert-success']"
        self.view_form_link = "//a[@class='ajax_dialog']"
        self.archived_restored_dropdown = '//*[@id="select2-report_filter_archive_or_restore-container"]'
        self.archived_forms_option = '/html/body/span/span/span[2]/ul/li[2]'
        self.manage_forms_return = '//span[contains(text(),"Return to")]/a[.="Manage Forms"]'

    def wait_to_click(self, *locator, timeout=20):
        time.sleep(5)
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()


    def wait_to_clear(self, *locator, timeout=5):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).clear()
        except TimeoutException:
            print(TimeoutException)

    def switch_to_next_tab(self):
        winHandles = self.driver.window_handles
        window_after = winHandles[1]
        self.driver.switch_to.window(window_after)

    def switch_back_to_prev_tab(self):
        winHandles = self.driver.window_handles
        window_before = winHandles[0]
        self.driver.switch_to.window(window_before)

    def get_url_paste_browser_case(self):
        self.wait_to_click(By.XPATH, self.copy_odatafeed_link)
        time.sleep(2)
        self.wait_to_click(By.XPATH, self.edit_button)
        time.sleep(2)
        get_url = self.driver.current_url
        ID = get_url.split("/")[10]
        odata_feed_link_case = "https://staging.commcarehq.org/a/qa-automation/api/v0.5/odata/cases/" + ID + "/feed/"
        self.driver.back()
        self.driver.execute_script("window.open('');")  # Open a new tab
        self.switch_to_next_tab()
        username = load_settings()["login_username"]
        password = load_settings()["login_password"]
        final_URL_case = f"https://{username}:{password}@{odata_feed_link_case[8:]}"
        print(final_URL_case)
        self.driver.get(final_URL_case)

    def get_url_paste_browser_form(self, settings):
        self.wait_to_click(By.XPATH, self.copy_odatafeed_link)
        time.sleep(2)
        self.wait_to_click(By.XPATH, self.edit_button)
        time.sleep(2)
        get_url = self.driver.current_url
        ID = get_url.split("/")[10]
        odata_feed_link_form = "https://staging.commcarehq.org/a/qa-automation/api/v0.5/odata/forms/" + ID + "/feed/"
        self.driver.back()
        self.driver.execute_script("window.open('');")  # Open a new tab
        self.switch_to_next_tab()
        username = settings["login_username"]
        password = settings["login_password"]
        final_URL_form = f"https://{username}:{password}@{odata_feed_link_form[8:]}"
        print(final_URL_form)
        self.driver.get(final_URL_form)

    def data_tab(self):
        self.wait_to_click(By.LINK_TEXT, self.data_dropdown)
        self.wait_to_click(By.LINK_TEXT, self.view_all_link)

    def deletion(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.delete_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.delete_confirmation_button).click()
        print("Delete Confirmation Button clicked")

    # Test Case 20_a - Verify Export functionality for Forms
    def add_form_exports(self):
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.menu_dropdown)
        self.wait_to_click(By.XPATH, self.select_menu)
        self.wait_to_click(By.XPATH, self.form_dropdown)
        self.wait_to_click(By.XPATH, self.select_form)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Export created!!")

    def form_exports(self):
        self.wait_to_click(By.XPATH, self.export_form_case_data_button)
        # Date filter
        # self.wait_to_click(By.ID, self.date_range)
        # self.wait_to_click(By.XPATH, self.date_range_key)
        self.wait_to_click(By.XPATH, self.prepare_export_button)
        self.wait_to_click(By.XPATH, self.download_button)
        print("Download form button clicked")
        time.sleep(3)

    # Test Case 22_a -  Find Data By ID, forms
    def validate_downloaded_form_exports(self):
        self.wait_to_click(By.LINK_TEXT, self.find_data_by_ID_link)
        newest_file = latest_download_file()
        print("Newest file:" + newest_file)
        data = pd.read_excel(newest_file)
        df = pd.DataFrame(data, columns=['form.womans_name', 'formid'])
        formID = df['formid'].values[0]
        woman_name_excel = df['form.womans_name'].values[0]

        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((
            By.XPATH, self.find_data_by_ID_textbox))).send_keys(str(formID))
        self.wait_to_click(By.XPATH, self.find_data_by_ID_button)
        self.wait_to_click(By.LINK_TEXT, self.view_FormID_CaseID)
        self.switch_to_next_tab()
        time.sleep(3)
        womanName_HQ = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((
            By.XPATH, self.womanName_HQ))).text
        assert woman_name_excel == womanName_HQ
        print("Downloaded file has the required data!")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case 20_b - Verify Export functionality for Cases
    def add_case_exports(self):
        self.wait_to_click(By.LINK_TEXT, self.export_case_data_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.case_type_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_type)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Export created!!")

    def case_exports(self):
        self.wait_to_click(By.LINK_TEXT, self.export_case_data_link)
        self.wait_to_click(By.XPATH, self.export_form_case_data_button)
        self.wait_to_click(By.XPATH, self.prepare_export_button)
        self.wait_to_click(By.XPATH, self.download_button)
        time.sleep(3)

    # Test Case 22_b - Find Data by ID for Case Exports
    def validate_downloaded_case_exports(self):
        self.wait_to_click(By.LINK_TEXT, self.find_data_by_ID_link)
        newest_file = latest_download_file()
        print("Newest file:" + newest_file)
        data2 = pd.read_excel(newest_file)
        df2 = pd.DataFrame(data2, columns=['name', 'caseid'])
        caseID = df2['caseid'].values[0]
        woman_name_excel = df2['name'].values[0]

        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((
                By.XPATH, self.find_data_by_ID_textbox))).send_keys(str(caseID))
        self.wait_to_click(By.XPATH, self.find_data_by_ID_button)
        self.wait_to_click(By.LINK_TEXT, self.view_FormID_CaseID)
        time.sleep(3)
        self.switch_to_next_tab()
        womanName_HQ = WebDriverWait(self.driver, 15).until(ec.presence_of_element_located((
            By.XPATH, self.woman_case_name_HQ))).text
        assert woman_name_excel == womanName_HQ
        print("Downloaded file has the required data!")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case 21 - Export SMS Messages
    def sms_exports(self):
        self.wait_to_click(By.LINK_TEXT, self.export_sms_link)
        self.wait_to_click(By.XPATH, self.prepare_export_button)
        self.wait_to_click(By.XPATH, self.download_button)
        time.sleep(3)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        modTimesinceEpoc = (UserInputsData.download_path / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        assert "Messages" in newest_file and diff_seconds in range(0, 600)
        print("Export successful")

    # Test Case 23_a - Daily saved export, form
    def daily_saved_exports_form(self):
        self.wait_to_click(By.LINK_TEXT, self.export_form_data_link)
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.edit_form_case_export)
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.form_export_name)
        self.wait_to_click(By.XPATH, self.create_DSE_checkbox)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        self.wait_to_click(By.XPATH, self.update_data)
        self.wait_to_click(By.XPATH, self.update_data_conf)
        time.sleep(2)
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.download_dse_form)
        time.sleep(3)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        modTimesinceEpoc = (UserInputsData.download_path / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        assert "Form Export DSE" in newest_file and diff_seconds in range(0, 600)
        print("DSE Form Export successful")

    # Test Case 23_b - Daily saved export, case
    def daily_saved_exports_case(self):
        self.wait_to_click(By.LINK_TEXT, self.export_case_data_link)
        self.wait_to_click(By.XPATH, self.edit_form_case_export)
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.case_export_name)
        self.wait_to_click(By.XPATH, self.create_DSE_checkbox)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        self.wait_to_click(By.XPATH, self.update_data)
        self.wait_to_click(By.XPATH, self.update_data_conf)
        time.sleep(2)
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.download_dse_case)
        time.sleep(3)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        modTimesinceEpoc = (UserInputsData.download_path / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        assert "Case Export DSE" in newest_file and diff_seconds in range(0, 600)
        print("DSE Case Export successful")

    # Test Case - 24 - Excel Dashboard Integration, form
    def excel_dashboard_integration_form(self):
        self.wait_to_click(By.LINK_TEXT, self.export_excel_dash_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_form_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.menu_dropdown)
        self.wait_to_click(By.XPATH, self.select_menu)
        self.wait_to_click(By.XPATH, self.form_dropdown)
        self.wait_to_click(By.XPATH, self.select_form)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Dashboard Feed added!!")
        self.wait_to_clear(By.XPATH, self.export_name)
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((
                    By.XPATH, self.export_name))).send_keys(UserInputsData.dashboard_feed_form)
        self.driver.find_element(By.XPATH, self.export_settings_create).click()
        print("Dashboard Form Feed created!!")
        self.wait_to_click(By.XPATH, self.update_data)
        self.wait_to_click(By.XPATH, self.update_data_conf)
        time.sleep(2)
        self.driver.refresh()
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.copy_dashfeed_link).click()
            dashboard_feed_link = self.driver.find_element(By.XPATH, self.dashboard_feed_link).get_attribute("href")
            print("Feed Link: "+dashboard_feed_link)
            self.driver.execute_script("window.open('');")  # Open a new tab
            self.switch_to_next_tab()
            self.driver.get(dashboard_feed_link)
            dashboard_feed_data = self.driver.page_source
            if dashboard_feed_data != "":
                print("Excel Dashboard form has data")
            else:
                print("Excel Dashboard (form) is empty")
            self.driver.close()
            self.switch_back_to_prev_tab()
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    # Test Case - 25 - Excel Dashboard Integration, case

    def excel_dashboard_integration_case(self):
        self.wait_to_click(By.LINK_TEXT, self.export_excel_dash_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.case_type_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_type)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Dashboard Feed added!!")
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.dashboard_feed_case)
        self.driver.find_element(By.XPATH, self.export_settings_create).click()
        print("Dashboard Form Feed created!!")
        self.wait_to_click(By.XPATH, self.update_data)
        self.wait_to_click(By.XPATH, self.update_data_conf)
        time.sleep(2)
        self.driver.refresh()
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.copy_dashfeed_link).click()
            dashboard_feed_link = self.driver.find_element(By.XPATH, self.dashboard_feed_link).get_attribute("href")
            print(dashboard_feed_link)
            self.driver.execute_script("window.open('');")  # Open a new tab
            self.switch_to_next_tab()
            self.driver.get(dashboard_feed_link)
            dashboard_feed_data = self.driver.page_source
            if dashboard_feed_data != "":
                print("Excel Dashboard (case) has data")
            else:
                print("Excel Dashboard (case) is empty")
            self.driver.close()
            self.switch_back_to_prev_tab()
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    # Test Case - 28 - Power BI / Tableau Integration, Form
    def power_bi_tableau_integration_form(self):
        self.wait_to_click(By.LINK_TEXT, self.powerBI_tab_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_form_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.menu_dropdown)
        self.wait_to_click(By.XPATH, self.select_menu)
        self.wait_to_click(By.XPATH, self.form_dropdown)
        self.wait_to_click(By.XPATH, self.select_form)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Odata form Feed added!!")
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.odata_feed_form)
        self.driver.find_element(By.XPATH, self.export_settings_create).click()
        print("Odata Form Feed created!!")
        self.driver.refresh()
        self.get_url_paste_browser_form()
        odata_feed_data = self.driver.page_source
        assert odata_feed_data != ""
        print("Odata form feed has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case - 27 - Power BI / Tableau Integration, Case`
    def power_bi_tableau_integration_case(self):
        self.driver.refresh()
        self.wait_to_click(By.LINK_TEXT, self.powerBI_tab_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        print("Add OData_feed_button clicked")
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.case_type_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_type)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Odata Case Feed added!!")
        time.sleep(5)
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.odata_feed_case)
        self.driver.find_element(By.XPATH, self.export_settings_create).click()
        print("Odata Case Feed created!!")
        self.driver.refresh()
        self.get_url_paste_browser_case()
        odata_feed_data = self.driver.page_source
        assert odata_feed_data != ""  # This condition can be improvised
        print("Odata case feed has data")
        self.driver.close()  # Close the feed URL
        self.switch_back_to_prev_tab()
        self.driver.refresh()

    # Test Case - 30 - Verify user is able to manage forms and archive a form
    def manage_forms(self):
        # Forms archival
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.XPATH, self.apply_button)
        time.sleep(2)
        self.wait_to_click(By.XPATH, self.checkbox1)
        self.wait_to_click(By.XPATH, self.archive_button)
        assert WebDriverWait(self.driver, 40).until(ec.presence_of_element_located((
            By.XPATH, self.success_message))).is_displayed()
        print("Forms archival successful!!")
        time.sleep(5)
        
        # View Archived Forms
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.XPATH, self.archived_restored_dropdown)
        self.wait_to_click(By.XPATH, self.archived_forms_option)
        self.wait_to_click(By.XPATH, self.apply_button)
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("archived_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

        # Restore Archived Forms
        try:
            self.wait_to_click(By.XPATH, self.checkbox1)
            self.wait_to_click(By.XPATH, self.archive_button)
            assert WebDriverWait(self.driver, 40).until(ec.presence_of_element_located((
                By.XPATH, self.success_message))).is_displayed()
            print("Forms archival successful!!")
        except TimeoutException:
            print(TimeoutException)

        # View Normal Forms
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.XPATH, self.apply_button)
        self.wait_to_click(By.XPATH, self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("normal_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

        
       
