from testPages.groupPage import GroupPage
from testPages.mobileWorkersPage import MobileWorkerPage
from testPages.rolesPermissionsPage import RolesPermissionPage
from testCases.BaseTest import BaseTest
import pytest

class TestCleanUps(BaseTest):

    def test_01_cleanup_mobile_worker(self):
        driver = self.driver
        clean = MobileWorkerPage(driver)
        clean.mobile_worker_menu()
        clean.select_mobile_worker_created()
        clean.cleanup_mobile_worker()
        print("Deleted the mobile worker")

    def test_02_cleanup_user_field(self):
        driver = self.driver
        clean = MobileWorkerPage(driver)
        clean.mobile_worker_menu()
        clean.edit_user_field()
        clean.cleanup_user_field()
        clean.save_field()
        print("Deleted the user field")

     def test_03_cleanup_group(self):
        driver = self.driver
        clean = GroupPage(driver)
        clean2 = MobileWorkerPage(driver)
        clean2.mobile_worker_menu()
        clean.click_group_menu()
        clean.cleanup_group()
        print("Deleted the group")
