import pytest
import time
import warnings

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.nps_window import NPSWindow


@pytest.fixture
def driver_name(request):
    driver_name = request.config.getoption('driver')
    if driver_name is None:
        driver_name = 'Chrome'
        warnings.warn(UserWarning("--driver should be specified. 'Chrome' is chosen by default"))
    driver_name = driver_name.title()
    return driver_name


@pytest.fixture(scope="function")
def driver_setup(request, driver_name):
    driv = driver_name
    if driv == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
    driver.get("http://localhost:58001/")
    driver.delete_cookie("NPS_sended")
    driver.implicitly_wait(0.3)
    timeout = time.time() + 20
    while not NPSWindow(driver).is_main_window_present() and\
            time.time() < timeout:
        driver.get("http://localhost:58001/")
        driver.delete_cookie("NPS_sended")
    driver.implicitly_wait(3)
    request.node._driver = driver
    yield driver
    driver.quit()
