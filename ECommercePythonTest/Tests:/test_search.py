# === tests/test_search.py ===
import time
from pages.search_page import SearchPage

def test_search(driver):
    search = SearchPage(driver)
    search.visit("http://automationpractice.com")
    search.search("dress")
    assert "search" in driver.current_url
    time.sleep(2)