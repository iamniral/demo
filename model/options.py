import configparser
from appium.options.android import UiAutomator2Options
from conftest import ROOT_DIR

config = configparser.ConfigParser()
config.sections()
config.read("..\\ConfigurationData\\config.ini")

class Options:

    def get_options(self):
        options = UiAutomator2Options()
        options.platform_name = config["OPTIONS"]["platform name"]
        options.platform_version = config["OPTIONS"]["platform version"]
        options.device_name = config["OPTIONS"]["device name"]
        options.app_package = config["OPTIONS"]["appPackage"]
        options.app_wait_activity = config["OPTIONS"]["appWaitActivity"]
        options.udid = config["OPTIONS"]["ud id"]
        options.automation_name = config["OPTIONS"]["automation name"]
        # options.adb_port = config["OPTIONS"]["port"]
        options.use_new_wda = True

        return options
