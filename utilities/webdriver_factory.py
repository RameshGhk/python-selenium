"""
@package utilities

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from utilities.config_file_reader import ConfigFileReader
import os


class WebDriverFactory():

    def __init__(self, browser):
        yml_file_path = "../config/config.yml"
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, yml_file_path)
        cfg = ConfigFileReader(destinationFile)
        self.chrome = cfg.getChromeDriverPath()
        self.firefox = cfg.getFirefoxDriverPath()
        self.baseUrl = cfg.getBaseUrl()
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path = self.firefox)
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path = self.chrome)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver