from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from driver_manager.driver import Driver
from screens.permission_screen import PermissionScreen
from utilities.element_handler import ElementHandler


class TestAcceptPermission:
    def test_accept_permission(self):
        driver = Driver().create_driver_and_return()
        element_handler = ElementHandler(driver)
        self.element_handler


