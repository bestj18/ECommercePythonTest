# === tests/test_checkout.py ===
import time
from pages.checkout_page import CheckoutPage

def test_checkout(driver):
    checkout = CheckoutPage(driver)
    checkout.visit("http://automationpractice.com")
    checkout.add_to_cart_and_checkout()
    assert "controller=order" in driver.current_url
    time.sleep(2)