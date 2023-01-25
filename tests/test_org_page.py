import pytest
from selenium.webdriver.common.by import By

ORG_SETTINGS_ICON = (By.CSS_SELECTOR, ".navigation-footer .text-ellipsis")
ORG_HEADER_TITLE = (By.CSS_SELECTOR, ".bolt-master-panel-header-title")


# create project
# delete project

@pytest.mark.usefixtures("org_page")
class TestOrg:
    def test_org_settings_link(self, org_page):
        org_page.click_org_settings_icon()
        org_page.verify_org_page_title()
