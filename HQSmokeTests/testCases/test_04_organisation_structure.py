from testPages.homePage import HomePage
from testPages.organisationStructurePage import OrganisationStructurePage
from testCases.BaseTest import BaseTest


class TestOrganisationStructure(BaseTest):

    def test_01_open_organisation_page(self):
        driver = self.driver
        menu = HomePage(driver)
        visible = OrganisationStructurePage(driver)
        menu.users_menu()
        visible.organisation_menu_open()
        print("Opened Organisation StructurePage Page")

    def test_02_create_location(self):
        driver = self.driver
        create = OrganisationStructurePage(driver)
        create.create_location()
        print("Location created")

    def test_03_edit_location(self):
        driver = self.driver
        edit = OrganisationStructurePage(driver)
        edit.edit_location()
        print("Location edited")

    def test_04_edit_location_fields(self):
        driver = self.driver
        edit = OrganisationStructurePage(driver)
        edit.edit_location_fields()
        print("Location field created")

    def test_05_visibilty_of_location_fields_in_locations(self):
        driver = self.driver
        edit = OrganisationStructurePage(driver)
        edit.selection_location_field_for_location_created()
        print("Selected location field created, for the location")

    def test_06_creation_organization_level(self):
        driver = self.driver
        org = OrganisationStructurePage(driver)
        org.create_org_level()

    def test_07_download_locations(self):
        driver = self.driver
        menu = HomePage(driver)
        menu.users_menu()
        org = OrganisationStructurePage(driver)
        org.download_locations()

    def test_08_upload_locations(self):
        driver = self.driver
        org = OrganisationStructurePage(driver)
        org.upload_locations()

    def test_09_cleanup(self):
        driver = self.driver
        org = OrganisationStructurePage(driver)
        org.cleanup()
