import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

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

time.sleep(5)

# Your automation code goes here
# driver.find_element(By.ID, 'com.android.calendar.AllInOneActivity').click()
# driver.find_element(By.CLASS_NAME, 'com.android.calendar.AllInOneActivity').click()
# driver.find_element(By.NAME, "com.android.calendar.AllInOneActivity").click()
# driver.find_element(By.XPATH, "//android.widget.TextInput[@index='1']").click()
# driver.find_element(By.TAG_NAME, "").click()

#Swipe from left to right on intro screen

# Get the device screen size
screen_size = driver.get_window_size()
screen_width = screen_size['width']
screen_height = screen_size['height']

# Define the start and end coordinates for the swipe
start_x = int(screen_width * 0.8)
end_x = int(screen_height * 0.4)
y = int(screen_height * 0.5)

# Perform the swipe gesture from left to right
print("Swipe from left to right")
TouchAction(driver).press(x=start_x, y=y).move_to(x=end_x, y=y).release().perform()
print("Swipe complete.")
# driver.swipe(start_x, y, end_x, y, 800) # The last parameter is the duration in milliseconds


# End the driver session
time.sleep(5)
# driver.quit()