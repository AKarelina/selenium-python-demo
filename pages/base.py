from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        return self.is_visible(locator).text

    def get_cur_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    def get_cookie(self, name):
        return self.wait.until(lambda d: d.get_cookie(name))

    def verify_text(self, locator, text):
        assert self.driver.find_element(locator).text == text, f"Actual text {self.driver.find_element(locator).text}" \
                                                               f" Expected text {text} "
