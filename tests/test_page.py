import time

import pytest

from utilities.selenium_utils import alert_displayed
from page_objects.pages.PracticePage import PracticePage

@pytest.fixture(autouse = True)
def open_page(driver):
    practice_page = PracticePage(driver)
    practice_page.open_page()
    return practice_page

def test_logo(driver, open_page):
    assert open_page.check_logo_is_present()

def test_practice_page_text(driver, open_page):
    assert open_page.check_practice_page_text()

def test_select_bmw_in_radio_example(driver, open_page):
    assert open_page.select_radio_example_bmw()

def test_select_honda_in_checkbox_example(driver, open_page):
    assert open_page.select_honda_in_checkbox_example()

def test_select_benz_in_class_example(driver, open_page):
    assert open_page.select_class_example_benz()

def test_peach_in_multiple_select_example(driver, open_page):
    assert open_page.select_peach_in_multiple_select_example()

def test_given_input_into_auto_suggest_example(driver, open_page):
    open_page.give_input_in_auto_suggest("Vinay")

def test_click_disable_button(driver, open_page):
    open_page.click_disable_in_enabled_or_disabled()

def test_click_hide_in_element_displayed(driver, open_page):
    open_page.click_element_displayed_hide()
    assert open_page.check_input_element_displayed_button_not_displayed()

def test_click_show_in_element_displayed(driver, open_page):
    open_page.click_element_displayed_show()
    assert open_page.check_input_element_displayed_button_displayed()

@pytest.mark.parametrize("name", ["vinay", "Name"])
def test_click_alert(driver, open_page, name):
    open_page.give_input_in_switch_alert_example(name)
    open_page.click_switch_to_alert_button()
    alert_displayed(driver, 10)
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_text = f"Hello {name}, share this practice page and share your knowledge"
    assert alert_text == expected_text
    alert.accept()

def test_mouse_hover(driver, open_page):
    open_page.click_mouse_hover_button()
    open_page.click_mouse_hover_top()
    time.sleep(5)
    open_page.click_mouse_hover_button()
    open_page.click_mouse_hover_reload()

def test_iframe_example_is_present(driver, open_page):
    assert open_page.check_iframe_example_section_is_present()

def test_click_all_courses_and_then_first_course_and_check_firstcourse_is_present(driver, open_page):
    open_page.click_on_all_courses_section_in_iframes()
    open_page.click_on_first_course_in_iframes()
    assert open_page.check_first_course_is_displayed()

def test_click_switch_tab_example_open(driver, open_page):
    main_window = driver.current_window_handle
    open_page.click_open_in_switch_tab_example()
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break
    assert open_page.find_new_tab_element()
    driver.switch_to.window(main_window)