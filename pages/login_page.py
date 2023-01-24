from selenium.webdriver.common.by import By
from pages.base import Base
from test_data.data import BaseData

USER_EMAIL = (By.CSS_SELECTOR, "[name='loginfmt']")
BUTTON_SUBMIT = (By.CSS_SELECTOR, ".primary")
USER_PASSWORD = (By.CSS_SELECTOR, "[name='passwd']")


class Login(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(BaseData.login_url)

    def input_email(self):
        self.is_visible(USER_EMAIL).send_keys(BaseData.username)

    def click_submit(self):
        self.is_visible(BUTTON_SUBMIT).click()

    def input_password(self):
        self.is_visible(USER_PASSWORD).send_keys(BaseData.password)
