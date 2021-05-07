from selenium.webdriver.common.by import By
import json

from pages.base_page import BasePage

mail_link_lc = (By.CSS_SELECTOR, ".ph-project.svelte-1a5kxdz:nth-of-type(2)")
email_input_lc = (By.CSS_SELECTOR, ".email-input")
password_input_lc = (By.CSS_SELECTOR, ".password-input")


class MainPage(BasePage):
    def login_user(self, driver):
        with open('files/userdata.json', 'r') as userdata:
            data = json.loads(userdata.read())
            email = data['email']
            password = data['password']

        email_input = driver.find_element(email_input_lc)
        email_input.send_keys(f"{email}")
        password_input = driver.find_element(password_input_lc)
        password_input.send_keys(f"{password}")

    def go_to_mail_page(self, driver):
        mail_link = driver.find_element(mail_link_lc)
        mail_link.click()



