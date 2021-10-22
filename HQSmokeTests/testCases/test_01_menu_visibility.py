from HQSmokeTests.testPages.homePage import HomePage
from HQSmokeTests.testCases.BaseTest import BaseTest
from HQSmokeTests.UserInputs.userInputsData import UserInputsData


class TestMenuVisibility(BaseTest):

    def test_01_reports_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.reports_menu()
        assert "My Saved Reports : Project Reports :: - CommCare HQ" in driver.title

    def test_02_dashboard_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.dashboard_menu()
        assert "CommCare HQ" in driver.title

    def test_03_data_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.data_menu()
        assert "Export Form Data : Data :: - CommCare HQ" in driver.title

    def test_04_user_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.users_menu()
        assert "Mobile Workers : Users :: - CommCare HQ" in driver.title

    def test_05_application_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.applications_menu()
        assert "Releases - "+UserInputsData.application+" - CommCare HQ" in driver.title

    def test_06_messaging_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.messaging_menu()
        assert "Dashboard : Messaging :: - CommCare HQ" in driver.title

    def test_07_web_apps_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.web_apps_menu()
        assert "Web Apps - CommCare HQ" in driver.title
