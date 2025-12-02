from Pages.BasePage import BasePage
from SmartThings.locators import SmartThingsLocators
from driver_manager import driver


class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gotoSignIn(self):

        driver.find_element(*SmartThingsLocators.SIGN_IN).click()
        self.wait_for_element_to_be_visible(INTRO_TITLE_XPATH)


