import os
from configparser import ConfigParser
from pathlib import Path

import pytest
from HQSmokeTests.UserInputs.userInputsData import UserInputsData
from HQSmokeTests.testPages.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

global driver


@pytest.fixture(scope="session")
def environment_settings():
    """Load settings from os.environ

            Names of environment variables:
                DIMAGIQA_URL
                DIMAGIQA_LOGIN_USERNAME
                DIMAGIQA_LOGIN_PASSWORD

            See https://docs.github.com/en/actions/reference/encrypted-secrets
            for instructions on how to set them.
            """
    settings = {}
    for name in ["url", "login_username", "login_password"]:
        var = f"DIMAGIQA_{name.upper()}"
        if var in os.environ:
            settings[name] = os.environ[var]
    return settings


@pytest.fixture(scope="session")
def settings(environment_settings):
    if os.environ.get("CI") == "true":
        settings = environment_settings
        if not settings:
            raise RuntimeError(
                f"Environment variables not set:\n"
                "  DIMAGIQA_URL\n"
                "  DIMAGIQA_LOGIN_USERNAME\n"
                "  DIMAGIQA_LOGIN_PASSWORD\n\n"
                "See https://docs.github.com/en/actions/reference/encrypted-secrets "
                "for instructions on how to set them."
            )
        return settings
    path = Path(__file__).parent.parent / "settings-sample.cfg"
    if not path.exists():
        raise RuntimeError(
            f"Not found: {path}\n\n"
            "Copy settings-sample.cfg to settings-sample.cfg and populate "
            "it with values for the environment you want to test."
        )
    settings = ConfigParser()
    settings.read(path)
    return settings["default"]


@pytest.fixture(scope="session")
def driver(request, settings):
    chrome_options = Options()
    if settings.get("CI") == "true":
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-extensions')
        chrome_options.add_argument('--safebrowsing-disable-download-protection')
        chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
        chrome_options.add_argument('window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": str(UserInputsData.download_path),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True})
    else:
        chrome_options.add_argument('--safebrowsing-disable-download-protection')
        chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
        # #
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument('--headless')

        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": str(UserInputsData.download_path),
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True})
        # web_driver = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=web_driver, options=chrome_options)
    web_driver = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=web_driver, options=chrome_options)
    login = LoginPage(driver, settings["url"])
    login.login(settings["login_username"], settings["login_password"])

    yield driver

    driver.close()
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
# @pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    print("entering report formation")
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    print(item.funcargs)
    # drv = item.funcargs["driver"]
    if report.when == "call" or report.when == "teardown":
        print(report.when)
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            print("report skipped or failed")
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = None
            screen_img = _capture_screenshot(item.funcargs["driver"])
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        print("extra added to report")


def _capture_screenshot(driver):
    return driver.get_screenshot_as_base64()


'''
@pytest.fixture
def email_pytest_report(req):
    "pytest fixture for device flag"
    return req.config.getoption("--email_pytest_report")

# Command line options:
def pytest_addoption(parser):
    parser.addoption("--email_pytest_report",
                 dest="email_pytest_report",
                 help="Email pytest report: Y or N",
                 default="Y")

def pytest_terminal_summary(terminalreporter, exitstatus):
    "add additional section in terminal summary reporting."
    print("entering the terminal summery")
    if not hasattr(terminalreporter.config, 'workerinput'):
        print("terminalreporter has workerinput")
        print(terminalreporter.config.getoption("--email_pytest_report"))
        if terminalreporter.config.getoption("--email_pytest_report").lower() == 'y':
            print("creating email")
            # Initialize the Email_Pytest_Report object
            email_obj = Email_Pytest_Report()
            # Send html formatted email body message with pytest report as an attachment
            email_obj.send_test_report_email(html_body_flag=True, attachment_flag=True, report_file_path='report.html')
            print("send email: Yes")
'''
