from selenium.webdriver.common.by import By
from HQSmokeTests.testPages.base.base_page import BasePage


class ReassignCasesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.reassign_cases_menu = (By.LINK_TEXT, "Reassign Cases")
        self.apply = (By.ID, "apply-btn")
        self.case_type = (By.ID, "select2-report_filter_case_type-container")
        self.case_type_option_value = (By.XPATH, "//option[@value='reassign']")
        self.select_first_case = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.user_search_dropdown = (By.ID, "select2-reassign_owner_select-container")
        self.user_to_be_reassigned = (By.XPATH, "(//li[contains(.,'Active Mobile Worker')])[1]")
        self.submit = (By.XPATH, "(//button[text()='Reassign'])[1]")
        self.new_owner_name = (By.XPATH, "((//td)[4])[1]")

    def get_cases(self):
        self.wait_to_click(self.reassign_cases_menu)
        self.wait_to_click(self.case_type)
        self.wait_to_click(self.case_type_option_value)
        self.wait_to_click(self.apply)

    def reassign_case(self):
        self.wait_to_click(self.select_first_case)
        self.wait_to_click(self.user_search_dropdown)
        assigned_username = self.get_text(self.user_to_be_reassigned).split('"')[0]
        self.move_to_element_and_click(self.user_to_be_reassigned)
        self.wait_to_click(self.submit)
        self.driver.refresh()
        reassigned_username = self.get_text(self.new_owner_name).split('@')[0]
        assert reassigned_username in assigned_username
