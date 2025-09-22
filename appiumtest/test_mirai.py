import time
from appium import webdriver



desired_caps = dict(
    deviceName='2a50ee87',
    platformName='Android',
    browserName='chrome',
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.get("http://www.google.com")
print(driver.title)
time.sleep(2)
driver.quit()
driver.back()