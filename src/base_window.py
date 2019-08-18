import logging
from time import sleep

logging.basicConfig(level=logging.INFO)


class BaseWindow:
    def __init__(self, driver=None, locator_map=None):
        self.dr = driver
        self.lm = locator_map

    def click_button(self, element, n=None):
        button, by_method, locator = self.get_element(element, n)
        logging.info(
            "Clicking on button '{}' which was funded by {}".format(
                locator, by_method))
        button.click()

    def get_element(self, element, n=None):
        by_method, locator = self.lm[element]
        if n:
            locator = '{}[.="{}"]'.format(locator, n)
        return self.dr.find_element(by_method, locator), by_method, locator

    def input_text(self, element, n=None, text=""):
        element, by_method, locator = self.get_element(element, n)
        logging.info(
            "Input text '{}' in field '{}' which was funded by {}".format(
                text, locator, by_method))
        element.send_keys(text)

    def is_element_absent(self, element, n=None):
        element, by_method, locator = self.get_element(element, n)
        sleep(1)
        actual_state = element.is_displayed()
        logging.info(
            "Actual state of '{}' which was funded by {} is {}".format(
                locator, by_method, actual_state))
        return not actual_state

    def is_element_present(self, element, n=None):
        element, by_method, locator = self.get_element(element, n)
        actual_state = element.is_displayed()
        logging.info(
            "Actual state of '{}' which was funded by {} is {}".format(
                locator, by_method, actual_state))
        return actual_state

    def is_label_correct(self, exp, element, n=None):
        label, by_method, locator = self.get_element(element, n)
        act = label.get_property("innerText")
        actual_state = act == exp
        logging.info(
            "Expected value '{}'' is equal to actual '{}': {}".format(
                exp, act, actual_state))
        return actual_state

