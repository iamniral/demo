from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SmartThingsLocators  # Assumed to be available
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy


class SmartThingsApp:
    """
    Page Object class for common interactions and navigation flows in the
    SmartThings mobile application.
    """

    # Define a default wait time
    DEFAULT_TIMEOUT = 30

    def __init__(self, driver: WebDriver):
        """Initializes the Page Object with the current Appium driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def _get_element(self, locator):
        """Helper to wait for and find an element using unpacked locator."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click_element(self, locator):
        """Helper to wait for and click an element."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _get_text(self, locator):
        """Helper to wait for and get the text of an element."""
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def skip_initial_setup(self):
        """
        Handles the entire initial setup, navigation through intro screens,
        and allowance of required permissions by using the 'Skip' path.
        """

        print("Starting initial app navigation and setup skip...")

        # 1. Verify intro title
        title_text = self._get_text(SmartThingsLocators.INTRO_TITLE)
        print(f"First Page title is: {title_text}")

        # 2. Click through initial screens (Allow -> More -> Continue)
        self._click_element(SmartThingsLocators.INTRO_ALLOW_BUTTON)
        self._click_element(SmartThingsLocators.MORE_BUTTON)
        self._click_element(SmartThingsLocators.CONTINUE_BUTTON)

        # Wait for the next screen (which might be the long loading process)
        # 3. Click the SKIP button instead of Start SmartThings
        self.wait.until(EC.element_to_be_clickable(SmartThingsLocators.SKIP_BUTTON))
        self._click_element(SmartThingsLocators.SKIP_BUTTON)

        # 4. Handle permissions (Click 'While using the app' and two 'Allow' buttons)
        self._click_element(SmartThingsLocators.WHILE_USING_APP_PERMISSION)

        # Permission 1
        self._click_element(SmartThingsLocators.PERMISSION_ALLOW_BUTTON)

        # Permission 2 (Note: This might be the same button on a different screen)
        self._click_element(SmartThingsLocators.PERMISSION_ALLOW_BUTTON)

        # 5. Verify navigation to the home screen
        home_title = self._get_text(SmartThingsLocators.HOME_TITLE)
        print(f"Navigation complete. Home screen title is: {home_title}")

        return home_title