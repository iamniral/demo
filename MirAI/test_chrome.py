import time
from appium import webdriver
from appium.options.common import AppiumOptions

# Step 1: Create an AppiumOptions object
options = AppiumOptions()

# Step 2: Set the desired capabilities
options.set_capability('platformName', 'Android')
options.set_capability('appium:platformVersion', '16.0')
options.set_capability('appium:deviceName', 'emulator-5554')
options.set_capability('appium:browserName', 'Chrome')
options.set_capability('appium:automationName', 'UiAutomator2')
# Add the capability to enable automatic Chromedriver download
options.set_capability('appium:chromedriverAutodownload', True)
options.set_capability('appium:skipDeviceInitialization', True)
options.set_capability('appium:ignoreHiddenApiPolicyError', True)
options.set_capability('appium:noReset', True)

# Step 3: Connect to the Appium server and create a new session
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Your test commands
#driver.get("https://www.google.com/")
print(driver.title)
time.sleep(2)

# Step 4: End the driver session
driver.quit()