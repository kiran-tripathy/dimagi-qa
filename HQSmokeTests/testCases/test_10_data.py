from HQSmokeTests.testPages.dataPage import DataPage
from HQSmokeTests.testPages.exportDataPage import ExportDataPage

def test_01_auto_case_update(driver):

    export = ExportDataPage(driver)
    data = DataPage(driver)
    export.data_tab()
    data.open_auto_case_update_page()
    data.add_new_rule()
    data.remove_rule()


def test_02_create_lookup_table(driver):

    data = DataPage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.create_lookup_table()


def test_03_view_lookup_table(driver):

    data = DataPage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.view_lookup_table()
    data.delete_lookup_table()
