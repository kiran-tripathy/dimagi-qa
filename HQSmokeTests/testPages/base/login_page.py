from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

from HQSmokeTests.testPages.base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)

        self.username_textbox_id = (By.ID, "id_auth-username")
        self.password_textbox_id = (By.ID, "id_auth-password")
        self.submit_button_xpath = (By.XPATH, '//button[@type="submit"]')
        self.alert_button_accept = (By.ID, "hs-eu-confirmation-button")
        self.continue_button_xpath = (By.XPATH, '//button[@class="btn btn-primary btn-lg" and @type ="button"]')
        self.close_notification = (By.XPATH, "//div[@class='frame-close']/button[1]")
        self.iframe = (By.XPATH, "//iframe[contains(@src,'/embed/frame')]")
        self.view_latest_updates = (By.XPATH, "//*[.='View latest updates']")

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def enter_username(self, username):
        self.clear(self.username_textbox_id)
        self.send_keys(self.username_textbox_id, username)

    def click_continue(self):
        try:
            self.click(self.continue_button_xpath)
        except (NoSuchElementException, ElementNotInteractableException):
            print("Non SSO workflow")

    def enter_password(self, password):
        self.clear(self.password_textbox_id)
        self.send_keys(self.password_textbox_id, password)

    def click_submit(self):
        self.click(self.submit_button_xpath)

    def accept_alert(self):
        try:
            self.wait_to_click(self.alert_button_accept)
        except TimeoutException:
            pass  # ignore if alert not on page

    def assert_logged_in(self):
        assert "Log In" not in self.driver.title, "Login failed"

    def dismiss_notification(self):
        try:
            self.driver.switch_to.frame(self.find_element(self.iframe))
            self.wait_for_element(self.view_latest_updates)
            self.js_click(self.close_notification)
            self.driver.switch_to.default_content()
        except TimeoutException:
            pass  # ignore if alert not on page

    def login(self, username, password):
        self.enter_username(username)
        self.click_continue()
        self.enter_password(password)
        self.dismiss_notification()
        self.accept_alert()
        self.click_submit()
        self.assert_logged_in()
