import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from HQSmokeTests.UserInputs.generateUserInputs import fetch_random_string
from HQSmokeTests.UserInputs.userInputsData import UserInputsData
from HQSmokeTests.testPages.organisationStructurePage import latest_download_file


class ApplicationPage:

    def __init__(self, driver):
        self.driver = driver

        # Create New Application
        self.applications_menu_id = "ApplicationsTab"
        self.new_application = "New Application"
        self.edit_app_name = '//span[@class="inline-edit-icon h3 app-title"]'
        self.app_name_textbox = "(//input[@type='text'])[1]"
        self.app_name = "App "+fetch_random_string()
        self.confirm_change = "(//button[@data-bind=\"click: save, hasFocus: saveHasFocus, visible: !isSaving()\"])[1]"
        self.add_module = "//a[@class='appnav-add js-add-new-item']"
        self.add_case_list = "//button[@data-type='case']"
        self.add_questions = "//div[@class='dropdown fd-add-question-dropdown']"
        self.text_question = "//a[@data-qtype='Text']"
        self.question_display_text = "(//div[@role='textbox'])[1]"
        self.question_display_text_name = "Name"
        self.save_button = "//span[text()='Save']"
        self.app_created = "//span[text()='"+self.app_name+"']"

        # Delete Application
        self.settings = "//i[@class='fa fa-gear']"
        self.delete_app = "//a[@href='#delete-app-modal']"
        self.delete_confirm = "(//button[@class='disable-on-submit btn btn-danger'])[last()]"

        # Application Contents
        self.menu_settings = "//a[@class='appnav-title appnav-title-secondary appnav-responsive']"
        self.menu_settings_content = "js-appmanager-body"
        self.form_settings = "(//a[@data-action='View Form'])[1]"
        self.form_settings_content = "//div[@class='tabbable appmanager-tabs-container']"

        # Form XML
        self.download_xml = "//a[contains(i/following-sibling::text(), 'Download')]"
        self.upload_xml = "//a[@href='#upload-xform']"
        self.add_form_button = "(//i[@class='fa fa-plus'])[1]"
        self.register_form = "//button[@data-case-action='open']"
        self.new_form_settings = "(//a[@data-action='View Form'])[3]"
        self.choose_file = "xform_file_input"
        self.upload = 'xform_file_submit'
        self.same_question_present = "//a[contains(i/following-sibling::text(), 'Name')]"

        # App Settings
        self.languages_tab = "//a[@href='#languages']"
        self.languages_tab_content = "language-settings-options"
        self.multimedia_tab = "//a[@href='#multimedia-tab']"
        self.multimedia_tab_content = "multimedia-tab"
        self.actions_tab = "//a[text()='Actions']"
        self.actions_tab_content = "actions"
        self.add_ons_tab = "//a[@href='#add-ons']"
        self.add_ons_tab_content = "add-ons"
        self.advanced_settings_tab = "//a[@href='#commcare-settings']"
        self.advanced_settings_tab_content = "app-settings-options"

    def wait_to_click(self, *locator, timeout=10):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def create_new_application(self):
        self.wait_to_click(By.ID, self.applications_menu_id)
        self.wait_to_click(By.LINK_TEXT, self.new_application)
        self.wait_to_click(By.XPATH, self.edit_app_name)
        self.driver.find_element(By.XPATH, self.app_name_textbox).clear()
        self.driver.find_element(By.XPATH, self.app_name_textbox).send_keys(self.app_name)
        self.wait_to_click(By.XPATH, self.confirm_change)
        self.wait_to_click(By.XPATH, self.add_module)
        time.sleep(1)
        self.wait_to_click(By.XPATH, self.add_case_list)
        self.wait_to_click(By.XPATH, self.add_questions)
        self.wait_to_click(By.XPATH, self.text_question)
        self.driver.find_element(By.XPATH, self.question_display_text).send_keys(self.question_display_text_name)
        self.wait_to_click(By.XPATH, self.save_button)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.app_created))).is_displayed()
        print("New App created successfully!")

    def form_builder_exploration(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.menu_settings).click()
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.menu_settings_content))).is_displayed()
        print("Menu Settings loaded successfully!")
        self.driver.find_element(By.XPATH, self.form_settings).click()
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.form_settings_content))).is_displayed()
        print("Form Settings loaded successfully!")

    def delete_application(self):
        time.sleep(2)
        settings_button = self.driver.find_element(By.XPATH, self.settings)
        self.driver.execute_script("arguments[0].click();", settings_button)
        self.wait_to_click(By.XPATH, self.actions_tab)
        self.wait_to_click(By.XPATH, self.delete_app)
        self.wait_to_click(By.XPATH, self.delete_confirm)

    def form_xml_download_upload(self):
        self.wait_to_click(By.XPATH, self.actions_tab)
        self.wait_to_click(By.XPATH, self.download_xml)
        time.sleep(1)
        self.wait_to_click(By.XPATH, self.add_form_button)
        time.sleep(1)
        try:
            self.wait_to_click(By.XPATH, self.register_form)
            time.sleep(2)
        except TimeoutException:
            self.driver.refresh()
        self.wait_to_click(By.XPATH, self.new_form_settings)
        self.wait_to_click(By.XPATH, self.actions_tab)
        self.wait_to_click(By.XPATH, self.upload_xml)
        newest_file = latest_download_file()
        file_that_was_downloaded = UserInputsData.download_path / newest_file
        self.driver.find_element(By.ID, self.choose_file).send_keys(str(file_that_was_downloaded))
        time.sleep(1)
        self.driver.find_element(By.ID, self.upload).click()
        time.sleep(1)
        assert True == WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
            By.XPATH, self.same_question_present))).is_displayed()
        print("XML copied successfully!")

    def app_settings_exploration(self):
        self.wait_to_click(By.XPATH, self.settings)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.languages_tab_content))).is_displayed()
        self.wait_to_click(By.XPATH, self.multimedia_tab)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.multimedia_tab_content))).is_displayed()
        self.wait_to_click(By.XPATH, self.actions_tab)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.actions_tab_content))).is_displayed()
        self.wait_to_click(By.XPATH, self.add_ons_tab)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.add_ons_tab_content))).is_displayed()
        self.wait_to_click(By.XPATH, self.advanced_settings_tab)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.advanced_settings_tab_content))).is_displayed()
        print("App Settings loading successfully!")
