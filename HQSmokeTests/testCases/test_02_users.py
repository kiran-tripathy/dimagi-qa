from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.mobile_workers_page import MobileWorkerPage
from HQSmokeTests.testPages.users.group_page import GroupPage
from HQSmokeTests.testPages.users.roles_permissions_page import RolesPermissionPage
from HQSmokeTests.testPages.users.org_structure_page import OrganisationStructurePage
from HQSmokeTests.testPages.users.webapps_permission_page import WebAppPermissionPage


def test_case_02_create_mobile_worker(driver):

    worker = MobileWorkerPage(driver)
    worker.mobile_worker_menu()
    worker.create_mobile_worker()
    worker.mobile_worker_enter_username("username_" + str(fetch_random_string()))
    worker.mobile_worker_enter_password(fetch_random_string())
    worker.click_create()


def test_case_03_create_and_assign_user_field(driver):

    create = MobileWorkerPage(driver)
    create.mobile_worker_menu()
    create.edit_user_field()
    create.add_field()
    create.add_user_property("user_field_" + fetch_random_string())
    create.add_label("user_field_" + fetch_random_string())
    create.add_choice("user_field_" + fetch_random_string())
    create.save_field()
    create.select_mobile_worker_created()
    create.enter_value_for_created_user_field()
    create.update_information()


def test_case_05_create_group_and_assign_user(driver):

    menu = HomePage(driver)
    menu.users_menu()
    visible = GroupPage(driver)
    visible.add_group()
    visible.add_user_to_group()


def test_case_05_edit_user_groups(driver):

    edit = GroupPage(driver)
    edit.edit_existing_group()
    edit.remove_user_from_group()


def test_case_06_add_role(driver):

    role = RolesPermissionPage(driver)
    role.roles_menu_click()
    print("Opened Roles and Permissions Page")
    role = RolesPermissionPage(driver)
    role.add_role()
    print("New Role Added")


def test_case_06_edit_role(driver):

    role = RolesPermissionPage(driver)
    role.edit_role()
    print("Role Edited Successfully")


def test_case_07_create_location(driver):

    create = OrganisationStructurePage(driver)
    create.organisation_menu_open()
    print("Opened Organisation StructurePage Page")
    create.create_location()
    print("Location created")


def test_case_07_edit_existing_location(driver):

    edit = OrganisationStructurePage(driver)
    edit.edit_location()
    print("Location edited")


def test_case_08_edit_location_fields(driver):

    edit = OrganisationStructurePage(driver)
    edit.edit_location_fields()
    print("Location field created")
    edit.selection_location_field_for_location_created()
    print("Selected location field created, for the location")


def test_case_09_creation_organization_level(driver):

    org = OrganisationStructurePage(driver)
    org.create_org_level()


def test_case_10_download_and_upload_users(driver):

    user = MobileWorkerPage(driver)
    user.download_mobile_worker()
    user.upload_mobile_worker()


def test_case_11_download_and_upload_locations(driver):

    org = OrganisationStructurePage(driver)
    org.download_locations()
    org.upload_locations()


def test_case_12_toggle_option_webapp_permission(driver):

    web = WebAppPermissionPage(driver)
    web.webapp_permission_option_toggle()


def test_case_04_deactivate_user(driver):

    user = MobileWorkerPage(driver)
    user.mobile_worker_menu()
    user.deactivate_user()
    user.verify_deactivation_via_login()


def test_case_04_reactivate_user(driver):

    user = MobileWorkerPage(driver)
    user.mobile_worker_menu()
    user.reactivate_user()
    user.verify_reactivation_via_login()


def test_cleanup_items_in_users_menu(driver):
    clean = MobileWorkerPage(driver)
    clean2 = GroupPage(driver)
    clean3 = RolesPermissionPage(driver)
    clean4 = OrganisationStructurePage(driver)

    clean.mobile_worker_menu()
    clean.select_mobile_worker_created()
    clean.cleanup_mobile_worker()
    print("Deleted the mobile worker")

    clean.mobile_worker_menu()
    clean.edit_user_field()
    clean.cleanup_user_field()
    clean.save_field()
    print("Deleted the user field")

    clean.mobile_worker_menu()
    clean2.click_group_menu()
    clean2.cleanup_group()
    print("Deleted the group")

    clean3.roles_menu_click()
    clean3.cleanup_role()
    print("Deleted the role")

    clean4.cleanup_location()
    print("Deleted the location and location field")
