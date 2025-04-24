# === pages/login_page.py ===
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "passwd")
        self.submit_button = (By.ID, "SubmitLogin")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()