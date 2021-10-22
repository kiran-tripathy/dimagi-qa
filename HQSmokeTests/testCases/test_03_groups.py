from testPages.homePage import HomePage
from testPages.groupPage import GroupPage
from testCases.BaseTest import BaseTest


class TestGroups(BaseTest):

    def test_01_user_groups(self):
        driver = self.driver
        menu = HomePage(driver)
        visible = GroupPage(driver)
        menu.users_menu()
        visible.click_group_menu()
        visible.add_group()
        visible.add_user_to_group()

    def test_02_edit_user_groups(self):
        driver = self.driver
        edit = GroupPage(driver)
        edit.click_group_menu()
        edit.edit_existing_group()
        edit.remove_user_from_group()
