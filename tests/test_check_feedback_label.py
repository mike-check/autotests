import random

from src.nps_window import NPSWindow


def test_check_feedback_label(driver_setup):
    page = NPSWindow(driver_setup)
    page.click_rate(random.randint(0, 6))
    assert page.is_feedback_label_correct()
