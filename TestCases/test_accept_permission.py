from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from driver_manager.driver import Driver
from screens.permission_screen import AppPermissionPopup


class TestAcceptPermission:
    def test_app_permission(self):
        driver = Driver().create_driver_and_return()
        permission_screen = AppPermissionPopup(driver)
        permission_screen.accept_app_permission()


