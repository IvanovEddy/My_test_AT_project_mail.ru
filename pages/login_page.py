from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = lambda: self.driver.find_element(By.CSS_SELECTOR, '[name="username"]')
        self.email_enter_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="next-button"]')
        self.submit_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="submit-button"]')
        self.password_input = lambda: self.driver.find_element(By.CSS_SELECTOR, '[name="password"]')

    base_url = "https://account.mail.ru/"

    def login_user(self):

        self.wait_for(lambda driver: self.email_input().is_enabled() and self.email_input().is_displayed())
        self.email_input().send_keys(f"{self.email}")
        self.email_enter_button().click()
        self.wait_for(lambda driver: self.password_input().is_enabled() and self.password_input().is_displayed())
        self.password_input().send_keys(f"{self.password}")
        self.submit_button().click()



