from testPages.homePage import HomePage
from testPages.messagingPage import MessagingPage
from testCases.BaseTest import BaseTest


class MessagingTests(BaseTest):

    def test_01_dashboard(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.open_dashboard_page()

    def test_02_compose_sms(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.compose_sms()

    def test_03_broadcast(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.send_broadcast_message()

    def test_04_create_cond_alert(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.create_cond_alert()
        msg.remove_cond_alert()

    def test_05_cond_alert_bulk_upload(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.cond_alert_download()
        msg.cond_alert_upload()

    def test_06_keyword_creation(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.add_keyword_trigger()
        msg.remove_keyword()
        msg.add_structured_keyword_trigger()
        msg.remove_structured_keyword()

    def test_07_chats(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.chat_page()

    def test_08_general_settings(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.general_settings_page()

    def test_09_languages(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.languages_page()

    def test_10_translations(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.msg_trans_download()
        msg.msg_trans_upload()

    def test_11_settings_pages(self):
        driver = self.driver
        msg = MessagingPage(driver)
        msg.project_settings_page()
        msg.current_subscription_page()
