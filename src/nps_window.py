from selenium.common.exceptions import NoSuchElementException
from src.locators import nps_locators
from src.base_window import BaseWindow
from src.settings import (
    dislike,
    feedback,
    like,
    welcome
)


class NPSWindow(BaseWindow):
    def __init__(self, driver=None, locator_map=nps_locators):
        super().__init__(driver, locator_map)

    def click_close(self):
        self.click_button("Close Button")

    def click_rate(self, n=0):
        self.click_button("General Rate Button", n)

    def get_cookie(self):
        return self.dr.get_cookie("NPS_sended")

    def input_feedback(self, text):
        self.input_text("Feedback Textarea", text=text)

    def is_main_window_present(self):
        try:
            self.dr.find_element(
                nps_locators["Main Window"][0],
                nps_locators["Main Window"][1])
            return 1
        except NoSuchElementException:
            return 0

    def is_dislike_label_correct(self, exp=dislike):
        return self.is_label_correct(exp, "Title Not Like")

    def is_feedback_label_correct(self, exp=feedback):
        return self.is_label_correct(exp, "Feedback Label")

    def is_feedback_present(self):
        return self.is_element_present("Feedback Input")

    def is_like_label_correct(self, exp=like):
        return self.is_label_correct(exp, "Title Like")

    def is_welcome_label_correct(self, exp=welcome):
        return self.is_label_correct(exp, "Title Welcome")

    def is_window_absent(self):
        return self.is_element_absent("Main Window")

    def click_send_button(self):
        self.click_button("Send Button")
