import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.by import By

# Step 1: Create an AppiumOptions object
options = AppiumOptions()

# Step 2: Set the desired capabilities for app installation
# Replace 'path/to/your/app.apk' with the actual absolute path to your APK file
options.set_capability('platformName', 'Android')
options.set_capability('appium:platformVersion', '16.0') # Set your device's Android version
options.set_capability('appium:deviceName', 'emulator-5554') # Set your device UDID
options.set_capability('appium:automationName', 'UiAutomator2')
options.set_capability('appium:app', 'C:/Users/Niral.Shah/Documents/Appium/apk/PanasonicMirAIe.apk')
# options.set_capability('appPackage', 'com.panasonic.in.miraie')
# options.set_capability('appActivity', 'com.panasonic.in.miraie.apptour.AppTourActivity')
# Optional capabilities
# options.set_capability('appium:noReset', True) # To prevent app data from being reset
# options.set_capability('appium:fullReset', False) # To prevent the app from being uninstalled after the test

# Step 3: Connect to the Appium server and create a new session
driver = webdriver.Remote('http://localhost:4723', options=options)
print("App has been installed and launched successfully!")
time.sleep(15)

# Get the device screen size
screen_size = driver.get_window_size()
width = screen_size['width']
height = screen_size['height']

# Perform the swipe gesture from right to left
print("Swiping from right to left using execute_script...")
driver.execute_script('mobile: swipeGesture', {
    'left': 0,         # Start X of the swipe area (top-left corner)
    'top': 0,          # Start Y of the swipe area (top-left corner)
    'width': width,    # Width of the swipe area
    'height': height,  # Height of the swipe area
    'direction': 'left', # Specify the direction
    'percent': 0.8     # Swipe dist   ance as a float between 0.0 and 1.0 (80%)
})
print("Swipe complete.")

#Click on Get Started
driver.find_element(By.ID, 'com.panasonic.in.miraie:id/button_get_started').click()
time.sleep(5)
driver.find_element(By.ID,'com.panasonic.in.miraie:id/panasonic_image').is_displayed()
print("Panasonic Image is displayed")
driver.find_element(By.ID, 'com.panasonic.in.miraie:id/enter_mobile_number').send_keys("shahniral01@gmail.com")
driver.find_element(By.ID, 'com.panasonic.in.miraie:id/password_container').send_keys("Vasupujy@3")
driver.find_element(By.ID, 'com.panasonic.in.miraie:id/loginButton').click()

# End the driver session
time.sleep(5)
driver.quit()

driver.find_element(By.LINK_)