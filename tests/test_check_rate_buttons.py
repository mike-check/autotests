import pytest

from src.nps_window import NPSWindow


@pytest.mark.parametrize('rate', [x for x in range(11)])
def test_check_rate_buttons(driver_setup, rate):
    page = NPSWindow(driver_setup)
    page.click_rate(rate)
    if rate in range(7, 11):
        assert page.is_window_absent()
    else:
        assert page.is_feedback_present()
