# === tests/test_login.py ===
import time
from pages.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)
    login.visit("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    login.login("test@example.com", "password")
    assert "My account" in driver.page_source
    time.sleep(2)