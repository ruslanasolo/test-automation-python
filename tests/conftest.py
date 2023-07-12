import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param  - to run tests in all browsers ( chrome, safari, firefox)
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        raise TypeError(f"expected 'chrome', but got {browser}")

    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
