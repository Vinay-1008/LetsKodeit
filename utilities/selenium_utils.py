from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_to_be_clickable(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_for_element_to_be_visible(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_element_to_be_invisible(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))

def alert_displayed(driver, timeout):
    return WebDriverWait(driver, timeout).until(EC.alert_is_present())