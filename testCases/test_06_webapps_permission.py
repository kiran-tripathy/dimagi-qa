from testPages.homePage import HomePage
from testPages.webappsPermissionPage import WebAppPermissionPage
from testCases.BaseTest import BaseTest


class TestWebAppPermissions(BaseTest):

    def test_01_toggle_option_webapp_permission(self):
        driver = self.driver
        menu = HomePage(driver)
        web = WebAppPermissionPage(driver)
        menu.users_menu()
        web.webapp_permission_option_toggle()