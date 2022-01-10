from HQSmokeTests.testPages.groupPage import GroupPage
from HQSmokeTests.testPages.homePage import HomePage


def test_01_user_groups(driver):

    menu = HomePage(driver)
    visible = GroupPage(driver)
    menu.users_menu()
    visible.click_group_menu()
    visible.add_group()
    visible.add_user_to_group()


def test_02_edit_user_groups(driver):

    edit = GroupPage(driver)
    edit.click_group_menu()
    edit.edit_existing_group()
    edit.remove_user_from_group()
