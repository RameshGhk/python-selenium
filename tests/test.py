"""
@pending_task
parameterize user credentials
"""

from page_objects.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class GithubLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.lp.userLogin("username", "password")
        titleResult = self.lp.verifyTitle()
        self.ts.mark(titleResult, "Title Verified")
        loginResult = self.lp.verifyLogin()
        self.ts.markFinal("test_login", loginResult, "Login Verified")