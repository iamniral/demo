import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.set_capability('platformName', 'Android')
options.set_capability('appium:deviceName', 'emulator-5554')
options.set_capability('appium:automationName', 'UiAutomator2')
# options.set_capability('appium:app', 'C:/Users/Niral.Shah/Documents/Appium/apk/SmartThings.apk')

# --- CLEANSED LAUNCH CAPABILITIES ---
options.set_capability('appium:appPackage', 'com.samsung.android.oneconnect')

# Use wildcard on appWaitActivity to successfully wait for any activity to load
options.set_capability('appium:appWaitActivity', '*')
options.set_capability('appium:appWaitDuration', 30000)


# Optional capabilities for stability
options.set_capability('appium:noReset', False)
options.set_capability('appium:skipDeviceInitialization', True)
options.set_capability('appium:ignoreHiddenApiPolicyError', True)

driver = webdriver.Remote('http://localhost:4723', options=options)

print("Smart Things App Launched successfully!")

# Navigation till home screen
title_text = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.samsung.android.oneconnect:id/introTitle"]').text
print(f"First Page title is: {title_text}")

driver.find_element(By.ID, 'com.samsung.android.oneconnect:id/intro_allow_button').click()
driver.find_element(By.XPATH, f'//android.widget.Button[@text = "More"]').click()
driver.find_element(By.XPATH, f'//android.widget.Button[@text = "Continue"]').click()
time.sleep(23) # Added for potential long loading/login process
driver.find_element(By.XPATH, f'//android.widget.Button[@text = "Start SmartThings"]').click()
time.sleep(2)

# Allow permissions
driver.find_element(By.XPATH, f'//*[contains(@text,"While using the app")]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()
time.sleep(3)

home_title = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.samsung.android.oneconnect:id/title"]').text
print(f"The home screen title is: {home_title}")
time.sleep(3)

# Find your account ID
driver.find_element(By.ID,'com.samsung.android.oneconnect:id/signin_btn').click()
time.sleep(10)
driver.find_element(By.XPATH,'//android.widget.TextView[@text="Find ID"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="givenName"]').send_keys('Niral')
time.sleep(5)
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="familyName"]').send_keys('Shah')
time.sleep(5)
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="day"]').send_keys('21')
time.sleep(5)
driver.find_element(By.XPATH, '//android.view.View[@resource-id="month"]').click()
time.sleep(5)
# Select 'July' from the month dropdown using an explicit wait
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckedTextView[@text="July"]'))
).click()
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="year"]').send_keys('1993')
time.sleep(5)
driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="findIdButton"]').click()

# Assertion step
time.sleep(2)
Found_ID = driver.find_element(By.XPATH, '//android.widget.TextView[@text="We found 1 Email ID(s)."]')
EXPECTED_TEXT = "We found 1 Email ID(s)."
assert Found_ID.text == EXPECTED_TEXT
print('Found 1 Email ID(s) in this app.')

# End of driver session
driver.find_element(By.XPATH, '//android.widget.Button[@text="Sign in now"]').click()
driver.quit()
