# Test Objective:
# 1. Launch the app
# 2. Accept the permission
# 3. Redirect to Home screen & print home screen name


import time

from app_launch import getdriver
from locators import SmartThingsLocators

driver = getdriver()

# Navigation till home screen
title_text = driver.find_element(*SmartThingsLocators.INTRO_TITLE).text
print(f"First Page title is: {title_text}")

driver.find_element(*SmartThingsLocators.INTRO_ALLOW_BUTTON).click()
driver.find_element(*SmartThingsLocators.MORE_BUTTON).click()
driver.find_element(*SmartThingsLocators.CONTINUE_BUTTON).click()
time.sleep(5)  # Added for potential long loading/login process
# driver.find_element(*SmartThingsLocators.START_SMARTTHINGS_BUTTON).click()
driver.find_element(*SmartThingsLocators.SKIP_BUTTON).click()
time.sleep(5)

# App Permissions
driver.find_element(*SmartThingsLocators.WHILE_USING_APP_PERMISSION).click()
time.sleep(5)
# Permission 1
driver.find_element(*SmartThingsLocators.PERMISSION_ALLOW_BUTTON).click()
time.sleep(5)
# Permission 2
driver.find_element(*SmartThingsLocators.PERMISSION_ALLOW_BUTTON).click()
time.sleep(5)
home_title = driver.find_element(*SmartThingsLocators.HOME_TITLE).text
print(f"The home screen title is: {home_title}")

# End of driver session
time.sleep(2)
driver.quit()
