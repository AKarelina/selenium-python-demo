import time

import pytest
from selenium.webdriver.common.by import By

USER_SETTINGS = (By.CSS_SELECTOR, "[data-renderedregion] .flex-center:nth-child(7)")


# Verify links in user settings
# create project
# delete project

@pytest.mark.usefixtures("org_page")
class TestOrg:
    def test_user_settings_options(self, org_page):
        org_page.is_visible(USER_SETTINGS).click()
        time.sleep(3)
