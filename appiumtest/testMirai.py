import time
from appium import webdriver
from appium.options.common import AppiumOptions

# Step 1: Create an AppiumOptions object
options = AppiumOptions()

# Step 2: Set the desired capabilities for app installation
# Replace 'path/to/your/app.apk' with the actual absolute path to your APK file
options.set_capability('platformName', 'Android')
options.set_capability('appium:platformVersion', '16.0') # Set your device's Android version
options.set_capability('appium:deviceName', 'emulator-5554') # Set your device UDID
options.set_capability('appium:automationName', 'UiAutomator2')
options.set_capability('appium:app', 'C:/Users/Niral.Shah/Documents/Appium/apk/PanasonicMirAIe.apk') # Absolute path to the app

# Optional capabilities
# options.set_capability('appium:noReset', True) # To prevent app data from being reset
# options.set_capability('appium:fullReset', False) # To prevent the app from being uninstalled after the test

# Step 3: Connect to the Appium server and create a new session
driver = webdriver.Remote('http://localhost:4723', options=options)

print("App has been installed and launched successfully!")

# Your automation code goes here
# Example: interacting with elements in your app

# End the driver session
time.sleep(5)
driver.quit()