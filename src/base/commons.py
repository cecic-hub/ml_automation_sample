from selenium.webdriver.common.by import By
from src.base import cfg, get_rootdir
import time
from pytest_html import extras
from datetime import datetime

root = get_rootdir.root_path()
mobileWeb = cfg.read_config_data('Details', 'mobileWeb')


def get_element(driver, page_name, key):
    """
    :param driver: Webdriver
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    :return: Web element
    """
    element_details = cfg.pages(page_name, key)
    ele_list = element_details.replace('"', '').split('=', 1)
    prefix = ele_list[0]
    locator = ele_list[1]
    # print(f"Prefix is {prefix}, Locator is {locator}")

    if prefix == 'id':
        element = driver.find_element(By.ID, locator)
    elif prefix == 'xpath':
        element = driver.find_element(By.XPATH, locator)
    elif prefix == 'class_name':
        element = driver.find_element(By.CLASS_NAME, locator)
    elif prefix == 'css_selector':
        element = driver.find_element(By.CSS_SELECTOR, locator)
    else:
        raise Exception(f"Locator strategy/Prefix is missing: {element_details}")
    return element


def get_elements(driver, page_name, key):
    """
    :param driver: Webdriver
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    :return: Web elements
    """
    element_details = cfg.pages(page_name, key)
    ele_list = element_details.replace('"', '').split('=', 1)
    prefix = ele_list[0]
    locator = ele_list[1]
    # print(f"Prefix is {prefix}, Locator is {locator}")

    if prefix == 'id':
        elements = driver.find_elements(By.ID, locator)
    elif prefix == 'xpath':
        elements = driver.find_elements(By.XPATH, locator)
    elif prefix == 'class_name':
        elements = driver.find_elements(By.CLASS_NAME, locator)
    elif prefix == 'css_selector':
        elements = driver.find_elements(By.CSS_SELECTOR, locator)
    else:
        raise Exception(f"Locator strategy/Prefix is missing: {element_details}")
    return elements


def get_by_prefix(page_name, key):
    """
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    :return: Selenium By
    """
    element_details = cfg.pages(page_name, key)
    ele_list = element_details.replace('"', '').split('=', 1)
    prefix = ele_list[0]
    locator = ele_list[1]

    if prefix == 'id':
        by_prefix = (By.ID, locator)
    elif prefix == 'xpath':
        by_prefix = (By.XPATH, locator)
    elif prefix == 'class_name':
        by_prefix = (By.CLASS_NAME, locator)
    elif prefix == 'css_selector':
        by_prefix = (By.CSS_SELECTOR, locator)
    else:
        raise Exception(f"Locator strategy/Prefix is missing: {element_details}")

    return by_prefix


def current_time():
    """
    :return: current time in format '%Y%m%d-%H%M%S'
    """
    return datetime.now().strftime('%Y%m%d-%H%M%S')


def report_screenshot_html(driver, extra):
    """
    Add screenshot to pytest-html report
    :param driver: Webdriver
    :param extra: pytest_html extras
    """
    time.sleep(0.5)
    timestamp = current_time()
    screenshot_path = 'html_screenshots/scr' + timestamp + '.png'
    driver.save_screenshot(root + '/src/report/pytest-html/' + screenshot_path)
    print(f"save screenshot to {root + '/src/report/pytest-html/' + screenshot_path}")
    extra.append(extras.html(
        f'<div class="image"><a href="{screenshot_path}"><img src="{screenshot_path}"></a></div>')
    )
