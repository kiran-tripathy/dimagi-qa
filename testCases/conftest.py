import os
from configparser import ConfigParser
from pathlib import Path
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from testPages.loginPage import LoginPage
from selenium.webdriver.chrome.options import Options
from UserInputs.userInputsData import UserInputsData
from datetime import datetime
import time
# from pytest_html_reporter import attach
import base64
from utilities.email_pytest_report import Email_Pytest_Report

driver = None

def load_settings_from_environment():
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


def load_settings():
    if os.environ.get("CI") == "true":
        settings = load_settings_from_environment()
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

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="class")
def init_driver(request):
    settings = load_settings()
    chrome_options = Options()
    global driver
    if os.environ.get("CI") == "true":
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-extensions')
        chrome_options.add_argument('--safebrowsing-disable-download-protection')
        chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
        chrome_options.add_argument('window-size=1920,1080')
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
           # "download.default_directory": str(UserInputsData.download_path),
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True})
    web_driver = ChromeDriverManager().install()

    driver = webdriver.Chrome(executable_path=web_driver, options=chrome_options)
    request.cls.driver = driver
    login = LoginPage(request.cls.driver, settings["url"])
    login.login(settings["login_username"], settings["login_password"])
    
    yield driver

    driver.close()
    driver.quit()
    


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    print("entering report formation")
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield 
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    print(report)
    print("init", item.funcargs)
   
    if report.when == "call" or report.when == "teardown": 
        
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png" 
            #file_name = None
            screen_img = _capture_screenshot(item.funcargs['init_driver'])
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
    report.extra = extra
   
def _capture_screenshot(driver):
    return driver.get_screenshot_as_base64()
"""
def _capture_screenshot(driver):
    '''
         The screenshot is saved as base64
    '''
    SCREENSHOT_DIR = UserInputsData.Screenshots
    now_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    screen_path = os.path.join(SCREENSHOT_DIR, "{}.png".format(now_time))
    driver.save_screenshot(screen_path)
    with open(screen_path, 'rb') as f:
        imagebase64 = base64.b64encode(f.read())
    return imagebase64.decode()
"""
@pytest.fixture
def email_pytest_report(req):
    "pytest fixture for device flag"
    return req.config.getoption("--email_pytest_report")

# Command line options:
def pytest_addoption(parser):
    parser.addoption("--email_pytest_report",
                 dest="email_pytest_report",
                 help="Email pytest report: Y or N",
                 default="N")

def pytest_terminal_summary(terminalreporter, exitstatus):
    "add additional section in terminal summary reporting."
    print("entering the terminal summery")
    if not hasattr(terminalreporter.config, 'workerinput'):
        if terminalreporter.config.getoption("--email_pytest_report").lower() == 'y':
            # Initialize the Email_Pytest_Report object
            email_obj = Email_Pytest_Report()
            # Send html formatted email body message with pytest report as an attachment
            email_obj.send_test_report_email(html_body_flag=True, attachment_flag=True, report_file_path='default')