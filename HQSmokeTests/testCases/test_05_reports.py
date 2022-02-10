from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage


def test_case_14_report_loading(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.worker_activity_report()
    load.daily_form_activity_report()
    load.submissions_by_form_report()
    load.form_completion_report()
    load.case_activity_report()
    load.completion_vs_submission_report()
    load.worker_activity_times_report()
    load.project_performance_report()
    load.submit_history_report()
    load.case_list_report()
    load.sms_usage_report()
    load.messaging_history_report()
    load.message_log_report()
    load.sms_opt_out_report()
    load.scheduled_messaging_report()


def test_case_17_create_form_report(driver):

    report = HomePage(driver)
    driver.refresh()
    report.reports_menu()
    load = ReportPage(driver)
    load.create_report_builder_form_report()


def test_case_18_create_case_report(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.create_report_builder_case_report()


def test_case_19_saved_report(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.saved_report()


def test_case_20_scheduled_report(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.scheduled_report()
    load.delete_scheduled_and_saved_reports()
