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

    def login_user(self):

        self.wait_for_element_display_and_enable(self.email_input)
        self.email_input().send_keys(f"{self.email}")
        self.submit_button().click()
        self.wait_for_element_display_and_enable(self.password_input)
        self.password_input().send_keys(f"{self.password}")
        self.email_enter_button().click()

    def go_to_mail_page(self):
        self.mail_link().click()
