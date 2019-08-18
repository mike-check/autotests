from src.nps_window import NPSWindow


def test_close_window(driver_setup):
    page = NPSWindow(driver_setup)
    page.click_close()
    assert page.is_window_absent()
