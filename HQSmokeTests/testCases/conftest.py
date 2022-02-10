import os
from configparser import ConfigParser
from pathlib import Path

import pytest
from HQSmokeTests.userInputs.user_inputs import UserData
from HQSmokeTests.testPages.base.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from HQSmokeTests.utilities.email_pytest_report import Email_Pytest_Report


global driver


@pytest.fixture(scope="session")
def environment_settings():
    """Load settings from os.environ

            Names of environment variables:
                DIMAGIQA_URL
                DIMAGIQA_LOGIN_USERNAME
                DIMAGIQA_LOGIN_PASSWORD
                DIMAGIQA_MAIL_USERNAME
                DIMAGIQA_MAIL_PASSWORD

            See https://docs.github.com/en/actions/reference/encrypted-secrets
            for instructions on how to set them.
            """
    settings = {}
    for name in ["url", "login_username", "login_password", "mail_username", "mail_password"]:
        var = f"DIMAGIQA_{name.upper()}"
        if var in os.environ:
            settings[name] = os.environ[var]
    if "url" not in settings:
        env = os.environ.get("DIMAGIQA_ENV") or "staging"
        subdomain = "www" if env == "production" else env
        settings["url"] = f"https://{subdomain}.commcarehq.org/"
    return settings


@pytest.fixture(scope="session")
def settings(environment_settings):
    if os.environ.get("CI") == "true":
        settings = environment_settings
        settings["CI"] = "true"
        if any(x not in settings for x in ["url", "login_username", "login_password", "mail_username", "mail_password"]):
            lines = environment_settings.__doc__.splitlines()
            vars_ = "\n  ".join(line.strip() for line in lines if "DIMAGIQA_" in line)
            raise RuntimeError(
                f"Environment variables not set:\n  {vars_}\n\n"
                "See https://docs.github.com/en/actions/reference/encrypted-secrets "
                "for instructions on how to set them."
            )
        return settings
    path = Path(__file__).parent.parent / "settings.cfg"
    if not path.exists():
        raise RuntimeError(
            f"Not found: {path}\n\n"
            "Copy settings-sample.cfg to settings.cfg and populate "
            "it with values for the environment you want to test."
        )
    settings = ConfigParser()
    settings.read(path)
    return settings["default"]


@pytest.fixture(scope="module")
def driver(settings):
    chrome_options = webdriver.ChromeOptions()
    if settings.get("CI") == "true":
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-extensions')
        chrome_options.add_argument('--safebrowsing-disable-download-protection')
        chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
        chrome_options.add_argument('window-size=1920,1080')
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": str(UserData.DOWNLOAD_PATH),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True})
    else:
        chrome_options.add_argument('--safebrowsing-disable-download-protection')
        chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
        # Local Headless
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument('--headless')
        # chrome_options.set_capability("browserVersion", "94.0.4606")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": str(UserData.DOWNLOAD_PATH),
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True})
    web_driver = Service(executable_path=ChromeDriverManager().install(), service_args=['--verbose', 'log_path="/logs/chrome.log"'])
    driver = webdriver.Chrome(service=web_driver, options=chrome_options)
    print("Chrome version:", driver.capabilities['browserVersion'])
    login = LoginPage(driver, settings["url"])
    login.login(settings["login_username"], settings["login_password"])
    yield driver
    driver.close()
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
# @pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == "call" or report.when == "teardown":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            print("reports skipped or failed")
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot(item.funcargs["driver"])
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(driver):
    return driver.get_screenshot_as_base64()


'''
#Email Utility (For reference)
@pytest.fixture
def email_pytest_report(req):
    "pytest fixture for device flag"
    return req.config.getoption("--email_pytest_report")

# Command line options:
def pytest_addoption(parser):
    parser.addoption("--email_pytest_report",
                 dest="email_pytest_report",
                 help="Email pytest reports: Y or N",
                 default="Y")


def pytest_terminal_summary(terminalreporter, exitstatus):
    "add additional section in terminal summary reporting."
    username = os.environ.get("DIMAGIQA_MAIL_USERNAME")
    password = os.environ.get("DIMAGIQA_MAIL_PASSWORD")
    print(username, password)
    print("entering the terminal summery")
    if not hasattr(terminalreporter.config, 'workerinput'):
        print("terminalreporter has workerinput")
        print(terminalreporter.config.getoption("--email_pytest_report"))
        if terminalreporter.config.getoption("--email_pytest_report").lower() == 'y':
            print("creating email")
            # Initialize the Email_Pytest_Report object
            email_obj = Email_Pytest_Report()
            # Send html formatted email body message with pytest reports as an attachment
            email_obj.send_test_report_email(username,password,html_body_flag=True, attachment_flag=True, report_file_path='reports.html')
            print("send email: Yes")
'''