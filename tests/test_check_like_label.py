from src.nps_window import NPSWindow


def test_check_like_label(driver_setup):
    page = NPSWindow(driver_setup)
    assert page.is_like_label_correct()
