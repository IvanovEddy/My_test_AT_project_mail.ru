from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from config_test import Config


class BasePage:
    email = ""
    password = ""
    base_url = ""
    short_url = ""

    def __init__(self, driver):
        self.driver = driver
        self.config = Config()
        self.base_url = self.config.base_url
        self.email = self.config.email
        self.password = self.config.password
        self.name = self.config.name

    @property
    def url(self):
        return self.base_url + self.short_url

    def open(self):
        """Открывает нужную url страницу"""
        self.driver.get(self.url)

    def wait_for_true(self, bool_condition):
        """Ожидание какого-либо условия
        :param bool_condition: функция-условие
        """
        WebDriverWait(self.driver, 10).until(bool_condition)

    def wait_for_element_display_and_enable(self, element_func):
        """Ожидание пока эелемент не станет отображен и доступен"""
        def is_element_present(driver):
            try:
                element_func()
                if element_func().is_enabled() and element_func().is_displayed():
                    return True
                else:
                    return False
            except NoSuchElementException:
                return False

        WebDriverWait(self.driver, 10).until(is_element_present)

    def is_element_present(self, element):
        """Проверка наличия элемента"""
        try:
            element
        except NoSuchElementException:
            return False
        return True

    def validate_url(self):
        assert self.url in self.driver.current_url
