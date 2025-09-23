from appium import webdriver
from appium.options.common import AppiumOptions
import time

# Set up desired capabilities
options = AppiumOptions()
options.set_capability('platformName', 'Android')
options.set_capability('appium:deviceName', '2a50ee87') # Replace with your device name
options.set_capability('appium:automationName', 'UiAutomator2')
options.set_capability('appium:appPackage', 'com.google.android.calendar')
options.set_capability('appium:appActivity', 'com.android.calendar.AllInOneActivity')
options.set_capability('appium:noReset', True) # Important for pre-installed apps
options.set_capability('appium:ignoreHiddenApiPolicyError', True)

# Initialize the Appium driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

print("Calendar app launched successfully!")

# Wait for a few seconds to see the app
time.sleep(5)

# Close the session
driver.quit()