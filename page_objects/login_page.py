from page_objects.base_page import BasePage
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators in login page for github              #Locator types for reference
    _loginLink = "//a[@href='/login']"              #xpath
    _emailField = "login_field"                     #id
    _passwordField = "password"                     #id
    _signInButton = "commit"                        #name
    _verifyLogin = "//p[@class='shelf-lead']"       #xpath


    def clickLoginLink(self):
        self.elementClick(self._loginLink, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._emailField, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._passwordField, locatorType="id")

    def clickSignIn(self):
        self.elementClick(self._signInButton, locatorType="name")

    def verifyLogin(self):
        element = self.isElementPresent(self._verifyLogin, locatorType="xpath")
        return element

    def verifyTitle(self):
        self.verifyPageTitle("GitHub")


    def userLogin(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        #self.clickSignIn()
