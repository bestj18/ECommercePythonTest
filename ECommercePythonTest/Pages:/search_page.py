# === pages/search_page.py ===
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "search_query_top")
        self.search_button = (By.NAME, "submit_search")

    def search(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()