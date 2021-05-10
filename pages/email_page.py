from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.send_email_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[title = "Написать письмо"]')

    base_url = "https://e.mail.ru/inbox/"
    short_url = ""
    LETTERS_DATASET = (By.CSS_SELECTOR, '.dataset-letters')

    def is_email_page(self):
        self.should_be_email_url()
        self.should_be_emails_dataset()
        self.should_be_send_email_button()

    def should_be_email_url(self):
        self.wait_for(lambda driver: self.send_email_button().is_enabled() and self.send_email_button().is_displayed())
        assert "https://e.mail.ru/inbox/" in self.driver.current_url, "URL неверный"

    def should_be_emails_dataset(self):
        assert self.is_element_present(self.send_email_button()) is not None, "Email dataset is not presented"

    def should_be_send_email_button(self):
        assert self.is_element_present(self.send_email_button()) is not None, "Send email button is not presented"
