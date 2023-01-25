from selenium.webdriver.common.by import By
from pages.base import Base

ORG_SETTINGS_ICON = (By.CSS_SELECTOR, ".navigation-footer .text-ellipsis")
ORG_HEADER_TITLE = (By.CSS_SELECTOR, ".bolt-master-panel-header-title")
ORG_TITLE = "Organization Settings"


class Org(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_org_settings_icon(self):
        self.is_visible(ORG_SETTINGS_ICON).click()

    def verify_org_page_title(self):
        assert self.is_visible(ORG_HEADER_TITLE).text == ORG_TITLE
