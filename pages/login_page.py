from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = lambda: self.driver.find_element(By.CSS_SELECTOR, '[name="username"]')
        self.email_enter_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="next-button"]')
        self.submit_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="submit-button"]')
        self.password_input = lambda: self.driver.find_element(By.CSS_SELECTOR, '[name="password"]')
        self.base_url="https://account.mail.ru/"


    def login_user(self):

        self.wait_for_element_display_and_enable(self.email_input)
        self.email_input().send_keys(f"{self.email}")
        self.email_enter_button().click()
        self.wait_for_element_display_and_enable(self.password_input)
        self.password_input().send_keys(f"{self.password}")
        self.submit_button().click()

    def is_login_page(self):
        self.wait_for_element_display_and_enable(self.email_input)
        assert self.is_element_present(self.email_input()) is not None
        assert self.is_element_present(self.email_enter_button()) is not None
        self.validate_url()





