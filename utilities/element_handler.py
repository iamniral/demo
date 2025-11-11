import configparser
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import ROOT_DIR

config = configparser.ConfigParser()
config.sections()
config.read(f"{ROOT_DIR}/config.ini")

class ElementHandler:
    def __init__(self, driver):
        self.driver = driver
        self.default_wait = config["default_wait"]["element_wait"]

    def wait_for_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, float(self.default_wait)).until(expected_conditions.visibility_of_element_located(locator))

    def click_on_continue_button(self, locator1):
        self.wait_for_element_to_be_visible(locator1).click()


