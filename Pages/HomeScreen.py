from Pages.BasePage import BasePage


class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_Signin(self):
        self.wait_for_element_to_be_visible("SIGN_IN_BUTTON").click()

    def click_on_Explore_SmartThings(self):
        self.wait_for_element_to_be_visible("EXPLORE_SMARTTHINGS").click()
