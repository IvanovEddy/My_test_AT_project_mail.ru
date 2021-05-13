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
        self.url = self.base_url + self.short_url

    def open(self):
        self.driver.get(self.url)

    def wait_for(self, element):
        WebDriverWait(self.driver, 10).until(element)

    def is_element_present(self, element):
        try:
            element
        except NoSuchElementException:
            return False
        return True

    def validate_url(self):
        assert self.url in self.driver.current_url
