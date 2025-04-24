# === conftest.py ===
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()