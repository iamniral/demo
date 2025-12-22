from Pages.BasePage import BasePage


class IntroScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def introAllow(self):
        self.wait_for_element_to_be_visible("INTRO_ALLOW_BUTTON").click()
        self.wait_for_element_to_be_visible("MORE_BUTTON").click()
        self.wait_for_element_to_be_visible("CONTINUE_BUTTON").click()
        self.wait_for_element_to_be_visible("SKIP_BUTTON").click()
        # self.wait_for_element_to_be_visible("START_SMARTTHINGS_BUTTON").click()
        # self.wait_for_element_to_be_visible("MORE_BUTTON").click()
