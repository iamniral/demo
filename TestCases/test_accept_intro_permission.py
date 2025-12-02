from driver_manager.driver import Driver
from screens.intro_screen import IntroScreen


class TestAcceptIntroPermissionTest:
    def test_accept_intro_permission(self):
        driver = Driver().create_driver_and_return()
        intro_screen = IntroScreen(driver)
        intro_screen.accept_intro_permission()
