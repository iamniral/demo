import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By


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
time.sleep(30) # Added for potential long loading/login process
driver.find_element(By.XPATH, f'//android.widget.Button[@text = "Start SmartThings"]').click()
time.sleep(5)

driver.find_element(By.XPATH, f'//*[contains(@text,"While using the app")]').click()
time.sleep(5)
# Permission 1
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()
time.sleep(5)
# Permission 2
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()

time.sleep(5)
home_title = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.samsung.android.oneconnect:id/title"]').text
print(f"The home screen title is: {home_title}")

# End of driver session
time.sleep(2)
driver.quit()
