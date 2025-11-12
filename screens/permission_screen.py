from appium.webdriver.common.appiumby import AppiumBy

from utilities.permission_element_handler import PermissionElementHandler


class AppPermissionPopup:
    def __init__(self, driver):
        self.driver = driver
        self.element_handler = PermissionElementHandler(driver)
        self.while_using_App_Permission = (AppiumBy.XPATH, '//*[contains(@text,"While using the app")]')
        self.Permission_allow_button = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')

    def accept_app_permission(self):
        self.element_handler.click_app_permission_button(self.while_using_App_Permission, self.Permission_allow_button, self.Permission_allow_button)