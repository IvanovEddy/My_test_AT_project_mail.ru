from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_input = lambda: self.driver.find_element(By.CSS_SELECTOR, '.password-input')
        self.email_input = lambda: self.driver.find_element(By.CSS_SELECTOR, '.email-input')
        self.email_enter_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-to-mail"]')
        self.mail_link = lambda: driver.find_element(By.CSS_SELECTOR, '.ph-project.svelte-1a5kxdz:nth-of-type(2)')
        self.submit_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[data-testid="enter-password"]')

    short_url = ""

    def login_user(self):

        self.wait_for(lambda driver: self.email_input().is_enabled() and self.email_input().is_displayed())
        self.email_input().send_keys(f"{self.email}")
        self.submit_button().click()
        self.wait_for(lambda driver: self.password_input().is_enabled() and self.password_input().is_displayed())
        self.password_input().send_keys(f"{self.password}")
        self.email_enter_button().click()

    def go_to_mail_page(self):
        self.mail_link().click()
