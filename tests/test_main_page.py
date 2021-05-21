import allure
from pages.email_page import EmailPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sent_email_page import SentEmailPage


@allure.feature("Авторизация с главной страницы")
@allure.severity("Blocker")
def test_user_can_login_from_main_page(driver):
    """Тест на проверку авторизации с главной страницы"""
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(driver)
        main_page.open()
    with allure.step("Проверка url"):
        main_page.validate_url()
    with allure.step("Авторизовать пользователя"):
        main_page.login_user()
        email_page = EmailPage(driver)
    with allure.step("Проверка является ли страница email page"):
        email_page.is_email_page()
    with allure.step("Проверка что пользователь авторизован"):
        email_page.user_is_authorised()


@allure.feature("Авторизация при попытке открыть электронную почту")
@allure.severity("Blocker")
def test_user_can_login_from_email_page(driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(driver)
        main_page.open()
    with allure.step("Перейти на страницу почты"):
        main_page.go_to_mail_page()
    with allure.step("Проверка является ли страница страницей авторизации"):
        login_page = LoginPage(driver)
        login_page.is_login_page()
    with allure.step("Авторизовать пользователя"):
        login_page.login_user()
        email_page = EmailPage(driver)
    with allure.step("Проверка является ли страница email page"):
        email_page.is_email_page()
    with allure.step("Проверка что пользователь авторизован"):
        email_page.user_is_authorised()


@allure.feature("Отправить новое письмо")
@allure.severity("Blocker")
def test_user_can_send_new_email(driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(driver)
        main_page.open()
    with allure.step("Перейти на страницу почты"):
        main_page.go_to_mail_page()
    with allure.step("Проверка является ли страница страницей авторизации"):
        login_page = LoginPage(driver)
        login_page.is_login_page()
    with allure.step("Авторизовать пользователя"):
        login_page.login_user()
        email_page = EmailPage(driver)
    with allure.step("Проверка является ли страница email page"):
        email_page.is_email_page()
    with allure.step("Проверка что пользователь авторизован"):
        email_page.user_is_authorised()
    with allure.step("Отправить новое письмо"):
        email_page.send_new_email()
    with allure.step("Перейти в отправленные письма"):
        email_page.go_to_sent_emails()
        sent_email_page = SentEmailPage(driver)
    with allure.step("Проверка является ли страница отправленными письмами"):
        sent_email_page.is_sent_email_page()
    with allure.step("Проверка соотвествия последнего отправленного письма"):
        sent_email_page.last_sent_email_is_correct()

