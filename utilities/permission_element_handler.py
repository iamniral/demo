import configparser
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import ROOT_DIR

config = configparser.ConfigParser()
config.sections()
config.read(f"{ROOT_DIR}/config.ini")

class PermissionElementHandler:
    def __init__(self, driver):
        self.driver = driver
        self.default_wait = config["WAIT TIMEOUTS"]["element wait"]

    def wait_for_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, float(self.default_wait)).until(expected_conditions.visibility_of_element_located(locator))

    def click_app_permission_button(self, locator1, locator2,  locator3):
        self.wait_for_element_to_be_visible(locator1).click()
        self.wait_for_element_to_be_visible(locator2).click()
        self.wait_for_element_to_be_visible(locator3).click()

    def click_on_intro_permission(self, locator1, locator2, locator3, locator4):
        self.wait_for_element_to_be_visible(locator1).click()
        self.wait_for_element_to_be_visible(locator2).click()
        self.wait_for_element_to_be_visible(locator3).click()
        self.wait_for_element_to_be_visible(locator4).click()






