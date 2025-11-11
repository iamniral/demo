from appium import webdriver

from model.options import Options


class Driver:

    def create_driver_and_return(self):
        options = Options().get_options()
        driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
        return driver
