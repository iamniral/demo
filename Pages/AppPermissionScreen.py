from Pages.BasePage import BasePage


class AppPermissionScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def allowAppPermission(self):
        self.wait_for_element_to_be_visible("WHILE_USING_APP_PERMISSION").click()
        self.wait_for_element_to_be_visible("PERMISSION_ALLOW_BUTTON").click()
        self.wait_for_element_to_be_visible("PERMISSION_ALLOW_BUTTON").click()
