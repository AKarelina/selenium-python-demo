import time
from collections import ChainMap
from pages.base import Base
from selenium.webdriver.common.by import By
from test_data.data import BaseData
import json

USER_EMAIL = (By.CSS_SELECTOR, "[name='loginfmt']")
BUTTON_SUBMIT = (By.CSS_SELECTOR, ".primary")
USER_PASSWORD = (By.CSS_SELECTOR, "[name='passwd']")
COOKIES_FILE = "/Users/annkarelina/Desktop/pytest/python-selenium-demo/config/cookies.json"


def get_cookies(driver, url):
    driver.get(url)
    Base(driver).is_visible(USER_EMAIL).send_keys(BaseData.username)
    Base(driver).is_visible(BUTTON_SUBMIT).click()
    Base(driver).is_visible(USER_PASSWORD).send_keys(BaseData.password)
    Base(driver).is_visible(BUTTON_SUBMIT).click()
    Base(driver).is_visible(BUTTON_SUBMIT).click()
    new_cookie = Base(driver).get_cookie("UserAuthentication")
    new_value = new_cookie['value']
    cookie_expires = new_cookie['expiry']

    with open(COOKIES_FILE, "r") as f:
        data = json.load(f)
    for d in data:
        d["value"] = new_value
        d["expires"] = cookie_expires
    with open(COOKIES_FILE, "w") as f:
        json.dump(data, f)


def load_cookies(driver, url):
    cookies = json.load(open(COOKIES_FILE, "rb"))
    driver.execute_cdp_cmd("Network.enable", {})
    for cookie in cookies:
        if "expiry" in cookie:
            cookie["expires"] = cookie["expiry"]
            del cookie["expiry"]
        cookie["domain"] = cookie["domain"]
        driver.execute_cdp_cmd("Network.setCookie", cookie)
    driver.execute_cdp_cmd('Network.disable', {})
    driver.get(url)


def is_valid_cookies_date(driver, url):
    with open(COOKIES_FILE, "r") as f:
        data = json.load(f)
    cookies_data = dict(ChainMap(*data))
    actual_date = time.time()
    if actual_date < cookies_data["expires"]:
        load_cookies(driver, url)
    else:
        get_cookies(driver, url)
