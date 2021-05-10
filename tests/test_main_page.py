from pages.email_page import EmailPage
from pages.main_page import MainPage


def test_user_can_login(driver):
    page = MainPage(driver)
    page.open()
    page.login_user()
    email_page = EmailPage(driver)
    email_page.is_email_page()
