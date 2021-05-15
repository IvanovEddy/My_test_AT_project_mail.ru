from pages.email_page import EmailPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sent_email_page import SentEmailPage


def test_user_can_login_from_main_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.validate_url()
    main_page.login_user()
    email_page = EmailPage(driver)
    email_page.is_email_page()
    email_page.user_is_authorised()


def test_user_can_login_from_email_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.go_to_mail_page()
    login_page = LoginPage(driver)
    login_page.is_login_page()
    login_page.login_user()
    email_page = EmailPage(driver)
    email_page.is_email_page()
    email_page.user_is_authorised()


def test_user_can_send_new_email(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.go_to_mail_page()
    login_page = LoginPage(driver)
    login_page.is_login_page()
    login_page.login_user()
    email_page = EmailPage(driver)
    email_page.is_email_page()
    email_page.user_is_authorised()
    email_page.send_new_email()
    email_page.go_to_sent_emails()
    sent_email_page = SentEmailPage(driver)
    sent_email_page.is_sent_email_page()
    sent_email_page.last_sent_email_is_correct()

