from appium.webdriver.common.appiumby import AppiumBy

from utilities.permission_element_handler import PermissionElementHandler


class IntroScreen:
    def __init__(self, driver):
        self.driver = driver
        self.element_handler = PermissionElementHandler(driver)
        self.INTRO_ALLOW_BUTTON = (AppiumBy.ID, 'com.samsung.android.oneconnect:id/intro_allow_button')
        self.MORE_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@text = "More"]')
        self.CONTINUE_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@text = "Continue"]')
        self.SKIP_BUTTON = (AppiumBy.ID, 'com.samsung.android.oneconnect:id/cancel')

    def accept_intro_permission(self):
        self.element_handler.click_on_intro_permission(self.INTRO_ALLOW_BUTTON, self.MORE_BUTTON, self.CONTINUE_BUTTON, self.SKIP_BUTTON)


