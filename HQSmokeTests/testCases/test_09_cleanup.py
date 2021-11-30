from HQSmokeTests.testPages.groupPage import GroupPage
from HQSmokeTests.testPages.mobileWorkersPage import MobileWorkerPage


def test_01_cleanup_mobile_worker(driver):

    clean = MobileWorkerPage(driver)
    clean.mobile_worker_menu()
    clean.select_mobile_worker_created()
    clean.cleanup_mobile_worker()
    print("Deleted the mobile worker")


def test_02_cleanup_user_field(driver):

    clean = MobileWorkerPage(driver)
    clean.mobile_worker_menu()
    clean.edit_user_field()
    clean.cleanup_user_field()
    clean.save_field()
    print("Deleted the user field")


def test_03_cleanup_group(driver):

    clean = GroupPage(driver)
    clean2 = MobileWorkerPage(driver)
    clean2.mobile_worker_menu()
    clean.click_group_menu()
    clean.cleanup_group()
    print("Deleted the group")
