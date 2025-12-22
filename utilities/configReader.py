import configparser
import os

from conftest import ROOT_DIR


def readConfig(section, key):
    config = configparser.ConfigParser()
    config.sections()
    config.read("C:/Users/Niral.Shah/PycharmProjects/PythonProject/ConfigurationData/config.ini")
    return config.get(section, key)

print(readConfig("locators", "INTRO_TITLE"))