import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config_cookies import *
from pages.org_page import Org


def pytest_addoption(parser):
    parser.addoption("--which_browser", action="store")


@pytest.fixture
def which_browser(request):
    browser = request.config.getoption("--which_browser")
    return browser


@pytest.fixture
def get_driver(which_browser):
    if which_browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                options=Options())
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options())
    return driver


@pytest.fixture
def setup(get_driver):
    url = BaseData.main_url
    get_driver.maximize_window()
    get_driver.get(url)
    is_valid_cookies_date(get_driver, url)
    yield get_driver
    get_driver.quit()


@pytest.fixture
def org_page(setup):
    yield Org(setup)
