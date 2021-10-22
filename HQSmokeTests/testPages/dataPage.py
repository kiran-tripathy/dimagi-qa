from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from UserInputs.generateUserInputs import fetch_random_string


class DataPage:

    def __init__(self, driver):
        self.driver = driver

        # Auto Case Update
        self.auto_case_update_link = 'Automatically Update Cases'
        self.add_rule_button_id = 'add-new'
        self.add_rule_name_id = "id_rule-name"
        self.case_type_id = "id_criteria-case_type"
        self.case_type_option_value = "//option[@value='case']"
        self.rule_save = "//button[@class='btn btn-primary' and text()='Save']"
        self.add_action = "(//button[@ data-toggle='dropdown'])[3]"
        self.close_case = "//li[@data-bind=\"click: function() { addAction('close-case-action'); }\"]"
        self.rule_name = "rule " + fetch_random_string()
        self.rule_created = "//a/strong[text()='" + self.rule_name + "']"
        self.delete_rule = self.rule_created + "//following::button[@class='btn btn-danger'][1]"
        self.delete_confirm = self.rule_created + "//following::button[@class='btn btn-danger delete-item-confirm'][1]"

        # Manage LookUp Table
        self.manage_tables_link = "Manage Tables"
        self.add_table = "//button[@data-bind='click: $root.addDataType']"
        self.table_fields = "//label[@class=\"control-label col-sm-2\"]" \
                            "//following::input[@type='text' and @class = 'form-control']"
        self.table_id = self.table_fields+"[last()-3]"
        self.table_id_name = "lookuptable_"+fetch_random_string()
        self.table_id_description = self.table_fields+"[last()-2]"
        self.add_field = "(//button[@data-bind='click: addField'])[last()]"
        self.field_name = "(//input[@data-bind=\"value: tag, valueUpdate: 'afterkeydown', hasfocus: true\"])[last()]"
        self.save_table = "(//button[@data-bind='click: saveEdit'])[last()]"
        self.table_created = "(//span[text()='"+self.table_id_name+"'])[1]"

        # View LookUp Tables
        self.view_tables_link = "View Tables"
        self.select_table_drop_down_id = "select2-report_filter_table_id-container"
        self.select_table_from_dropdown = "//li[contains(.,'"+self.table_id_name+"')]"
        self.view_table_id = "apply-btn"
        self.column_name = "(//div[contains(i/following-sibling::text(), '"+self.table_id_name+"')])[1]"
        self.delete_table = self.table_created+"//following::button[@data-bind='click: $root.removeDataType'][1]"

    def wait_to_click(self, *locator, timeout=10):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except NoSuchElementException:
            print(NoSuchElementException)

    def open_auto_case_update_page(self):
        self.wait_to_click(By.LINK_TEXT, self.auto_case_update_link)

    def add_new_rule(self):
        self.wait_to_click(By.ID, self.add_rule_button_id)
        self.driver.find_element(By.ID, self.add_rule_name_id).send_keys(self.rule_name)
        self.wait_to_click(By.ID, self.case_type_id)
        self.wait_to_click(By.XPATH, self.case_type_option_value)
        self.wait_to_click(By.XPATH, self.add_action)
        self.wait_to_click(By.XPATH, self.close_case)
        self.wait_to_click(By.XPATH, self.rule_save)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.rule_created))).is_displayed()
        print("New Rule to Update Cases created successfully!")

    def remove_rule(self):
        self.open_auto_case_update_page()
        self.wait_to_click(By.XPATH, self.delete_rule)
        self.wait_to_click(By.XPATH, self.delete_confirm)
        try:
            self.driver.refresh()
            isPresent = self.driver.find_element(By.XPATH, self.rule_created).is_displayed()
        except NoSuchElementException:
            isPresent = False
        if not isPresent:
            assert True
            print("Rule removed successfully!")

    def create_lookup_table(self):
        self.wait_to_click(By.LINK_TEXT, self.manage_tables_link)
        self.wait_to_click(By.XPATH, self.add_table)
        self.driver.find_element(By.XPATH, self.table_id).send_keys(self.table_id_name)
        self.driver.find_element(By.XPATH, self.table_id_description).send_keys(self.table_id_name)
        self.wait_to_click(By.XPATH, self.add_field)
        self.driver.find_element(By.XPATH, self.field_name).send_keys(self.table_id_name)
        self.wait_to_click(By.XPATH, self.save_table)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.table_created))).is_displayed()
        print("LookUp Table created successfully!")

    def view_lookup_table(self):
        self.wait_to_click(By.LINK_TEXT, self.view_tables_link)
        self.wait_to_click(By.ID, self.select_table_drop_down_id)
        self.wait_to_click(By.XPATH, self.select_table_from_dropdown)
        self.wait_to_click(By.ID, self.view_table_id)
        assert True == WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
            By.XPATH, self.column_name))).is_displayed()
        print("LookUp Table can be viewed successfully!")

    def delete_lookup_table(self):
        self.wait_to_click(By.LINK_TEXT, self.manage_tables_link)
        self.wait_to_click(By.XPATH, self.delete_table)
        obj = self.driver.switch_to.alert
        obj.accept()
        print("LookUp Table deleted successfully!")

