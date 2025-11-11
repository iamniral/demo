import time

from driver_manager.driver import Driver


class TestLaunchApplication:

    def test_app_launch(self):
        driver = Driver().create_driver_and_return()
        print(driver.page_source)
        time.sleep(10)
        driver.quit()