from HQSmokeTests.testPages.homePage import HomePage
from HQSmokeTests.testPages.webappsPermissionPage import WebAppPermissionPage

def test_01_toggle_option_webapp_permission(driver):

    menu = HomePage(driver)
    web = WebAppPermissionPage(driver)
    menu.users_menu()
    web.webapp_permission_option_toggle()
