import time
from selenium.webdriver.common.by import By

class SmartThingsLocators:
    """
    Stores all Appium locators for the SmartThings application.
    Locators are stored as tuples: (By strategy, locator value).
    """

    # --- Initial Screens / Navigation ---
    INTRO_TITLE = (By.XPATH, '//android.widget.TextView[@resource-id="com.samsung.android.oneconnect:id/introTitle"]')
    INTRO_ALLOW_BUTTON = (By.ID, 'com.samsung.android.oneconnect:id/intro_allow_button')
    MORE_BUTTON = (By.XPATH, '//android.widget.Button[@text = "More"]')
    CONTINUE_BUTTON = (By.XPATH, '//android.widget.Button[@text = "Continue"]')
    START_SMARTTHINGS_BUTTON = (By.XPATH, '//android.widget.Button[@text = "Start SmartThings"]')
    SKIP_BUTTON = (By.ID, 'com.samsung.android.oneconnect:id/cancel')

    # --- Permissions ---
    WHILE_USING_APP_PERMISSION = (By.XPATH, '//*[contains(@text,"While using the app")]')
    PERMISSION_ALLOW_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')

    # --- Home Screen ---
    HOME_TITLE = (By.XPATH, '//android.widget.TextView[@resource-id="com.samsung.android.oneconnect:id/title"]')
    SIGN_IN_BUTTON = (By.ID, 'com.samsung.android.oneconnect:id/signin_btn')

    # --- Login Screen ---
    EMAIL_INPUT = (By.XPATH, '//android.widget.EditText[@resource-id="iptLgnPlnID"]')
    PASSWORD_INPUT = (By.XPATH, '//android.widget.EditText[@resource-id="iptLgnPlnPD"]')
    SIGN_IN_FINAL_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="signInButton"]')

    # --- Find ID Screen ---
    FIND_ID_LINK = (By.XPATH, '//android.widget.TextView[@text="Find ID"]')
    GIVEN_NAME_INPUT = (By.XPATH, '//android.widget.EditText[@resource-id="givenName"]')
    FAMILY_NAME_INPUT = (By.XPATH, '//android.widget.EditText[@resource-id="familyName"]')
    DAY_INPUT = (By.XPATH, '//android.widget.EditText[@resource-id="day"]')
    MONTH_DROPDOWN = (By.XPATH, '//android.view.View[@resource-id="month"]')
    MONTHS_DROPDOWN = (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1"]')
    JULY_OPTION = (By.XPATH, '//android.widget.CheckedTextView[@text="July"]')
    YEAR_INPUT = (By.XPATH, '//android.widget.EditText[@resource-id="year"]')
    FIND_ID_FINAL_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="findIdButton"]')

    # --- Verification Message ---
    FOUND_ID_MESSAGE = (By.XPATH, '//android.widget.TextView[@text="We found 1 Email ID(s)."]')
    SIGN_IN_NOW_BUTTON = (By.XPATH, '//android.widget.Button[@text="Sign in now"]')

    #--- Explore SmartThings ---
    EXPLORE_SMARTTHINGS = (By.XPATH, '//android.widget.TextView[@resource-id="com.samsung.android.oneconnect:id/item_name" and @text="Explore SmartThings"]')
    NAVIGATE_BACK = (By.XPATH, '//android.widget.Button[@content-desc="Navigate up"]')
