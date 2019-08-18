from src.nps_window import NPSWindow


def test_check_welcome_label(driver_setup):
    page = NPSWindow(driver_setup)
    assert page.is_welcome_label_correct()
