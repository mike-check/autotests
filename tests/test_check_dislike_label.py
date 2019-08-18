from src.nps_window import NPSWindow


def test_check_dislike_label(driver_setup):
    page = NPSWindow(driver_setup)
    assert page.is_dislike_label_correct()
