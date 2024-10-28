from utilities.selenium_utils import wait_for_element_to_be_visible, wait_for_element_to_be_clickable, \
    wait_for_element_to_be_invisible
from page_objects.locators import FIRST_LOGO_XPATH, PRACTICE_PAGE, SELECT_BMW_RADIO_EXAMPLE, \
    SELECT_HONDA_CHECKBOX_EXAMPLE, SELECT_CLASS_EXAMPLE_BENZ, MULTIPLE_SELECT_EXAMPLE_PEACH, AUTO_SUGGEST_EXAMPLE_INPUT, \
    DISABLE_BUTTON, ELEMENT_DISPLAYED_HIDE, ELEMENT_DISPLAYED_SHOW, HIDE_OR_SHOW_EXAMPLE, SWITCH_TO_ALERT_BUTTON, \
    MOUSE_HOVER_BUTTON, MOUSE_HOVER_TOP, MOUSE_HOVER_RELOAD, IFRAME_EXAMPLE, ALL_COURSES_CSS, FIRST_COURSE, \
    FIRST_COURSE_NAME_AFTER_CLICKING, SWITCH_TO_ALERT_INPUT, SWITCH_TAB_EXAMPLE_OPEN, NEW_TAB_ELEMENT

from tests.conftest import driver

class PracticePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.letskodeit.com/practice")

    def check_logo_is_present(self):
        check_logo = wait_for_element_to_be_visible(self.driver, FIRST_LOGO_XPATH, 10)
        return check_logo.is_displayed()

    def check_practice_page_text(self):
        check_practice_page_text_1 = wait_for_element_to_be_visible(self.driver, PRACTICE_PAGE, 10)
        return check_practice_page_text_1.is_displayed()

    def select_radio_example_bmw(self):
        click_bmw_in_radio_example = wait_for_element_to_be_clickable(self.driver, SELECT_BMW_RADIO_EXAMPLE, 10)
        click_bmw_in_radio_example.click()
        return click_bmw_in_radio_example.is_selected()

    def select_honda_in_checkbox_example(self):
        click_honda_in_checkbox_example = wait_for_element_to_be_clickable(self.driver, SELECT_HONDA_CHECKBOX_EXAMPLE, 10)
        click_honda_in_checkbox_example.click()
        return click_honda_in_checkbox_example.is_selected()

    def select_class_example_benz(self):
        select_benz_in_class_example = wait_for_element_to_be_clickable(self.driver, SELECT_CLASS_EXAMPLE_BENZ, 10)
        select_benz_in_class_example.click()
        return select_benz_in_class_example.is_selected()

    def select_peach_in_multiple_select_example(self):
        click_peach_in_multiple_select_example = wait_for_element_to_be_clickable(self.driver, MULTIPLE_SELECT_EXAMPLE_PEACH, 10)
        click_peach_in_multiple_select_example.click()
        return click_peach_in_multiple_select_example.is_selected()

    def give_input_in_auto_suggest(self, input1):
        auto_suggest_input = wait_for_element_to_be_clickable(self.driver, AUTO_SUGGEST_EXAMPLE_INPUT, 10)
        return auto_suggest_input.send_keys(input1)

    def click_disable_in_enabled_or_disabled(self):
        click_disable = wait_for_element_to_be_clickable(self.driver, DISABLE_BUTTON, 10)
        click_disable.click()

    def click_element_displayed_hide(self):
        click_hide = wait_for_element_to_be_clickable(self.driver, ELEMENT_DISPLAYED_HIDE, 10)
        click_hide.click()

    def check_input_element_displayed_button_not_displayed(self):
        check_element_input_displayed = wait_for_element_to_be_invisible(self.driver, HIDE_OR_SHOW_EXAMPLE, 10)
        return check_element_input_displayed

    def click_element_displayed_show(self):
        click_show = wait_for_element_to_be_clickable(self.driver, ELEMENT_DISPLAYED_SHOW, 10)
        click_show.click()

    def check_input_element_displayed_button_displayed(self):
        check_element_input_displayed = wait_for_element_to_be_visible(self.driver, HIDE_OR_SHOW_EXAMPLE, 10)
        return check_element_input_displayed.is_displayed()

    def give_input_in_switch_alert_example(self, name):
        switch_alert_input = wait_for_element_to_be_clickable(self.driver, SWITCH_TO_ALERT_INPUT, 10)
        return switch_alert_input.send_keys(name)

    def click_switch_to_alert_button(self):
        click_alert_button = wait_for_element_to_be_clickable(self.driver, SWITCH_TO_ALERT_BUTTON, 10)
        click_alert_button.click()

    def click_mouse_hover_button(self):
        click_mouse_hover = wait_for_element_to_be_clickable(self.driver, MOUSE_HOVER_BUTTON, 10)
        click_mouse_hover.click()

    def click_mouse_hover_top(self):
        click_top_in_mouse_hover = wait_for_element_to_be_clickable(self.driver, MOUSE_HOVER_TOP, 10)
        click_top_in_mouse_hover.click()

    def click_mouse_hover_reload(self):
        click_reload_in_mouse_hover = wait_for_element_to_be_clickable(self.driver, MOUSE_HOVER_RELOAD, 10)
        click_reload_in_mouse_hover.click()

    def check_iframe_example_section_is_present(self):
        check_iframe_example_is_present = wait_for_element_to_be_visible(self.driver, IFRAME_EXAMPLE, 10)
        return check_iframe_example_is_present.is_displayed()

    def click_on_all_courses_section_in_iframes(self):
        self.driver.switch_to.frame('courses-iframe')
        click_on_all_courses_in_iframe = wait_for_element_to_be_clickable(self.driver, ALL_COURSES_CSS, 10)
        click_on_all_courses_in_iframe.click()
        self.driver.switch_to.default_content()

    def click_on_first_course_in_iframes(self):
        self.driver.switch_to.frame("courses-iframe")
        click_first_course_in_iframes = wait_for_element_to_be_clickable(self.driver, FIRST_COURSE, 10)
        click_first_course_in_iframes.click()
        self.driver.switch_to.default_content()

    def check_first_course_is_displayed(self):
        self.driver.switch_to.frame("courses-iframe")
        check_first_course_with_course_name = wait_for_element_to_be_visible(self.driver, FIRST_COURSE_NAME_AFTER_CLICKING, 10)
        return check_first_course_with_course_name.is_displayed()
    def click_open_in_switch_tab_example(self):
        click_switch_tab_example_open = wait_for_element_to_be_clickable(self.driver, SWITCH_TAB_EXAMPLE_OPEN, 10)
        click_switch_tab_example_open.click()

    def find_new_tab_element(self):
        new_tab_element1 = wait_for_element_to_be_visible(self.driver, NEW_TAB_ELEMENT, 10)
        return new_tab_element1.is_displayed()