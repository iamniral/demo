import configparser

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities import configReader

# config = configparser.ConfigParser()
# config.sections()
# config.read("..\\ConfigurationData\\config.ini")

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = configReader.readConfig("WAIT TIMEOUTS", "   element_wait")

    # def default_wait(self, element_wait):
    #      self.default_wait = configReader.readConfig("WAIT TIMEOUTS", element_wait)

    def wait_for_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, float(self.timeout)).until(
            expected_conditions.visibility_of_element_located(configReader.readConfig("locators", locator)))
