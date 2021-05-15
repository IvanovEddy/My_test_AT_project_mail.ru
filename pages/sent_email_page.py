from selenium.webdriver.common.by import By

from pages.email_page import EmailPage


class SentEmailPage(EmailPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.short_url = "/sent/"
        self.last_sent_letter = lambda: self.driver.find_element(By.XPATH, '//a[contains(@class, "llc")][1]')
        self.letter_contact = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.letter__author span.letter-contact')
        self.letter_recipients = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.letter__recipients span.letter-contact')
        self.letter_body = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class, "cl_")]/div[1]')

    def is_sent_email_page(self):
        self.wait_for_true(lambda driver: "Отправленные" in self.menu_name().get_attribute('title'))
        self.validate_url()
        assert self.is_element_present(self.letter_list()) is not None, "Не отображает письма"

    def last_sent_email_is_correct(self):
        self.wait_for_true(lambda driver: "Отправленные" in self.menu_name().get_attribute('title'))
        self.last_sent_letter().click()
        self.wait_for_element_display_and_enable(self.letter_contact)
        assert self.email in self.letter_contact().get_attribute('title')
        assert self.email in self.letter_recipients().get_attribute('title')
        assert f"Привет! Я {self.name}!" in self.letter_body().text





