from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.send_email_button = lambda: self.driver.find_element(By.CSS_SELECTOR, '[title = "Написать письмо"]')
        self.dropdown_auth_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-auth span.ph-dropdown-icon')
        self.auth_user_name = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-item__active-user div.ph-name')
        self.auth_user_email = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-item__active-user div.ph-desc')

    base_url = "https://e.mail.ru/inbox/"
    short_url = ""


    def is_email_page(self):
        self.should_be_email_url()
        self.should_be_emails_dataset()
        self.should_be_send_email_button()

    def should_be_email_url(self):
        self.wait_for(lambda driver: self.send_email_button().is_enabled() and self.send_email_button().is_displayed())
        assert "https://e.mail.ru/inbox/" in self.driver.current_url, "URL неверный"

    def should_be_emails_dataset(self):
        assert self.is_element_present(self.send_email_button()) is not None, "Не отображает письма"

    def should_be_send_email_button(self):
        assert self.is_element_present(self.send_email_button()) is not None, "Нет кнопки отправить сообщение"

    def user_is_authorised(self):
        self.wait_for(lambda driver: self.dropdown_auth_button().is_enabled() and self.dropdown_auth_button().is_displayed())
        self.dropdown_auth_button().click()
        self.wait_for(lambda driver: self.auth_user_name().is_enabled() and self.auth_user_name().is_displayed())

        assert self.auth_user_name().text == f'{self.name}', "Отображается неверное имя пользователя"
        assert self.auth_user_email().text == f'{self.email}', "Отображается неверный email"

