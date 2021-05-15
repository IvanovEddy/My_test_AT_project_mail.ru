from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class EmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.write_new_email_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'a[title = "Написать письмо"]')
        self.dropdown_auth_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-auth span.ph-dropdown-icon')
        self.auth_user_name = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-item__active-user div.ph-name')
        self.auth_user_email = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.ph-item__active-user div.ph-desc')
        self.letter_list = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.letter-list')
        self.email_body_textbox = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class, "editable-container")]/div[1]')
        self.send_email_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'span[title="Отправить"]')
        self.contact_input = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class,"contactsContainer")]//input')
        self.subject_input = lambda: self.driver.find_element(By.XPATH, '//div[contains(@class,"subject__container")]//input')
        self.close_email_was_sent_msg_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'span[title="Закрыть"]')
        self.sent_letters_button = lambda: self.driver.find_element(By.CSS_SELECTOR, 'a[title="Отправленные"]')
        self.menu_name = lambda: self.driver.find_element(By.CSS_SELECTOR, 'div.portal-menu-element__text')
        self.base_url = "https://e.mail.ru"
        self.short_url = "/inbox/"

    def is_email_page(self):
        """Проверяет является ли страницей электронной почты"""
        self.wait_for_element_display_and_enable(self.write_new_email_button)
        self.validate_url()
        self.should_be_emails_dataset()
        self.should_be_send_email_button()

    def should_be_emails_dataset(self):
        """Проверяет наличие писем на странице"""
        assert self.is_element_present(self.letter_list()) is not None, "Не отображает письма"

    def should_be_send_email_button(self):
        """Проверяет наличие кнопки 'Написать письмо'"""
        assert self.is_element_present(self.write_new_email_button()) is not None, "Нет кнопки отправить сообщение"

    def user_is_authorised(self):
        """Проверяет что пользователь авторизован под верными данными"""
        self.wait_for_element_display_and_enable(self.dropdown_auth_button)
        self.dropdown_auth_button().click()
        self.wait_for_element_display_and_enable(self.auth_user_name)
        assert self.auth_user_name().text == f'{self.name}', "Отображается неверное имя пользователя"
        assert self.auth_user_email().text == f'{self.email}', "Отображается неверный email"

    def send_new_email(self):
        """Отправляет новое письмо"""
        self.wait_for_element_display_and_enable(self.write_new_email_button)
        self.write_new_email_button().click()
        self.wait_for_element_display_and_enable(self.email_body_textbox)
        self.email_body_textbox().send_keys(f"Привет! Я {self.name}!")
        self.contact_input().send_keys(f"{self.email}")
        self.subject_input().send_keys("Привет!")
        self.send_email_button().click()
        self.wait_for_element_display_and_enable(self.close_email_was_sent_msg_button)
        self.close_email_was_sent_msg_button().click()

    def go_to_sent_emails(self):
        """Переход на страницу 'Отправленные'"""
        self.wait_for_element_display_and_enable(self.sent_letters_button)
        self.sent_letters_button().click()






