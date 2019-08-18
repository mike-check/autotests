import logging
from time import sleep

logging.basicConfig(level=logging.INFO)


class BaseWindow():
    def __init__(self, driver=None, locator_map=None):
        self.dr = driver
        self.lm = locator_map

    def click_button(self, element, n=None):
        by_method, locator = self.lm[element]
        if n:
            locator = '{}[.="{}"]'.format(locator, n)
        button = self.dr.find_element(by_method, locator)
        logging.info("Clicking on button '{}' finded by {}".format(
            locator, by_method))
        button.click()

    def input_text(self, element, n=None, text=""):
        by_method, locator = self.lm[element]
        if n:
            locator = '{}[.="{}"]'.format(locator, n)
        element = self.dr.find_element(by_method, locator)
        logging.info("Input text '{}' in field '{}' finded by {}".format(
            text, locator, by_method))
        element.send_keys(text)

    def is_element_absent(self, element, n=None):
        by_method, locator = self.lm[element]
        if n:
            locator = '{}[.="{}"]'.format(locator, n)
        sleep(1)
        element = self.dr.find_element(by_method, locator)
        actual_state = element.is_displayed()
        logging.info("Actual state of '{}' finded by {} is {}".format(
            locator, by_method, actual_state))
        return not actual_state

    def is_element_present(self, element, n=None):
        by_method, locator = self.lm[element]
        if n:
            locator = '{}[.="{}"]'.format(locator, n)
        element = self.dr.find_element(by_method, locator)
        actual_state = element.is_displayed()
        logging.info("Actual state of '{}' finded by {} is {}".format(
            locator, by_method, actual_state))
        return actual_state

    def is_label_correct(self, exp, element, n=None):
        by_method, locator = self.lm[element]
        if n:
            locator = '{}[.="{}"]'.format(locator, n)
        label = self.dr.find_element(by_method, locator)
        act = label.get_property("innerText")
        actual_state = act == exp
        logging.info("Expected value '{}'' is equal to actual '{}': {}".format(
            exp, act, actual_state))
        return actual_state

