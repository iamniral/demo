# Test Objective:
# 1. Capture video of scroll section

import base64
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

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

# --- Start Video ---
driver.start_recording_screen()


# --- Explore product (Scroll & Swipe) ---
driver.find_element(*SmartThingsLocators.EXPLORE_SMARTTHINGS).click()
time.sleep(10)

# --- Swipe Actions ---
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1118, 561)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(79, 561)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(3)

# --- Scroll action ---
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(625, 2400)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(625, 850)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(3)

# -- Navigate Back ---
# time.sleep(5)
# driver.find_element(*SmartThingsLocators.NAVIGATE_BACK).click()

# --- Stop Video Recording ---
video_rawdata = driver.stop_recording_screen()

# --- Video Name ---
video_name = driver.current_activity + time.strftime("%Y%m%d%H%M%S")

# --- File Path ---
filepath = os.path.join("C:/Users/Niral.Shah/PycharmProjects/PythonProject/SmartThings", video_name+".mp4")

# --- Converting base64 to .mp4 format ---
with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))

# End of driver session
time.sleep(2)
driver.quit()
