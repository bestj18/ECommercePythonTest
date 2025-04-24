# === pages/checkout_page.py ===
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    def add_to_cart_and_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "ul.product_list a.product_img_link").click()
        self.driver.find_element(By.NAME, "Submit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".button-container a[title='Proceed to checkout']").click()
