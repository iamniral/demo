import base64
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

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

ts = time.strftime("%Y_%m_%d_%H_%M_%S")
activityName = driver.current_activity
fileName = activityName+ts
driver.save_screenshot("C:/Users/Niral.Shah/PycharmProjects/PythonProject/Screenshot"+fileName+".png")

# End of driver session
time.sleep(2)
driver.quit()




