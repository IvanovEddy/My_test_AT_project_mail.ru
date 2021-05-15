import time

from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class EmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.write_new_email_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[title = "Написать письмо"]')
        self.dropdown_auth_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-auth span.ph-dropdown-icon')
        self.auth_user_name = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-item__active-user div.ph-name')
        self.auth_user_email = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-item__active-user div.ph-desc')
        self.compose_window = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.compose-app')
        self.email_container = lambda: self.driver.find_element(By.CSS_SELECTOR, '.editor-xd8a')
        self.email_body_textbox = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class, "editable-container")]/div[1]')
        self.send_email_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'span[title="Отправить"]')
        self.contact_input = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class,"contactsContainer")]//input')
        self.subject_input = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class,"subject__container")]//input')

    base_url = "https://e.mail.ru/inbox/"
    short_url = ""


    def is_email_page(self):
        self.should_be_email_url()
        self.should_be_emails_dataset()
        self.should_be_send_email_button()

    def should_be_email_url(self):
        self.wait_for_element_display_and_enable(self.write_new_email_button)
        assert "https://e.mail.ru/inbox/" in self.driver.current_url, "URL неверный"

    def should_be_emails_dataset(self):
        assert self.is_element_present(self.write_new_email_button()) is not None, "Не отображает письма"

    def should_be_send_email_button(self):
        assert self.is_element_present(self.write_new_email_button()) is not None, "Нет кнопки отправить сообщение"

    def user_is_authorised(self):
        self.wait_for_element_display_and_enable(self.dropdown_auth_button)
        self.dropdown_auth_button().click()
        self.wait_for_element_display_and_enable(self.auth_user_name)

        assert self.auth_user_name().text == f'{self.name}', "Отображается неверное имя пользователя"
        assert self.auth_user_email().text == f'{self.email}', "Отображается неверный email"

    def send_new_email(self):
        self.wait_for_element_display_and_enable(self.write_new_email_button)
        self.write_new_email_button().click()
        self.wait_for_element_display_and_enable(self.email_body_textbox)
        self.email_body_textbox().send_keys(f"Привет! Я {self.name}!")
        self.contact_input().send_keys(f"{self.email}")
        self.subject_input().send_keys("Привет!")
        self.send_email_button().click()


