from src.nps_window import NPSWindow


def test_check_welcome_label(driver_setup):
    page = NPSWindow(driver_setup)
    page.click_close()
    assert page.is_window_absent()
