from Pages.AppPermissionScreen import AppPermissionScreen
from Pages.HomeScreen import HomeScreen
from Pages.IntroScreen import IntroScreen
from TestCases.BaseTest import BaseTest


class TestAcceptIntroPermissionTest(BaseTest):

    def test_accept_intro_permission(self):
        intro = IntroScreen(self.driver)
        permission = AppPermissionScreen(self.driver)
        intro.introAllow()
        permission.allowAppPermission()








