from src.nps_window import NPSWindow


def test_cookies_after_rate(driver_setup):
    page = NPSWindow(driver_setup)
    page.click_rate(10)
    cookie = page.get_cookie()
    assert int(cookie['value']) == 1
