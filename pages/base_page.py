from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = "https://mail.ru/"
    short_url = ""
    url = base_url + short_url

    def __init__(self, driver):
        self.driver = driver

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
