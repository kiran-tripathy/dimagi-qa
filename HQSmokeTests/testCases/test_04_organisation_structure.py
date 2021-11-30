from HQSmokeTests.testPages.homePage import HomePage
from HQSmokeTests.testPages.organisationStructurePage import OrganisationStructurePage

def test_01_open_organisation_page(driver):

    menu = HomePage(driver)
    visible = OrganisationStructurePage(driver)
    menu.users_menu()
    visible.organisation_menu_open()
    print("Opened Organisation StructurePage Page")


def test_02_create_location(driver):

    create = OrganisationStructurePage(driver)
    create.create_location()
    print("Location created")


def test_03_edit_location(driver):

    edit = OrganisationStructurePage(driver)
    edit.edit_location()
    print("Location edited")


def test_04_edit_location_fields(driver):

    edit = OrganisationStructurePage(driver)
    edit.edit_location_fields()
    print("Location field created")


def test_05_visibilty_of_location_fields_in_locations(driver):

    edit = OrganisationStructurePage(driver)
    edit.selection_location_field_for_location_created()
    print("Selected location field created, for the location")


def test_06_creation_organization_level(driver):

    org = OrganisationStructurePage(driver)
    org.create_org_level()


def test_07_download_locations(driver):

    menu = HomePage(driver)
    menu.users_menu()
    org = OrganisationStructurePage(driver)
    org.download_locations()


def test_08_upload_locations(driver):

    org = OrganisationStructurePage(driver)
    org.upload_locations()


def test_09_cleanup(driver):

    org = OrganisationStructurePage(driver)
    org.cleanup()
