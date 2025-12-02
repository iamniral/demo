import configparser
import os

from conftest import ROOT_DIR


def readConfig(section, key):
    config = configparser.ConfigParser()
    config.sections()
    config.read("..\\ConfigurationData\\config.ini")
    return config.get(section, key)

print(readConfig("locator", "INTRO_TITLE"))