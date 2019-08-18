import random
import string

from src.nps_window import NPSWindow


def test_check_rate_buttons(driver_setup):
    letters = string.ascii_lowercase
    text = ''.join(
        random.choice(letters) for i in range(random.randrange(1, 255)))
    page = NPSWindow(driver_setup)
    page.click_rate(random.randint(0, 6))
    page.input_feedback(text)
    page.click_send_button()
    assert page.is_window_absent()
