from HQSmokeTests.testPages.applicationPage import ApplicationPage
from HQSmokeTests.testCases.BaseTest import BaseTest


class TestApplication(BaseTest):

    def test_01_create_new_app(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.create_new_application()

    def test_02_form_builder_explore(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.form_builder_exploration()

    def test_03_form_xml_download_upload(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.form_xml_download_upload()

    def test_04_settings_exploration(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.app_settings_exploration()

    def test_05_delete_app(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.delete_application()
