from appium.webdriver.common.appiumby import AppiumBy

from utilities.element_handler import ElementHandler


class PermissionScreen:
    def __init__(self, driver):
        self.driver = driver
        self.element_handler = ElementHandler(driver)
        self.continue_button = (AppiumBy.XPATH, '//android.widget.Button[@text = "Continue"]')
        self.while_using_App_Permission = (AppiumBy.XPATH, '//*[contains(@text,"While using the app")]')
        self.Permission_allow_button = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')

    def accept_permission(self):
        self.element_handler.click_on_continue_button(self.continue_button)