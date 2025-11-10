import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from locators import SmartThingsLocators

def getdriver():
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
    return driver