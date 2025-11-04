import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SmartThingsLocators

# --- Capability Setup ---
options = AppiumOptions()
options.set_capability('platformName', 'Android')
options.set_capability('appium:deviceName', 'emulator-5554')
options.set_capability('appium:automationName', 'UiAutomator2')
# options.set_capability('appium:app', 'C:/Users/Niral.Shah/Documents/Appium/apk/SmartThings.apk')

# --- CLEANSED LAUNCH CAPABILITIES ---
options.set_capability('appium:appPackage', 'com.samsung.android.oneconnect')
options.set_capability('appium:appWaitActivity', '*')
options.set_capability('appium:appWaitDuration', 30000)


# Optional capabilities for stability
options.set_capability('appium:noReset', False)
options.set_capability('appium:skipDeviceInitialization', True)
options.set_capability('appium:ignoreHiddenApiPolicyError', True)

driver = webdriver.Remote('http://localhost:4723', options=options)

print("Smart Things App Launched successfully!")

# --- Initial Navigation ---
# Navigation till home screen
title_text = driver.find_element(*SmartThingsLocators.INTRO_TITLE).text
print(f"First Page title is: {title_text}")

driver.find_element(*SmartThingsLocators.INTRO_ALLOW_BUTTON).click()
driver.find_element(*SmartThingsLocators.MORE_BUTTON).click()
driver.find_element(*SmartThingsLocators.CONTINUE_BUTTON).click()
time.sleep(5)
# driver.find_element(*SmartThingsLocators.START_SMARTTHINGS_BUTTON).click()
driver.find_element(*SmartThingsLocators.SKIP_BUTTON).click()
time.sleep(5)

# --- Allow Permissions ---
driver.find_element(*SmartThingsLocators.WHILE_USING_APP_PERMISSION).click()
time.sleep(3)
# Permission 1
driver.find_element(*SmartThingsLocators.PERMISSION_ALLOW_BUTTON).click()
time.sleep(3)
# Permission 2
driver.find_element(*SmartThingsLocators.PERMISSION_ALLOW_BUTTON).click()
time.sleep(3)

home_title = driver.find_element(*SmartThingsLocators.HOME_TITLE).text
print(f"The home screen title is: {home_title}")
time.sleep(3)

# --- Find Account ID Flow ---
driver.find_element(*SmartThingsLocators.SIGN_IN_BUTTON).click()
time.sleep(15)
driver.find_element(*SmartThingsLocators.FIND_ID_LINK).click()
time.sleep(5)
driver.find_element(*SmartThingsLocators.GIVEN_NAME_INPUT).send_keys('Niral')
time.sleep(5)
driver.find_element(*SmartThingsLocators.FAMILY_NAME_INPUT).send_keys('Shah')
time.sleep(5)
driver.find_element(*SmartThingsLocators.DAY_INPUT).send_keys('21')
time.sleep(5)
driver.find_element(*SmartThingsLocators.MONTH_DROPDOWN).click()
time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(SmartThingsLocators.JULY_OPTION)
).click()

driver.find_element(*SmartThingsLocators.YEAR_INPUT).send_keys('1993')
time.sleep(5)
driver.find_element(*SmartThingsLocators.FIND_ID_FINAL_BUTTON).click()

# --- Assertion Step ---
time.sleep(5)
Found_ID_Element = driver.find_element(*SmartThingsLocators.FOUND_ID_MESSAGE)
EXPECTED_TEXT = "We found 1 Email ID(s)."
assert Found_ID_Element.text == EXPECTED_TEXT
print('Found 1 Email ID(s) in this app. Assertion passed.')

# End of driver session
driver.find_element(*SmartThingsLocators.SIGN_IN_NOW_BUTTON).click()
driver.quit()
