import yaml

class ConfigFileReader:

    def __init__(self, fileName):
        with open(fileName, "r") as ymlfile:
            self.config = yaml.load(ymlfile)
            self.driver_executable_path = self.config.get("driver_executable_path")
            self.url = self.config.get("url")


    def getChromeDriverPath(self):
        return self.driver_executable_path["chrome"]

    def getFirefoxDriverPath(self):
        return self.driver_executable_path["firefox"]

    def getBaseUrl(self):
        return self.url["baseUrl"]



"""
usage :
cfg = ConfigFileReader("...../config/yml_config.yml")
print(cfg.getChromeDriverPath())
print(cfg.getFirefoxDriverPath())

"""