from appium import webdriver
from appium.options.common import AppiumOptions
import time

# Set up desired capabilities
options = AppiumOptions()
options.set_capability('platformName', 'Android')
options.set_capability('appium:deviceName', 'emulator-5554')  # Replace with your device name
options.set_capability('appium:automationName', 'UiAutomator2')
options.set_capability('appium:appPackage', 'com.google.android.calculator')  # Calculator's package name
options.set_capability('appium:appActivity', 'com.android.calculator2.Calculator') # Calculator's activity name

# Initialize the Appium driver
driver = webdriver.Remote('http://127.0.0.1:4723/', options=options)

print("Calculator app launched successfully!")

# Wait for a few seconds to see the app
time.sleep(5)

# Close the session
driver.quit()