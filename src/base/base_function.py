from selenium.common.exceptions import ElementNotVisibleException as nv, StaleElementReferenceException as sr
from selenium.common.exceptions import NoSuchElementException as ne, TimeoutException as to, ElementClickInterceptedException as ci
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.base import commons


def clicks(driver, page_name, key):
    """
    Clicks if element exists
    :param driver: Webdriver
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    """
    try:
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(commons.get_by_prefix(page_name, key)))
        WebDriverWait(driver, 15).until(ec.element_to_be_clickable(commons.get_by_prefix(page_name, key)))
        commons.get_element(driver, page_name, key).click()
        print(f"Clicks Element {key} from Page {page_name}")
    except (ne, nv, to, ci, sr):
        time.sleep(2)
        commons.get_element(driver, page_name, key).click()
        print(f"2nd try: Clicks Element {key} from Page {page_name}")


def scroll_at_top(driver, page_name, key):
    """
    Scroll to the element, show element on top of the page
    :param driver: Webdriver
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    """
    driver.execute_script("arguments[0].scrollIntoView(true);", commons.get_element(driver, page_name, key))
    print(f"Scroll to element {key} from Page {page_name}, show element on top of the page")


def scroll_until_element_exist(driver, page_name, key, scroll_range):
    """
    Scroll UP or DOWN until element is found in DOM, maximum number of scrolls is 30
    :param driver: Webdriver
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    :param scroll_range: -ve means scroll UP, +ve means scroll down
    """
    count = 0
    direction = "UP"
    if scroll_range[0] == "+":
        direction = "DOWN"
    while not is_element_exist(driver, page_name, key) and count <= 30:
        driver.execute_script(f"window.scrollTo(0, window.scrollY {scroll_range})")
        count += 1
        print(f"Scroll {direction} with range {scroll_range}, Times: {count}")


def is_element_exist(driver, page_name, key):
    """
    Check if element exists in DOM
    :param driver: Webdriver
    :param page_name: cfg file under src/pages
    :param key: key in the cfg file under src/pages
    :return: Boolean True or False
    """
    try:
        WebDriverWait(driver, 0.1).until(ec.visibility_of_element_located(commons.get_by_prefix(page_name, key)))
    except to:
        return False
    return True
