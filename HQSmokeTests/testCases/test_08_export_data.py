from HQSmokeTests.testPages.exportDataPage import ExportDataPage

def test_01_form_exports(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    export.add_form_exports()
    export.form_exports()
    export.validate_downloaded_form_exports()


def test_02_case_exports(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    export.add_case_exports()
    export.case_exports()
    export.validate_downloaded_case_exports()


def test_03_sms_exports(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    export.sms_exports()


def test_04_daily_saved_exports(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    export.daily_saved_exports_form()
    export.deletion()
    export.daily_saved_exports_case()
    export.deletion()


def test_05_excel_dashboard_integration(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    export.excel_dashboard_integration_form()
    export.deletion()
    export.excel_dashboard_integration_case()
    export.deletion()


def test_06_powerBI_tableau_integration(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    export.power_bi_tableau_integration_form()
    export.deletion()
    export.power_bi_tableau_integration_case()
    export.deletion()


def test_07_manage_forms(driver):

    export = ExportDataPage(driver)
    driver.refresh()
    export.data_tab()
    export.manage_forms()