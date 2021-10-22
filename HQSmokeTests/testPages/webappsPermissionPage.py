from selenium.webdriver.common.by import By


class WebAppPermissionPage:

    def __init__(self, driver):
        self.driver = driver
        self.web_app_permissions_menu = "Web Apps Permissions"
        self.first_radio_button = "//input[@name='ko_unique_1']"
        self.second_radio_button = "//input[@name='ko_unique_2']"
        self.save_button = "//div[@class='btn btn-primary']"

    def webapp_permission_option_toggle(self):
        self.driver.find_element(By.LINK_TEXT, self.web_app_permissions_menu).click()
        self.driver.implicitly_wait(2)
        if self.driver.find_element(By.XPATH, self.first_radio_button).is_selected():
            self.driver.find_element(By.XPATH, self.second_radio_button).click()
        else:
            self.driver.find_element(By.XPATH, self.first_radio_button).click()
        self.driver.find_element(By.XPATH, self.save_button).click()
