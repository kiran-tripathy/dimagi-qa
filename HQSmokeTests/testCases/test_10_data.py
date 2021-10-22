from testPages.dataPage import DataPage
from testPages.exportDataPage import ExportDataPage
from testCases.BaseTest import BaseTest


class TestData(BaseTest):

    def test_01_auto_case_update(self):
        driver = self.driver
        export = ExportDataPage(driver)
        data = DataPage(driver)
        export.data_tab()
        data.open_auto_case_update_page()
        data.add_new_rule()
        data.remove_rule()

    def test_02_create_lookup_table(self):
        driver = self.driver
        data = DataPage(driver)
        export = ExportDataPage(driver)
        export.data_tab()
        data.create_lookup_table()

    def test_03_view_lookup_table(self):
        driver = self.driver
        data = DataPage(driver)
        export = ExportDataPage(driver)
        export.data_tab()
        data.view_lookup_table()
        data.delete_lookup_table()
