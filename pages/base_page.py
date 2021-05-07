class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self, url):
        self.driver.open(self.url)
