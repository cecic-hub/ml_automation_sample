import pytest, pytest_html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options
from src.base import get_rootdir, cfg, commons

root = get_rootdir.root_path()
mobile_web = cfg.read_config_data('Details', 'mobileWeb')
headless_flag = cfg.read_config_data('Details', 'headless')
site_url = cfg.read_config_data('Details', 'url')
auto_close = cfg.read_config_data('Details', 'CloseBrowser')
driver_type = cfg.read_config_data('Details', 'Driver')


def browser_option_chrome(options):
    """
    :param options: Chrome Options
    """
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    # close browser after test for chrome
    if auto_close.upper() != 'Y':
        options.add_experimental_option("detach", True)

    if mobile_web.upper() == 'Y':
        # Nexus 5: 360,640; Pixel 2: 411,731
        mobile_emulation = {"deviceName": "Pixel 2"}
        options.add_argument("window-size=360,640")
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        print(f"Mobile web testing")
    else:
        options.add_argument("window-size=1920,1080")
        print(f"Web full screen testing")

    if headless_flag.upper() == 'Y':
        options.add_argument('--headless')
        options.add_argument('–disable-gpu')
        options.add_argument('log-level=3')  # INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
        print(f"Headless mode")


def browser_option_firefox(firefox_path):
    """
    :param firefox_path: Path to install Firefox driver
    :return: Webdriver
    """
    options = FirefoxOptions()
    if headless_flag.upper() == 'Y':
        options.add_argument("--headless")

    driver = webdriver.Firefox(service=firefox_path, options=options)
    if mobile_web.upper() == 'Y':
        driver.set_window_size(360, 640)
    else:
        driver.set_window_size(1920, 1080)

    return driver


def auto_close_browser(driver):
    """
    close browser after test for firefox
    :param driver: Webdriver
    """
    if auto_close.upper() == 'Y':
        driver.quit()
        print(f"Closed browser")


@pytest.fixture(scope="function")
def setup_web(request):
    print(f"initiating {driver_type} driver")
    if driver_type.lower() == "firefox":
        firefox_path = FirefoxService(GeckoDriverManager(path=root + "/Drivers").install())
        driver = browser_option_firefox(firefox_path)
    else:
        chrome_path = ChromeDriverManager(path=root + "/Drivers").install()
        options = Options()
        browser_option_chrome(options)
        driver = webdriver.Chrome(options=options, executable_path=chrome_path)

    request.cls.driver = driver

    driver.get(site_url)

    yield driver
    auto_close_browser(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('setup_web')
        commons.report_screenshot_html(driver, extra)
        report.extra = extra